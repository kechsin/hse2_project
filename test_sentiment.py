import torch
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment', return_dict=True)


@torch.no_grad()
def predict(text):
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    return predicted


a = predict("Редакция Наука, но на роль корреспондентки взяли дурочку, не способную вспомнить даже базовую анатомию человека? Нет, блин, никакой тазобедренной кости, есть тазовая и бедренная кости, а вот СУСТАВ тазобедренный. Зато 20 минут рекламы есть, ух, НАУЧНО! Твою налево, вы бы хоть проверяли, что мелете")
print(a)
