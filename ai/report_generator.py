import random


def prepare_comments(comments, max_comments=40):
    """
    Select a representative set of comments for Gemini.

    - Remove duplicates
    - Ignore very short comments
    - Shuffle to avoid bias
    - Return at most max_comments comments
    """

    unique_comments = []
    seen = set()

    for comment in comments:

        comment = comment.strip()

        if len(comment) < 20:
            continue

        lower = comment.lower()

        if lower in seen:
            continue

        seen.add(lower)
        unique_comments.append(comment)

    random.shuffle(unique_comments)

    return unique_comments[:max_comments]