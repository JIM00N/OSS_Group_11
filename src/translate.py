from transformers import MarianMTModel, MarianTokenizer

def translate_text(text: str, src_lang: str, tgt_lang: str) -> str:
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    return translated_text