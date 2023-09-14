from yt_dlp import YoutubeDL

print('dl.py - v0.1a')
print('***This script requires yt-dlp and ffmpeg!***')
print('For a full list of supported sites, go to this link: https://github.com/yt-dlp/yt-dlp/blob/release/supportedsites.md \n')

# asks user to input url
input_url = input("Enter a URL: ")

# presets
audio = {
    'format': 'mp3/bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
    }

with YoutubeDL(audio) as ydl:
    ydl.download(input_url)


#>todo: add an option for best quality mp4, maybe with a menu or something idk
