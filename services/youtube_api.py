from googleapiclient.discovery import build

from config import YOUTUBE_API_KEY

youtube = build(
    "youtube",
    "v3",
    developerKey=YOUTUBE_API_KEY
)


def get_comments(video_id):

    comments = []
    next_page_token = None

    while True:

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )

        response = request.execute()

        for item in response["items"]:

            comment = (
                item["snippet"]
                ["topLevelComment"]
                ["snippet"]
                ["textDisplay"]
            )

            comments.append(comment)

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments