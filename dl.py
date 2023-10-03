from yt_dlp import YoutubeDL
from urllib.parse import urlparse

# defines what a valid url is
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

print('dl.py - v0.2a')
print('***This script requires yt-dlp and ffmpeg!***')
print('For a full list of supported sites, go to this link: https://github.com/yt-dlp/yt-dlp/blob/release/supportedsites.md \n')

# asks user to input url, additionally validates if it is a url or not
while True:
    input_url = input("Enter a URL: ")
    if is_valid_url(input_url):
        break
    else:
        print("Invalid URL. Please enter a valid URL.")

# defines the avaliable options to use, being video and audio
options = ['video', 'audio']

# after user is prompted to enter url the user is then asked to download either video or audio
print("Options:")
for index, item in enumerate(options):
    print(f'{index+1}) {item}')

user_input = input("Type in the number corresponding to the option: ")

# validates options
while user_input not in map(str, range(1, len(options) + 1)):
    print("Invalid input. Please choose a valid option.")
    user_input = input("Type in the number corresponding to the option: ")

# miswift 25/09/2023 18:49 what about you add a cropping setting to video or songs of your dl.py?
# i feel like this would be a good idea to implement but the thing is it might be annoying for some users as that might not want to crop their videos every single
# time they download someting, might implement some sort of configuration json file which allows users to enable/disable features of the program, for example
# they could make it so that they can change the download directory of audio and video files in it as well as enabling the feature i am thinking of implementing

# converts user choice to integer
user_choice = int(user_input)

# presets for video/audio options
video = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

audio = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
}

# if the integer selected equals to 1, the program will download a video, anything else and it will download audio
if user_choice == 1:
    ydl_opts = video
else:
    ydl_opts = audio

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([input_url])
