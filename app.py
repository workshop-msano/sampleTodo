from flask import Flask

app = Flask(__name__)
print("hello world"); 

if __name__ == '__main__':
    app.run(debug=True, port=8000)
