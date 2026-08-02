import re


def clean_comments(comments):

    cleaned_comments = []

    for comment in comments:

        # Remove URLs
        comment = re.sub(r"http\S+", "", comment)

        # Remove HTML tags
        comment = re.sub(r"<.*?>", "", comment)

        # Remove extra whitespace
        comment = " ".join(comment.split())

        # Skip empty comments
        if not comment:
            continue

        cleaned_comments.append(comment)

    return cleaned_comments