import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text: str, top_n: int = 10) -> list:
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
    
    word_counts = Counter(filtered_words)
    common_keywords = word_counts.most_common(top_n)
    
    return [keyword[0] for keyword in common_keywords]
