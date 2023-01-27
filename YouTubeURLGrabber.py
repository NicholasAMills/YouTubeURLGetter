from googleapiclient.discovery import build
import creds
import pandas as pd


def call_playlist_items_api(service, playlist_id, next_page_token):
    '''
    API 'service' set for playlist items
    Goal: Retrieve video URL's
    Params:
        service: api service
        playlist_id: 'uploads' playlist id
        next_page_token: token for multiple pages. Default case set to empty (no value) for first page
    Returns:
        API response
    '''
    try:
        if next_page_token is not None:
            request = service.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken = next_page_token
            )
        else:
            request = service.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50
            )
        return request.execute()
        
    except Exception as e:
        print("An error occurred in call_playlist_items_api: " + str(e))

def call_channels_api(service, channel_id):
    '''
    API 'service' set for channels
    Goal: Retrieve "uploads" playlist id to use as a parameter for call_playlist_items_api 
    Params:
        service: api service
        channel_id: channel id (Must manually search for as of right now)
    Returns:
        API response
    '''
    try:
        request = service.channels().list(
            part='contentDetails',
            #   To find ID, make a GET request of the user's channel page (https://www.youtube.com/@UserHere) and check the META data. CTRL+F for 'channelid' and look for something along the lines of <meta itemprop="channelId" content="###############">
            #   the 'content' value will be found in other tags if it's correct. Should be fairly easy to confirm. Check the bottom-most result
            id=channel_id
        )
        return request.execute()
    except Exception as e:
        print("An error occurred in call_channels_api: " + str(e))

def call_videos_api(service, video_id):
    '''
    API 'service' set for videos
    Goal: Get video title
    Params:
        service: api service
        video_id: video id to retrieve name from
    '''
    try:
        request = service.videos().list(
            part='snippet',
            id=video_id
        )
        return request.execute()
    except Exception as e:
        print("An error occurred in call_videos_api: " + str(e))

try:
    print("====STARTING JOB====")
    api_key = creds.api_key
    channel_id = creds.channel_id
    service = build('youtube', 'v3', developerKey=api_key)

    # Get 'uploads' playlist id
    channels_response = call_channels_api(service, channel_id)
    uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Loop breaker. Starting as True to get through loop at least once
    has_next_page = True

    url_list = []
    count = 1

    # Call to first page
    playlist_items_response = call_playlist_items_api(service, uploads_playlist_id, None)

    # Will go through at least once
    while has_next_page:
        # Get next page token
        print('.')
        if 'nextPageToken' in playlist_items_response:
            has_next_page = True
            next_page = playlist_items_response['nextPageToken']
            # Work with data
            for i in playlist_items_response['items']:
                video_id = i['contentDetails']['videoId']
                videos_response = call_videos_api(service, video_id)
                video_title = videos_response['items'][0]['snippet']['title']
                url_list.append([str(video_title), "youtube.com/watch?v="+str(video_id)])
            # Call next page
            playlist_items_response = call_playlist_items_api(service, uploads_playlist_id, next_page)
        else:
            has_next_page = False
            # Work with data
            for i in playlist_items_response['items']:
                video_id = i['contentDetails']['videoId']
                videos_response = call_videos_api(service, video_id)
                video_title = videos_response['items'][0]['snippet']['title']
                url_list.append([str(video_title), "youtube.com/watch?v="+str(video_id)])

    df = pd.DataFrame(url_list, columns=['Title', 'Url'])
    df.to_csv(creds.OUTPUT_FILE, index=True)
    # for i in url_list:
    #     print(count, i)
    #     count+=1
    service.close()
    print("==========COMPLETE============")
except Exception as e:
    print("ERROR: " + str(e))

