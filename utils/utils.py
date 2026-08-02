from urllib.parse import urlparse, parse_qs


def get_video_id(url):
    """
    Extract the YouTube video ID from different types of URLs.

    Supported formats:
    https://www.youtube.com/watch?v=VIDEO_ID
    https://youtu.be/VIDEO_ID
    https://youtube.com/shorts/VIDEO_ID
    https://youtube.com/live/VIDEO_ID
    """

    try:
        parsed_url = urlparse(url)

        # Standard YouTube URL
        if "youtube.com" in parsed_url.netloc:

            # Watch URL
            if parsed_url.path == "/watch":
                return parse_qs(parsed_url.query).get("v", [None])[0]

            # Shorts URL
            elif parsed_url.path.startswith("/shorts/"):
                return parsed_url.path.split("/")[2]

            # Live URL
            elif parsed_url.path.startswith("/live/"):
                return parsed_url.path.split("/")[2]

        # Shortened URL
        elif "youtu.be" in parsed_url.netloc:
            return parsed_url.path.lstrip("/")

    except Exception:
        return None

    return None