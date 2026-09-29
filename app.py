from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  return "<h1>Hello, Render! 恭喜你成功跑通了第一个免费服务器！</h1>"


if __name__ == "__main__":
  app.run()
