import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast
import json

tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment', return_dict=True)


@torch.no_grad()
def predict(text):
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    return predicted


clusters = ["music", "politics", "science", "art", "sport", "funny", "games"]

clusters_sents = {}
for i in clusters:
    current_cluster = {'neut': 0, 'pos': 0, 'neg': 0}
    f = open(f"data/comments_{i}.txt", encoding="utf8")
    comments = f.readlines()
    for com in comments:
        a = predict(com.strip())
        if a[0] == 0:
            current_cluster['neut'] += 1
        elif a[0] == 1:
            current_cluster['pos'] += 1
        elif a[0] == 2:
            current_cluster['neg'] += 1
    clusters_sents[i] = current_cluster

f = open("sentiment_data.json", "w")
f.write(json.dumps(clusters_sents))
f.close()
