<h2>FastAPI сервис для классификации текста</h2>
<p>Сервис выполняет применение и отображение результатов работы <code>RNN(LSTM)</code> модели на некотором входном кусочке текста.</p>
<p>Входные данные: текст или таблица, которая подается на вход в виде csv-файла.</p>
<hr>
<p>Модель обучалась на данных с соревнования VK CUP 2022 ссылка на kaggle <a href="https://www.kaggle.com/datasets/mikhailma/russian-social-media-text-classification/data">Russian Social Media Text Classification.</a></p>
<p>Ссылка на репозиторий с реализацией обучения модели: <a href=https://github.com/lteplova/rnn_in_nlp>https://github.com/lteplova/rnn_in_nlp</a></p>
<hr>
<p>
<li>В файле <code>ml_app/app.py</code> содержится бэкэнд часть, которая запускает модель на веб-сервере.</li>
<li>Имплементация модели в файле <code>ml_app/ml_model/main_model.py</code>, состояние модели - <code>model_state_dict.pt</code>.<br>
</li>
<li>Архитектура нейронной сети <code>ml_app/ml_model/rnn_class.py</code>.</li>
<li>Фронтэнд часть находится в файле <code>ml_app/public/index.html</code>, который запускается методом .post в FаstAPI приложении.</li>
</p>
<hr>
Реализация выполнена с применением:<code>FastAPI/PyTorch/Html/JavaScript</code>
<hr>
<h4>Сервис позволяет добавить текст в поле или/и загрузить csv с одним или несколькими текстами.</h4>
<p>Результат работы выглядит так:</p>
 
<img width="648" alt="image" src="https://github.com/lteplova/RNN_Classification_FasAPI/assets/38242392/cb25e6ed-a096-4b2d-8645-8ea1e29c9f17">

