# prompt: install transformers
!pip install -q transformers

!pip install -q youtube_transcript_api

from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

youtube_video="your youtube video link"

video_id= youtube_video.split("=")[1]
#video_id

YouTubeTranscriptApi.get_transcript(video_id)
transcript=YouTubeTranscriptApi.get_transcript(video_id)

result= ""
for i in transcript:
  result+=' '+i['text']
print(len(result))

#it used BART summarizer
summarizer=pipeline('summarization')

num_iters=int(len(result)/1000)
summarized_text=[]
for i in range(0, num_iters+1):
  start=0
  start=i*1000
  end=(i+1)*1000
  out=summarizer(result[start:end])
  out=out[0]
  out=out['summary_text']
  summarized_text.append(out)
  
#output
str(summarized_text)