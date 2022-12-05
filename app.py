from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        result = request.form
        #データを投稿したらデータベースを更新、データベースからアイテムを取得して表示する
        return render_template("index.html", result = result)
    
    return render_template('index.html', 
        #データベースからアイテムを取得して表示する
    )


if __name__ == '__main__':
    app.run(debug=True, port=8000)
