from collections import Counter
import re

def extract_frequent_words(text):
    words = re.findall(r'\w+', text.lower())  # 소문자로 변환 후 단어 추출
    word_counts = Counter(words)
    return word_counts.most_common(5)  # 상위 5개의 고빈도 단어 반환
