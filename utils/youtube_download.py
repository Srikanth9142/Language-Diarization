# from _future_ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '8000'
    ],
    'prefer_ffmpeg': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    path=['https://youtu.be/AL8rb1mRojU']
    for i in path:
        ydl.download([i])
