# 🎯 FeedbackHub AI

<p align="center">

AI-powered YouTube Comment Analysis Platform built using Flask, NLP, Hugging Face Transformers, and Google Gemini AI.

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?logo=google)
![YouTube API](https://img.shields.io/badge/API-YouTube_Data-red?logo=youtube)
![Hugging Face](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![spaCy](https://img.shields.io/badge/NLP-spaCy-09A3D5)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

</p>

---

Analyze thousands of YouTube comments in seconds and generate AI-powered audience insights, sentiment analysis, trending topics, and structured reports—all from a single video URL.

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Future Roadmap](#-future-roadmap)
- [License](#-license)

## 📖 Overview

YouTube comment sections often contain valuable audience feedback, suggestions, opinions, and discussions. However, manually reading hundreds or thousands of comments to understand audience sentiment is inefficient and time-consuming.

FeedbackHub AI automates this process by collecting comments from any public YouTube video, analyzing them using Natural Language Processing (NLP) techniques, and generating a structured AI-powered audience report.

The project combines traditional machine learning techniques with Google's Gemini AI to transform raw comment data into meaningful insights that help users quickly understand audience perception.

## ⚠️ Problem Statement

Large YouTube comment sections are difficult to analyze manually.

Common challenges include:

- Thousands of comments requiring manual review
- Difficulty understanding overall audience sentiment
- Important feedback hidden among repetitive comments
- Trending discussion topics not immediately visible
- Time-consuming analysis for creators and businesses

These challenges make it difficult to quickly understand audience opinion and identify meaningful feedback.

## 💡 Solution

FeedbackHub AI provides an automated analysis pipeline that converts large volumes of YouTube comments into structured insights.

The application:

- Retrieves comments using the YouTube Data API
- Cleans and preprocesses comment text
- Performs sentiment analysis using Hugging Face Transformers
- Extracts trending topics using TF-IDF and spaCy
- Selects representative comments
- Generates an AI-powered audience report using Google Gemini
- Displays all results through a responsive Flask web application

## 🚀 Features

### AI Analysis

- AI-generated audience insights using Google Gemini
- Automated summary of large YouTube comment sections
- Actionable audience feedback reports

### Natural Language Processing

- Sentiment analysis using Hugging Face Transformers
- Topic extraction using TF-IDF
- Named Entity Recognition (NER) using spaCy
- Comment preprocessing and text cleaning

### YouTube Integration

- Analyze comments from any public YouTube video
- Fetch comments using the YouTube Data API v3
- Automatic retrieval of large comment datasets

### Web Application

- Interactive Flask-based dashboard
- Responsive Bootstrap interface
- Comment preview section
- Topic visualization
- Sentiment statistics

## 🏗️ System Architecture

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
          ┌───────────┴───────────┐
          ▼                       ▼
  Sentiment Analysis      Topic Extraction
          │                       │
          └───────────┬───────────┘
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

## 🛠️ Technology Stack

### Backend

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Web framework and application routing |

---

### Artificial Intelligence & NLP

| Technology | Purpose |
|------------|---------|
| Google Gemini | AI-powered audience report generation |
| Hugging Face Transformers | Sentiment analysis |
| spaCy | Natural language processing and named entity recognition |
| Scikit-learn | TF-IDF topic extraction |
| NLTK | Text preprocessing |

---

### APIs

| Technology | Purpose |
|------------|---------|
| YouTube Data API v3 | Retrieve public YouTube comments |
| Google Gemini API | Generate AI-powered summaries |

---

### Frontend

| Technology | Purpose |
|------------|---------|
| HTML5 | Page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive layout |
| JavaScript | Client-side interactions |

## 📂 Project Structure

```text
FeedbackHub-AI/
│
├── ai/
│   ├── gemini_service.py
│   ├── report_generator.py
│   └── topic_extractor.py
│
├── services/
│   ├── youtube_api.py
│   ├── sentiment.py
│   └── comment_processor.py
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

| Directory | Description |
|------------|-------------|
| **ai/** | AI integration, report generation, and topic extraction |
| **services/** | Core business logic including YouTube API interaction and sentiment analysis |
| **templates/** | HTML templates rendered by Flask |
| **static/** | CSS and JavaScript assets |
| **utils/** | Helper functions and utilities |
