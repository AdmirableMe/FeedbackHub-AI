import re
from collections import Counter

import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

# NLTK stop words
stop_words = set(stopwords.words("english"))

# Extra words we don't want as topics
custom_stop_words = {
    "video",
    "videos",
    "youtube",
    "watch",
    "watched",
    "watching",
    "people",
    "person",
    "thing",
    "things",
    "really",
    "guys",
    "guy",
    "one",
    "would",
    "could",
    "also",
    "even",
    "get",
    "got",
    "make",
    "made",
    "look",
    "looks",
    "looking",
    "know",
    "well",
    "good",
    "great",
    "lol",
    "lmao",
    "bro",
    "yeah",
    "yes",
    "nah",
    "im",
    "ive",
    "dont",
    "didnt"
}

stop_words.update(custom_stop_words)


def preprocess(comment):

    comment = comment.lower()

    comment = re.sub(r"http\S+", "", comment)

    comment = re.sub(r"[^a-zA-Z\s]", " ", comment)

    doc = nlp(comment)

    tokens = []

    for token in doc:

        if token.is_stop:
            continue

        if token.is_punct:
            continue

        lemma = token.lemma_.strip()

        if len(lemma) < 3:
            continue

        if lemma in stop_words:
            continue

        tokens.append(lemma)

    return " ".join(tokens)


def extract_named_entities(comments):

    entities = []

    for comment in comments:

        doc = nlp(comment)

        for ent in doc.ents:

            if ent.label_ in {
                "PERSON",
                "ORG",
                "PRODUCT",
                "WORK_OF_ART",
                "EVENT"
            }:

                text = ent.text.strip()

                if len(text) > 2:

                    entities.append(text)

    counter = Counter()

    for entity in entities:
        counter[entity.title()] += 1

    return [
        entity
        for entity, count in counter.most_common(5)
    ]


def extract_topics(comments, top_n=10):

    if not comments:
        return []

    processed = [
        preprocess(comment)
        for comment in comments
    ]

    vectorizer = TfidfVectorizer(
        max_features=1000,
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform(processed)

    feature_names = vectorizer.get_feature_names_out()

    scores = matrix.sum(axis=0).A1

    ranked = sorted(
        zip(feature_names, scores),
        key=lambda x: x[1],
        reverse=True
    )

    tfidf_topics = []

    for word, score in ranked:

        if word not in tfidf_topics:

            tfidf_topics.append(word)

        if len(tfidf_topics) >= top_n:

            break

    named_entities = extract_named_entities(comments)

    final_topics = []

    for entity in named_entities:

        if entity not in final_topics:

            final_topics.append(entity)

    for topic in tfidf_topics:

        topic = topic.title()

        if topic not in final_topics:

            final_topics.append(topic)

    return final_topics[:top_n]