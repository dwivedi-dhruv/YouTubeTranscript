import json
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from .models import *

def index(request):
    error_msg = ""
    if request.method == 'POST':

        url = request.POST['url']
        # after ?v= in url is videoID 
        # extracting the videoID
        index = 2
        videoID=""
        while(index < len(url)):
            if(url[index]=='=' and url[index-1]=='v' and url[index-2]=='?'):
                break
            else:
                index+=1
        index+=1
        while(index<len(url) and url[index]!='&'):
            videoID+=url[index]
            index+=1

        # check if data exists in the database or not
        # if it exists then redirect to the Caption_generator page
        # else save the data in the database
        
        if transcriptModel.objects.filter(videoID = videoID).exists():
            data = transcriptModel.objects.get(videoID = videoID)
            return HttpResponseRedirect(reverse("caption_generator", args=(data.id, )))
        else:
            # exception comes when some videos dont have subtitles and some age-restricted videos
            # to handle that situations 
            try:
                # using the srt variable with the list of dictonaries
                # obtained by the the .get_transcript() function

                srt = YouTubeTranscriptApi.get_transcript(videoID,languages=['en'])
                formatter = JSONFormatter()
                # .format_transcript(transcript) turns the transcript into a JSON string.
                json_formatted = formatter.format_transcript(srt, indent=2)
                newTranscript =  transcriptModel(videoID=videoID, transcript= json_formatted)
                newTranscript.save()
                data = transcriptModel.objects.get(videoID = videoID)
                return HttpResponseRedirect(reverse("caption_generator", args=(data.id, )))
            except Exception as e:
                error_msg = "Subtitles are disabled for this video"
    return render(request, 'caption/main.html', {'error_msg': error_msg} )
    

def caption_generator(request, pk):
    # given the primary key of the required data
    # first saving the data in transcript.json file 
    # after that print the data as a subtitle
    data = transcriptModel.objects.get(pk = pk)
    with open('transcript.json', 'w', encoding='utf-8') as json_file:
        json_file.write(data.transcript)
    f = open('transcript.json')
    subtitle = ""
    data = json.load(f)
    for i in data:
            subtitle+=i['text']
            subtitle+=" "
    return render(request, 'caption/print_caption.html', {'subtitle': subtitle} )