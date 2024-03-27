import cluster_get
clusters = ["music", "politics", "science", "art", "sport", "funny", "games"]
for i in clusters:
    cluster_get.save_videos(i, 20)
    cluster_get.save_comments(i, 50)
