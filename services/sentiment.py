from transformers import pipeline


class SentimentAnalyzer:

    def __init__(self):

        self.classifier = pipeline(
            "sentiment-analysis"
        )

    def analyze(self, comments):

        if not comments:

            return {
                "total": 0,
                "positive": 0,
                "neutral": 0,
                "negative": 0
            }

        positive = 0
        negative = 0
        neutral = 0

        for comment in comments:

            try:

                result = self.classifier(comment[:512])[0]

                label = result["label"].upper()
                score = result["score"]

                if label == "POSITIVE":

                    positive += 1

                elif label == "NEGATIVE":

                    if score > 0.90:
                        negative += 1
                    else:
                        neutral += 1

                else:

                    neutral += 1

            except Exception:

                neutral += 1

        total = len(comments)

        return {

            "total": total,

            "positive": round((positive / total) * 100, 1),

            "neutral": round((neutral / total) * 100, 1),

            "negative": round((negative / total) * 100, 1)
        }


sentiment_analyzer = SentimentAnalyzer()


def analyze_sentiment(comments):

    return sentiment_analyzer.analyze(comments)