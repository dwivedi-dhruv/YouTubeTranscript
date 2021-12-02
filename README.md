# YouTubeTranscript
**YouTubeTranscript** will provide the Transcript of the Youtube videos when url is provided and also generates JSON file for the same.

## Software Requirements

* Python `3.8`

## Install

It is recommended to [install this module by using pip](https://pypi.org/project/youtube-transcript-api/):

```
pip install youtube_transcript_api
```

### Downloading the Code

* Go to (<https://github.com/dwivedi-dhruv/YouTubeTranscript>) and click on **Fork**
* You will be redirected to *your* fork, `https://github.com/<your_user_name>YouTubeTranscript/`
* Open the terminal, change to the directory where you want to clone the **YouTubeTranscript** repository
* Clone your repository using `git clone https://github.com/<your_user_name>/YouTubeTranscript`
* Enter the cloned directory using `cd youtube_caption/`


### Running server

* Change directory to **YouTubeTranscript** `cd youtube_caption`
* Run the server `python manage.py runserver`

## Working

It is getting the Transcript from the Youtube videos when **YouTube url** is provided. When the url is provided, it extracts its **VideoID** (which is unique for each of the video on the YouTube). If some video don't have transcript, so it will return the message (Subtitle does not exist) otherwise it will first store the data in the database and redirect to the other page which has Transcript printed over there. It will also create a **transcript.json** file for the same video.
