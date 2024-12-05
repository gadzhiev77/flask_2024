from flask import Flask, render_template

app = Flask(__name__)
# @app.route('/<float:number>/')
# def index(number):
#     result = number * 2
#     text = f'Ваше число {number}, умноженное на 2: {number * 2}'
#     return render_template('index.html', number=result, text=text)
#



@app.route('/<float:number>')
def index(number):
    return render_template('index.html', text=f'Ваше число {number}, умноженное на 2: {number * 2}')


if __name__ == '__main__':
    app.run()
