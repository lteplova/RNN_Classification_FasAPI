<h2>FastAPI сервис для классификации текста</h2>
<p>
<li>В файле app.py содержится бэкэнд часть, которая запускает модель на веб-сервере.</li>
<li>Имплементация модели в файле main_model.py, состояние модели - model_state_dict.pt.<br>
Ссылка на репозиторий с реализацией обучения модели: <a href=https://github.com/lteplova/rnn_in_nlp/tree/main>https://github.com/lteplova/rnn_in_nlp/tree/main</a></li>
<li>Архитектура нейронной сети rnn_class.py.</li>
<li>Фронтэнд часть находится в файле index.html, окторый запускается с методом .post в FаstApi приложении.</li>
</p>
<h4>Сервис позволяет загрузить текст в поле или(и) загрузить csv с одним или несколькими текстами.</h4>
<p>Результат работы выглядит так:</p>
  
<img width="642" alt="image" src="https://github.com/lteplova/RNN_Classification_FasAPI/assets/38242392/1a848795-6e64-4f55-b375-dfa2704c67fb">
