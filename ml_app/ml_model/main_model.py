#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import torch
import torch.nn as nn
import string
import nltk
import ssl
from nltk.tokenize import word_tokenize
import pickle
import joblib
import warnings
warnings.filterwarnings("ignore")
from dataclasses import dataclass
from ml_model.rnn_class import RNN_Classiff_max

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download('punkt')

@dataclass
class Prediction:
    """Класс для вывода предсказания"""
    input_text: str
    label: str


def load_model():


    # загрузка модели, словаря и LabelEncoder для таргета
    device = 'cpu'
    model_clf = RNN_Classiff_max(hidden_dim=256, vocab_size=28633, num_classes=13, num_layers=2).to(device)
    load_model_state = torch.load('./ml_model/model_state_dict.pt', map_location=device)
    model_clf.load_state_dict(load_model_state['state_model'])

    le = joblib.load('./ml_model/le.joblib')

    with open('./ml_model/word2idx.pkl', 'rb') as f:
        word2idx = pickle.load(f)

    # функция для преобразования входного текста в эмбединг и торч тензор, применение модели, получение предсказания
    def model(input_text_: str) -> Prediction:
        processed_txt = input_text_.lower().translate(str.maketrans('', '', string.punctuation))  # препроцессинг
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


if __name__ == '__main__':
    a = load_model()
    s = a('Северные территории на границе королевства Налос давно привлекали внимание ее величества. Отправив верных рыцарей в поход на новые земли королева Гимнакс поручила вам ее доверенным картографам составить карты будущих владений. Смотрите видео правила по настольной игре Картографы Новинка Hotokenoid Картографы')
    print(s.label)

# test = '19 июня ABL разыграет 100 000 рублей и чемпионские перстни всех дивизионов В этот день мы соберемся все вместе во дворце спорта Динамо на Лавочкина чтобы определить а затем и поздравить чемпионов сезона 33 Вместе с вами мы создадим ассоциацию баскетболистов любителей чтобы развивать любительский баскетбол в России и СНГ. Богатый на эмоции день ждет не только финалистов но и самых важных людей этого сезона болельщиков. Вы сможете Посмотреть красивые финалы дивизионов от Late до Htokenoid Провести весело время на интерактивных площадках Из каждого матча мы постараемся сделать зрелищное шоу Сделаем вам кучу крутых снимков и в фотозоне и в зале и везде где сможем поймать вас в объектив Пополнить гардероб выиграть футболку с символикой ABL Выиграть баскетбольный мяч в интересных конкурсах И главное своим присутствием вы поможете команде за которую болеете выиграть 100 000 на оплату взносов следующего сезона. В розыгрыше может участвовать любая команда ABL. Проход бесплатный но нужно зарегистрироваться здесь Укажите имя телефон адрес электронной почты и команду которую Вы поддерживаете. Контакты нам нужны для отправки вам билета перед мероприятием. А команду просим указать чтобы знать какую именно поддерживает большинство и отдать ей приз 33 Это может быть ЛЮБАЯ команда планирующая участие в нашей лиге в сезоне 22 23 33 Важно 33 Все билеты будут сканироваться на входе и учитывать при подсчете мы будем болельщиков команд которые реально пришли поболеть в финале. Расписание матчей Late 12 00 Ptokenoid 13 20 Nova 14 40 Rofl 16 00 Easy 17 20 Love 18 40 Htokenoid 20 00 Если у вас занят этот день все отменяйте приходите. Обещаем будет круто 33 Встречаемся 19 июня начало мероприятия в 11 30. Будьте вместе с нами в истоках этой истории.'
# test = 'Встречаем вторую порцию оформленных карточек и помним навыки НЕ критуют hetokenoid eqtokenoid hetokenoid tokenoid'