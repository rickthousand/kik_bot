import echo
from flask import Flask, render_template, request
import newsapi
app=Flask(__name__)

# importing requests package 

import requests      

  

def NewsFromBBC():
	query='altcoins'
	main_url=f'https://newsapi.org/v2/everything?q={query}&apiKey=4dbc17e007ab436fb66416009dfb59a8'
	open_bbc_page = requests.get(main_url).json()
	article = open_bbc_page["articles"]
	results = []
	for ar in article:
		results.append(ar["title"])
#if __name__ == '__main__': 

      

    # function call 

  #  NewsFromBBC() 



@app.route('/')
def index():
	echo.main()
	query='altcoins'
	main_url = f'https://newsapi.org/v2/everything?q={query}&apiKey=4dbc17e007ab436fb66416009dfb59a8'
	open_bbc_page=requests.get(main_url).json()
	article = open_bbc_page["articles"]
	results = []
	for ar in article:
		results.append(ar["title"])
	for i in range(len(results)):
		a=print(i + 1, results[i])
		with open("news.txt", "w") as output:
			output.write(str(results))
	return render_template('index.html', foobar=results)


@app.route('/hi')
def hi():
	return "Hi Rick Wassup Bruh"
@app.route('/result', methods=['POST', 'GET'])
def result():
	if request.method=='POST':
		query=request.form['query']
		main_url = f'https://newsapi.org/v2/everything?q={query}&apiKey=4dbc17e007ab436fb66416009dfb59a8'
		open_bbc_page = requests.get(main_url).json()
		article = open_bbc_page["articles"]
		results1 = []
		for ar in article:
			results1.append(ar["title"])
		for i in range(len(results1)):
			#a = print(i + 1, results1[i])
			with open("news.txt", "w") as output:
				output.write(str(results1))
	return render_template('result.html', foobar=results1)
	
if __name__=='__main__':
	app.run(debug=True)