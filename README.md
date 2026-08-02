# FeedbackHub AI

AI-powered YouTube comment analysis platform that transforms audience feedback into actionable insights using Natural Language Processing (NLP), sentiment analysis, topic extraction, and Google's Gemini AI.

---

## Table of Contents

1. Overview
2. Problem Statement
3. Solution
4. Key Features
5. System Architecture
6. Technology Stack
7. Project Structure
8. Installation
9. Usage
10. Future Improvements
11. License

---

# Overview

Understanding audience feedback on YouTube videos becomes increasingly difficult as the number of comments grows. Manually reading hundreds or thousands of comments is time-consuming and often fails to provide an overall understanding of audience sentiment.

FeedbackHub AI automates this process by collecting comments from any public YouTube video, analyzing them using Natural Language Processing techniques, and generating a structured AI-powered audience report.

The project combines traditional NLP techniques with Large Language Models (LLMs) to provide meaningful insights rather than raw comment data.

---

# Problem Statement

Content creators, marketers, educators, and businesses often rely on YouTube comments to understand audience opinions.

However, large comment sections present several challenges:

- Reading every comment is impractical.
- Important feedback is buried among repetitive comments.
- Identifying overall audience sentiment is difficult.
- Discovering trending discussion topics requires manual effort.
- Extracting meaningful insights from thousands of comments is time-consuming.

FeedbackHub AI addresses these challenges through automated AI-powered analysis.

---

# Solution

FeedbackHub AI performs an end-to-end analysis pipeline:

1. Accepts a public YouTube video URL.
2. Retrieves comments using the YouTube Data API.
3. Cleans and preprocesses comment text.
4. Performs sentiment analysis.
5. Extracts the most discussed topics.
6. Selects representative comments.
7. Uses Google's Gemini AI to generate a comprehensive audience insights report.
8. Presents all results in an easy-to-understand web dashboard.

---

# Key Features

- Analyze comments from any public YouTube video
- Retrieve comments using the YouTube Data API v3
- Automatic comment preprocessing and cleaning
- Sentiment analysis using Hugging Face Transformers
- Topic extraction using TF-IDF and spaCy
- AI-generated audience insights using Google Gemini
- Summary statistics for positive, neutral, and negative comments
- Responsive web interface built with Flask and Bootstrap
- Modular project architecture for easy maintenance

---

# System Architecture

```text
                    User
                      │
                      ▼
           Enter YouTube Video URL
                      │
                      ▼
           YouTube Data API v3
                      │
                      ▼
            Retrieve Video Comments
                      │
                      ▼
          Comment Cleaning Pipeline
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
 Sentiment Analysis         Topic Extraction
         │                         │
         └────────────┬────────────┘
                      ▼
      Representative Comment Selection
                      │
                      ▼
          Google Gemini AI Analysis
                      │
                      ▼
         AI Audience Insights Report
                      │
                      ▼
            FeedbackHub AI Dashboard
```

---

# Technology Stack

## Backend

- Python
- Flask

The backend manages request handling, API communication, NLP processing, and AI report generation.

---

## Artificial Intelligence & NLP

- Google Gemini API
- Hugging Face Transformers
- spaCy
- Scikit-learn (TF-IDF)
- NLTK

These libraries are responsible for sentiment analysis, topic extraction, natural language preprocessing, and AI-generated audience reports.

---

## APIs

- YouTube Data API v3
- Google Gemini API

The application retrieves public YouTube comments and generates AI-powered insights using Google's latest language models.

---

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

The frontend provides a clean and responsive interface for displaying analysis results.

---

# Project Structure

```text
FeedbackHub-AI/
│
├── ai/
│   ├── gemini_service.py
│   ├── report_generator.py
│   └── topic_extractor.py
│
├── services/
│   ├── comment_processor.py
│   ├── sentiment.py
│   └── youtube_api.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── index.html
│
├── utils/
│   └── utils.py
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Directory Description

| Directory | Purpose |
|------------|---------|
| **ai/** | Gemini integration and AI report generation |
| **services/** | Core application logic including sentiment analysis and YouTube API interaction |
| **templates/** | HTML templates rendered by Flask |
| **static/** | CSS and JavaScript assets |
| **utils/** | Utility functions and helper methods |

---

# Installation

## Clone the repository

```bash
git clone https://github.com/AdmirableMe/FeedbackHub-AI.git
```

Navigate into the project directory.

```bash
cd FeedbackHub-AI
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

# Usage

1. Launch the application.
2. Paste a public YouTube video URL.
3. Click **Analyze**.
4. Wait while comments are collected and processed.
5. Review:
   - Sentiment distribution
   - Trending topics
   - AI-generated audience insights
   - Representative comments

---

# Future Improvements

The project is designed with extensibility in mind.

Planned enhancements include:

- Interactive sentiment charts
- Downloadable PDF reports
- Search history
- Comparison between multiple YouTube videos
- Multi-language comment analysis
- User authentication
- Cloud deployment
- Advanced analytics dashboard
- Export analysis results as CSV

---

# License

This project is licensed under the MIT License.

See the LICENSE file for more information.
