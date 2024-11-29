from translator import translate
from summarizer import summarize
from word_extractor import extract_frequent_words

if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog. This is a sample sentence for testing."

    # 번역 테스트
    translated = translate(text, "en", "es")
    print("Translated text:", translated)

    # 요약 테스트
    summary = summarize(text)
    print("Summary:", summary)

    # 고빈도 단어 추출 테스트
    frequent_words = extract_frequent_words(text)
    print("Frequent words:", frequent_words)
