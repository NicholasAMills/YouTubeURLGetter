# YouTubeURLGetter
## _Helping YouTube content creators from YouTube's antics_

Retrieve all of a YouTube content creator's videos' title + url and save to a .csv file. 
Purpose: YouTube is deleting old videos that break new guidelines and asking for a URL for a deleted video if they want it reviewed. This will create a micro .csv database to capture a user's video title and its url to help with this problem.

## Installation
Install the dependencies.
```sh
pip install pandas
pip install google-api-python-client
```

## Running
In the creds.py file, set values for 
```
api_key => Your console.cloud.google.com api key
channel_id => YouTube user's unique channel id. Can be found by sending a GET request from the channel and looking at the META tags. CTRL+F 'channelid'
OUTPUT_FILE =>  Desired location & file name
```

Run command: ``` python .\YouTubeURLGetter\YouTubeURLGrabber.py ```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
