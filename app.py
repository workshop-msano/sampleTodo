from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("DATABASE_URL"))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRES_URL")

db = SQLAlchemy(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(128), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods = ['POST', 'GET'])
def index():
    #post時にデータベースを更新、データベースからアイテムを取得して表示する
    if request.method == 'POST':
        todo = Todo(
            todo=request.form["todo"]
        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("index"))
    
    #get時はデータベースからアイテムを取得して表示する
    todos = db.session.execute(db.select(Todo)).all()
    return render_template('index.html', todos=todos)

# print("hello world")
# @app.route('/')
# def index():
#     return render_template('test.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
    # port = int(os.environ.get('PORT', 8080))
    # app.run(debug=True, host='0.0.0.0', port=port)
