from __future__ import unicode_literals
from pydub import AudioSegment
import youtube_dl
import sys
import os

id = sys.argv[1]
if 'youtube.com' in id:
    id = id[id.index('=')+1:]

ydl_opts = {'format':'251', 'outtmpl':id+".webm"}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v='+id])

AudioSegment.from_file(id+'.webm').export(id+'.mp3', format="mp3")
os.remove(id+'.webm')