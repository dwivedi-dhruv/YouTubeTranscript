import json
from django.shortcuts import render, redirect
from django.contrib import messages
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
    

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
        
        try:
            # using the srt variable with the list of dictonaries
            # obtained by the the .get_transcript() function
            srt = YouTubeTranscriptApi.get_transcript(videoID,languages=['en'])
            formatter = JSONFormatter()

            # .format_transcript(transcript) turns the transcript into a JSON string.
            json_formatted = formatter.format_transcript(srt, indent=2)
            
            with open('transcript.json', 'w', encoding='utf-8') as json_file:
                json_file.write(json_formatted)
            return redirect('/caption_generator')
 
        except Exception as e:
	        error_msg = "Subtitles are disabled for this video"
    return render(request, 'caption/main.html', {'error_msg': error_msg} )
    

def caption_generator(request):
    f = open('transcript.json')
    subtitle = ""
    data = json.load(f)
    for i in data:
            subtitle+=i['text']
            subtitle+=" "
    return render(request, 'caption/print_caption.html', {'subtitle': subtitle} )