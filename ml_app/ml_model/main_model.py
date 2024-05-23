#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import torch
import string
import nltk
from nltk.tokenize import word_tokenize
import pickle
import joblib
import warnings
warnings.filterwarnings("ignore")
from dataclasses import dataclass
from ml_model.rnn_class import RNN_Classiff_max
import pymorphy3

@dataclass
class Prediction:
    """Класс для вывода предсказания"""
    input_text: str
    label: str
def load_model():
    with open('./ml_model/word2idx.pkl', 'rb') as f:
        word2idx = pickle.load(f)
    # загрузка модели, словаря и LabelEncoder для таргета
    device = 'cpu'
    model_clf = RNN_Classiff_max(hidden_dim=512, vocab_size = len(word2idx), num_classes=13, num_layers=2).to(device)
    load_model_state = torch.load('./ml_model/model_state_dict.pt', map_location=device) # эта модель работает с точностью 84.5%
    model_clf.load_state_dict(load_model_state)
    le = joblib.load('./ml_model/le.joblib')
    morph = pymorphy3.MorphAnalyzer()


    # функция для преобразования входного текста в эмбединг и торч тензор, применение модели, получение предсказания
    def model(input_text_: str) -> Prediction:
        input = " ".join([morph.parse(w)[0].normal_form for w in input_text_.lower().split()])
        processed_txt = input.lower().translate(str.maketrans('', '', string.punctuation))  # препроцессинг
        tags = ['<unk>', '<bos>', '<eos>', '<pad>']
        unk_id, bos_id, eos_id, pad_id = [word2idx[tag] for tag in tags]  # тэги
        tok_sent = [word2idx.get(word, unk_id) for word in word_tokenize(processed_txt)]  # токенизация
        tok_sent.insert(0, bos_id)
        tok_sent.insert(-1, eos_id)
        max_len = 256
        max_seq_len = min(len(tok_sent), max_len)
        seq = tok_sent[:max_seq_len]
        for _ in range(max_len - len(tok_sent)):
            seq.append(pad_id)
        seqs = torch.LongTensor(seq)  # преобразование в тензор
        seqs = seqs.reshape(1, 256).to(device)
        model_clf.eval()  # перевод модели в режим применения
        logits = model_clf(seqs)  # вычисление предсказания
        predictions = logits.argmax(dim=1)
        label_ = le.inverse_transform([predictions.item()])[0]

        return Prediction(input_text=input_text_, label=str(label_))

    return model

# тестирование
if __name__ == '__main__':
    test_model = load_model()
    test_predict = test_model('Северные территории на границе королевства Налос давно привлекали внимание ее величества. Отправив верных рыцарей в поход на новые земли королева Гимнакс поручила вам ее доверенным картографам составить карты будущих владений. Смотрите видео правила по настольной игре Картографы Новинка Hotokenoid Картографы')
    print(test_predict.label)
