from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  return "<h1>Hello, World! 这是我修改后的新页面！</h1>"


if __name__ == "__main__":
  app.run()
