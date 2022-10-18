from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', row=8, col=8, color_1="red", color_2="black")


@app.route('/<int:num1>/<int:num2>')
def row_col(num1, num2):
    return render_template('index.html', row=num1, col=num2, color_1="red", color_2="black")


@app.route('/<int:num1>/<int:num2>/<string:color_1>/<string:color_2>')
def row_col_color(num1, num2, color_1, color_2):
    return render_template('index.html', row=num1, col=num2, color_1=color_1, color_2=color_2)


if __name__ == "__main__":
    app.run(debug=True)
