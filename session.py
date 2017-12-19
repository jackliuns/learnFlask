from flask import Flask, session, redirect, url_for, escape, request


#关于响应
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

#可以使用 make_response() 包裹返回表达式，获得响应对象，并对该对象 进行修改，然后再返回：

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


"""
会话
除了请求对象之外还有一种称为 session 的对象，允许你在不同请求 之间储存信息。这个对象相当于用密钥签名加密的 cookie ，
即用户可以查看你的 cookie ，但是如果没有密钥就无法修改它。
使用会话之前你必须设置一个密钥。
"""

app = Flask(__name__)

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	return '''
		<from action="" method="post">
			<p><input type=text name=username>
			<p><input type=submit value=Login>
		</from>
	'''

@app.route('/logout')
def logout():
	#如果会话中有用户名就删除它。
	session.pop('username', None)
	return redirect(url_for('index'))

app.secret_key = '\xd7W\xa5\xd6\x18\x05\xde\xd3\xec\xff\xd6(J\x80Q\xf2'  #os.urandom(16)随机生成种子
