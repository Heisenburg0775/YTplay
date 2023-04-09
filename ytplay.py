import youtubesearchpython
import yt_dlp as youtube_dl
import os
search = input("Search: ")

if search is None:
    print("Please provide a valid argument")
else:
    result = youtubesearchpython.VideosSearch(search,limit=1)
    url = result.result()["result"][0]["link"]

    options = {
    "format":"best",
    "quiet":True,
    "simulate":True,
    "forceurl":True
    }

    result = youtube_dl.YoutubeDL(options).extract_info(url)['url']
    os.system("cls")
    os.system(f'ffplay -autoexit "{result}"')
  


