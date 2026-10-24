from flask import Flask, render_template
from pathlib import Path
import webbrowser
app = Flask(__name__)
folder = Path('templates/')
total = sum(1 for item in folder.iterdir()) - 2
url = "http://127.0.0.1:5000/index/1"
@app.route('/index/<int:page>')
def index(page):
    #url_page_num = request.args.get('page',default=1,type=int)
    return render_template(f'index_{page}.html',
                           num=page,
                           title="Основы Python для начинающих",
                           h1=f"Основы Python для начинающих #{page}",
                           total = total
                           )
@app.route('/about')
def about():
    return render_template("about.html",total=total)

if __name__ == "__main__":
    webbrowser.open(url)
    app.run(debug = True)
    