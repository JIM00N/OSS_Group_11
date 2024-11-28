from translate import translate_text
from summarize import summarize_text
from keywords import extract_keywords

def process_document(file_path: str, src_lang: str, tgt_lang: str):
    with open(file_path, 'r') as file:
        document = file.read()
    
    # 번역
    translated_text = translate_text(document, src_lang, tgt_lang)
    print(f"Translated Text:\n{translated_text}\n")
    
    # 요약
    summary = summarize_text(document)
    print(f"Summary:\n{summary}\n")
    
    # 키워드 추출
    keywords = extract_keywords(document)
    print(f"Keywords: {', '.join(keywords)}")

if __name__ == "__main__":
    process_document("docs/document.txt", "en", "es")
