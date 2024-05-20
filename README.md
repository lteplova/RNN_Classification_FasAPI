<h2>FastAPI сервис для классификации текста</h2>

<p>
<li>В файле app.py содержится бэкэнд часть, которая запускает модель на веб-сервере.</li>
<li>Имплементация модели в файле <code>main_model.py</code>, состояние модели - <code>model_state_dict.pt</code>.<br>
Ссылка на репозиторий с реализацией обучения модели: <a href=https://github.com/lteplova/rnn_in_nlp>https://github.com/lteplova/rnn_in_nlp</a></li>
<li>Архитектура нейронной сети <code>rnn_class.py</code>.</li>
<li>Фронтэнд часть находится в файле <code>index.html</code>, окторый запускается с методом .post в FаstApi приложении.</li>
</p>
<h4>Сервис позволяет загрузить текст в поле или(и) загрузить csv с одним или несколькими текстами.</h4>
<p>Результат работы выглядит так:</p>
  
<img width="648" alt="image" src="https://github.com/lteplova/RNN_Classification_FasAPI/assets/38242392/cb25e6ed-a096-4b2d-8645-8ea1e29c9f17">

