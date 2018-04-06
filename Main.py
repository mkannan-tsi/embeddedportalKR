from flask import Flask, render_template, request, session
import requests
import string
import random

app = Flask(__name__)
app.config.update(TEMPLATES_AUTO_RELOAD = True)
app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/visualizations', methods=['GET', 'POST'])
def ShowVisualizations():
	# Retrieving the URL entered by the user 
	session['viz_url'] = request.form['inputURL']
	return render_template('thumbnails.html') 

@app.route('/viz/<int:viz>')
def ShowViz(viz):
	url=""
	# Pre-listed visualizations
	URLs = ["https://public.tableau.com/views/WorldIndicators_675/Business",
			"https://public.tableau.com/views/SalesDashboards_4/Product",
			"https://public.tableau.com/views/Regional_483/Obesity",
			"https://public.tableau.com/views/SalesDashboards_4/SalesOverview",
			"https://public.tableau.com/views/Regional_483/GlobalTemperatures"
	]
	custom_view = session['viz_url'] 
	URLs.append (custom_view[:custom_view.find("?:")])
	# Selecting the correct URL based on thumbnail selection
	for i in range(0, len(URLs)):
		if (i+1) == viz:
			url = URLs [i]
	return render_template('view.html', url=url) 

if __name__ == "__main__":
	app.run(host= '0.0.0.0', debug=True)


