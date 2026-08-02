from flask import Flask, render_template, request
import markdown

from utils.utils import get_video_id

from services.youtube_api import get_comments
from services.comment_processor import clean_comments
from services.sentiment import analyze_sentiment

from ai.topic_extractor import extract_topics
from ai.report_generator import prepare_comments
from ai.gemini_service import gemini

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    comments = []
    sentiment = None
    topics = []
    ai_report = None

    if request.method == "POST":

        url = request.form["url"].strip()

        video_id = get_video_id(url)

        if video_id:

            # Fetch comments
            comments = get_comments(video_id)

            # Clean comments
            comments = clean_comments(comments)

            # Sentiment Analysis
            sentiment = analyze_sentiment(comments)

            # Topic Extraction
            topics = extract_topics(comments)

            # Select representative comments
            sample_comments = prepare_comments(comments)

            # Generate AI report
            ai_report = gemini.generate_report(sample_comments)

            # Convert Markdown to HTML
            ai_report = markdown.markdown(
                ai_report,
                extensions=["extra", "sane_lists"]
            )

    return render_template(
        "index.html",
        comments=comments,
        sentiment=sentiment,
        topics=topics,
        ai_report=ai_report
    )


if __name__ == "__main__":
    app.run(debug=True)