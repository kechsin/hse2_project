import scrapetube
videos = scrapetube.get_channel("UCawVzkkGUvxTvwn_c_WJ-lA")
for video in videos:
    print(video['videoId'])