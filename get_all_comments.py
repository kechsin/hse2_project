import claster_get
clusters = ["politics", "science", "art", "sport", "funny", "games"]
for i in clusters:
    claster_get.save_videos(i, 20)
    claster_get.save_comments(i, 50)
