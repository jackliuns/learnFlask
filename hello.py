from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/url_for')
def show_url():
	return url_for('show_post', post_id='1')
#>>> @app.route('/user/<username>')
#... def profile(username): pass
#...
#>>> with app.test_request_context():
#...  print url_for('index')
#...  print url_for('login')
#...  print url_for('login', next='/')
#...  print url('profile', username='John Doe')
#...
#/
#/login
#/login?next=/
#/user/John%20Doe


"""
#使用选定的 'static' 端点就可以生成相应的 URL 。:
#url_for('static', filename='style.css')

#from flask import abort, redirect

#@app.route('/')
#def index():
#    return redirect(url_for('login'))
#@app.route('/login')
#def login():
#    abort(401)
#    this_is_never_executed()
#上例实际上是没有意义的，它让一个用户从索引页重定向到一个无法访问的页面（401 表示禁止访问）。但是上例可以说明重定向和出错跳出是如何工作的。

使用 errorhandler() 装饰器可以定制出错页面:
from flask import render_template
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

"""

if __name__ == "__main__":
	#app.debug = True
	app.run(host='0.0.0.0', debug=True)