from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
from pydantic import BaseModel
from ml_model.main_model import load_model

model = None
app = FastAPI()

class SentimentResponse(BaseModel):
    sentiment_text: str
    sentiment_label: str

# загрузка корневой страницы
@app.get("/")
def root():
    return FileResponse("public/index.html")

# старт модели при старте приложения
@app.on_event("startup")
def startup_event():
    global model
    model = load_model()

# функция для вычисления предсказания
@app.get("/predict")
def predict_sentiment(text: str):
    sentiment = model(text)
    response = SentimentResponse(
        sentiment_text = sentiment.input_text,
        sentiment_label = sentiment.label,
    )

    return response
# отправка данных на сервер и вычисление результата с его выдачей
@app.post("/result")
def result(data = Body()):
    txt = data["text"]
    file = data["file"]

    if len(txt):
        res_txt = predict_sentiment(txt)
        return {"message": f"<h3>Предсказанная категория для текстового поля:</h3><strong>Категория:</strong>  {res_txt.sentiment_label}<br><strong>Текст:</strong>  {res_txt.sentiment_text}<br>"}

    if len(file):
        lines = file.split('\n')
        res_file = {}
        result = []
        for i, line in enumerate(lines):
            if len(line):
                res_file[i] = predict_sentiment(line)
                predict = f"<strong>Категория:</strong>  {res_file[i].sentiment_label}<br><strong>Текст:</strong>  {res_file[i].sentiment_text}<br><br>"
                result.append(predict)
        result = str(result).replace(',', '').replace('[', '').replace(']', '').replace('\'', '')

        return {"message": f"<h3>Предсказания для csv файла:</h3> {result} <br>"}