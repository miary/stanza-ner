from transformers import pipeline
gen = pipeline("token-classification", "lakshyakh93/deberta_finetuned_pii")

text = "My name is Alma Demarco and I live in 302 Bloom St., claremont, CA 92798."
#text = "302 Bloom St., claremont, CA 92798"
#text = "380-09-4528"
output = gen(text, aggregation_strategy="first") # simple
#print(output[0]['entity_group'])
print(output)
