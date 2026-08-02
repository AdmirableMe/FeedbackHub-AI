from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate_report(self, comments):

        comments_text = "\n".join(
            f"- {comment}" for comment in comments
        )

        prompt = f"""
You are an expert product analyst.

You are analyzing YouTube comments.

Your job is to produce a concise, professional report.

Use Markdown formatting.

Return ONLY the report.

Structure your response exactly like this:

# Executive Summary

(2-4 sentences)

# Positive Highlights

- Point 1
- Point 2
- Point 3

# Negative Highlights

- Point 1
- Point 2
- Point 3

# Viewer Suggestions

- Point 1
- Point 2
- Point 3

# Overall Verdict

(2-3 sentences)

Here are the comments:

{comments_text}
"""

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text.strip()


gemini = GeminiService()