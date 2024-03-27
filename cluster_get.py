import scrapetube
from googleapiclient.discovery import build
import json


def save_videos(cluster_name, lim):
    f1 = open("channels.json")
    all_channels = json.loads(f1.read())
    f1.close()
    channels = all_channels[cluster_name]
    videos = []
    for i in channels:
        videos_i = scrapetube.get_channel(i, limit=lim)
        try:
            videos = videos + [j['videoId'] for j in list(videos_i)]
        except:
            f = open(f"data/failed_{cluster_name}.txt", "a")
            f.write("getting video-ids: " + i + "\n")
            f.close()
    f2 = open(f"data/videos_{cluster_name}.txt", "w")
    for i in videos:
        f2.write(i + "\n")


def video_comments(video_id, api_key, limit, cluster):  # всю эту функцию я откуда-то взяла и мало меняла
    n = 0
    comments = []
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
    try:
        video_response = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id
        ).execute()
    except:
        f = open(f"data/failed_{cluster}.txt", "a")
        f.write("Getting comments: " + video_id + "\n")
        f.close()
        return []
    while video_response and n < limit:
        for item in video_response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment.replace('\n', ' '))
            n += 1
            replycount = item['snippet']['totalReplyCount']
            if replycount > 0:
                try:
                    for reply in item['replies']['comments']:
                        # Extract reply
                        reply_text = reply['snippet']['textDisplay']

                        # Store reply is list
                        comments.append(reply_text.replace('\n', ' '))
                        n += 1
                        if n > limit:
                            return comments
                except:
                    f = open(f"data/failed_{cluster}.txt", "a")
                    f.write("Getting comment replies: " + video_id + "\n")
                    f.close()

        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                pageToken=video_response['nextPageToken']
            ).execute()
        else:
            break
    return comments


def save_comments(cluster_name, lim):
    f1 = open(f"data/videos_{cluster_name}.txt")
    videos = f1.read().split("\n")
    f1.close()
    with open("secret.txt") as f2:
        api_key = f2.read().strip()
    f3 = open(f"data/comments_{cluster_name}.txt", "wb")
    for i in videos:
        f3.write(("\n".join(video_comments(i, api_key, lim, cluster_name)) + "\n").encode("utf8"))
    f3.close()