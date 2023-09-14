from yt_dlp import YoutubeDL

print('dl.py - v0.1a')
print('***This script requires yt-dlp and ffmpeg!***')
print('For a full list of supported sites, go to this link: https://github.com/yt-dlp/yt-dlp/blob/release/supportedsites.md \n')

# asks user to input url
input_url = input("Enter a URL: ") #>todo add validation later

#here we give the user the option to download their file as an mp3 file or a video file also i just cut and pasted this from the internet haha
# options = ['video', 'audio']

# user_input = ''

# input_message = "Options:\n"

# for index, item in enumerate(options):
#     input_message += f'{index+1}) {item}\n'

# input_message += 'Type in number corresponding to option: '

# while user_input not in map(str, range(1, len(options) + 1)):
#     user_input = input(input_message)

#presets
# video = {
#     'format': 'mp4/bestvideo'
#     #>todo: finish settings
#     }

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