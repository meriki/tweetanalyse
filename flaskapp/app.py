from flask import Flask,url_for,render_template
# import matplotlib.pyplot as plt
# import plotly.plotly as py
app=Flask(__name__)



@app.route('/')
@app.route('/home')
def home_page():
	return render_template('start.html')
	# print url_for('newpage',name='ramya')
@app.route('/election', methods=['GET','POST'])
def election():
	return render_template('polls.html')

# def original_retweet():
# 	y=[3685,6788]
# 	x=['original tweets','retweeted tweets']
# 	plt.bar(x,y,3,color="blue")
# 	fig=plt.gcf()
# 	plot_url=py.plot_mpl(fig,filename='mpl-basic-bar')
# @app.route('/new/<name>')
# def newpage(name):
# 	return name
