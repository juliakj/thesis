from flask import Flask
from flaskext.mysql import MySQL
import sys
sys.path.insert(0, '/home/ubuntu/mygit/query_code/')
import get_providers, process_query
import pickle
from flask import request
from flask import render_template

app = Flask(__name__)
#app.debug = True
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Galdorhavens0!'
app.config['MYSQL_DATABASE_DB'] = 'db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def home():
  return render_template("home.html", results=[])


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    state = request.form['state']
    a = get_providers.get([text, state])
    l = a[5:]
    return render_template("home.html", results=l)





#  conn = mysql.connect()
 # cursor = conn.cursor()
 # cursor.execute("SELECT * from violations")
  
  #data = cursor.fetchall()[0]
#  data = process_query.process('pap smear') #get_providers.get(['pap smear', 'KY'])
  #map = pickle.load(open('fullSpecialtiesMap.p', 'rb'))

 # return str(data)


if __name__ == '__main__':
  app.run()

