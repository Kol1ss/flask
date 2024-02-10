from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def noole():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    prom_text = ["Человечество вырастает из детства.",
                 ' ',
                 "Человечеству мала одна планета.",
                 '',
                 "Мы сделаем обитаемыми безжизненные пока планеты.",
                 ' ', "И начнем с Марса!",
                 '',
                 "Присоединяйся!"]
    return '</br>'.join(prom_text)


@app.route('/image_mars')
def image_mars():
    return f'''<img src="{url_for('static', filename='bkg82iooampgcbiuqsfi.jpg')}"
           alt="здесь должна была быть картинка, но она не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
