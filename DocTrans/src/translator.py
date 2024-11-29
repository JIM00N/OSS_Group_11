from transformers import MarianMTModel, MarianTokenizer

def translate(text, src_lang="en", tgt_lang="es"):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translation = model.generate(**tokens)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

    return translated_text
