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

#使用选定的 'static' 端点就可以生成相应的 URL 。:
#url_for('static', filename='style.css')

if __name__ == "__main__":
	#app.debug = True
	app.run(host='0.0.0.0', debug=True)