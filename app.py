from flask import Flask

app = Flask(__name__)


# @app.route('/')  使用app.route装饰器注册视图函数
def hello_world():
    return '<h1>Hello MMY!</h1>'


app.add_url_rule('/', 'hello_world', hello_world)  # 使用app.add_url_rule()方法 3个参数：URL、端点名和视图函数


# 动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)


if __name__ == '__main__':
    app.run()

