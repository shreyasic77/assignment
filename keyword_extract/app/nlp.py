from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text: str, top_n: int = 10) -> List[str]:
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    indices = X[0].indices
    feature_names = vectorizer.get_feature_names_out()
    keywords = [feature_names[i] for i in indices]
    return keywords
