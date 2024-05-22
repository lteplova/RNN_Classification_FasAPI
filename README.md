<h2>FastAPI сервис для классификации текста</h2>
<h3>Задача:</h3>
<p>Создание сервиса, который выполняет применение и отображение результатов работы <code>RNN(LSTM)</code> модели на некотором входном кусочке текста.</p>
<p>Входные данные: текст или таблица, которая подается в виде csv-файла.</p>
<hr>
<h3>Данные:</h3>
<p>Модель обучалась на данных с соревнования VK CUP 2022 ссылка на kaggle <a href="https://www.kaggle.com/datasets/mikhailma/russian-social-media-text-classification/data">Russian Social Media Text Classification.</a>
<p>Датасет содержит тексты из спортивных сообществ социальной сети ВКонтакте, 13 подкатегорий тем:</p>
<i>(athletics, autosport, basketball, boardgames, esport, extreme, football, hockey, martial_arts, motosport, tennis, volleyball, winter_sport)</i>
</p>

<p>Ссылка на репозиторий с реализацией обучения модели: <a href=https://github.com/lteplova/rnn_in_nlp>https://github.com/lteplova/rnn_in_nlp</a></p>
<hr>
<h3>Решение:</h3>
<p>
Сервис доступен по ссылке: <a href="http://185.22.61.118:8000/">http://185.22.61.118:8000/</a>
<li>В файле <code>ml_app/app.py</code> содержится бэкэнд часть, которая запускает модель на веб-сервере.</li>
<li>Имплементация модели в файле <code>ml_app/ml_model/main_model.py</code>, состояние модели - <a href = "https://drive.google.com/file/d/1SECK0p2jrfBuhSRl4_o_BmH5eLcsSGY3/view?usp=drive_link">model_state_dict.pt</a>.<br>
</li>
<li>Архитектура нейронной сети <code>ml_app/ml_model/rnn_class.py</code>.</li>
<li>Фронтэнд часть находится в файле <code>ml_app/public/index.html</code>, который запускается методом .post в FаstAPI приложении.</li>
<p>запуск сервиса осуществляется строкой <code>uvicorn app:app --host 0.0.0.0 --port 8000</code></p>
</p>
<hr>
<h3>Используемые технологии:</h3>
Реализация выполнена с применением:<code>FastAPI&#183;PyTorch&#183;Html&#183;JavaScript</code>
<hr>
<h3>Сервис позволяет добавить текст в поле или/и загрузить csv с одним или несколькими текстами.</h3>
<p>Результат работы сервиса:</p>
 
<img width="648" alt="image" src="https://github.com/lteplova/RNN_Classification_FasAPI/assets/38242392/cb25e6ed-a096-4b2d-8645-8ea1e29c9f17">

