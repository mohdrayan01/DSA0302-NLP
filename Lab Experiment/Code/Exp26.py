# 26.Implement a machine translation program using the Hugging Face Transformers library,  translate English text to French using python.

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
text = "Artificial Intelligence is transforming the world."
inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs)
translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("English :", text)
print("French  :", translation)