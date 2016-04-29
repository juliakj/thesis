from flask import Flask
from flaskext.mysql import MySQL
import sys
sys.path.insert(0, '/home/ubuntu/mygit/query_code/')
import get_providers, process_query, revised, revised2
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
    conn = mysql.connect()
    cursor = conn.cursor()
    a = revised2.get([text, state], cursor)

    return render_template("home.html", results=a)


@app.route("/npi/<npi>")
def provider(npi):
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute("SELECT * from providers where npi=" + str(npi))
  personal = cursor.fetchall()[0]
  cursor.execute("SELECT * from locations where npi=" + str(npi))

  location = cursor.fetchall()[0]


  cursor.execute("SELECT * from violations where npi=" + str(npi))

  violations = cursor.fetchall()

  cursor.execute("SELECT descrip, submitted_charge from services where npi=" + str(npi) + " limit 5")
  services = cursor.fetchall()

  if personal[3] != "":
    name = personal[2] + " " + personal[3] + ". " + personal[1]
  else:
    name = personal[2] + " " + personal[1]
  
  specialty = personal[6]
  cred = personal[4]
  gender = personal[5]
  if personal[7] == "Y":
    medicare = "Yes"
  else:
    medicare = "No"

  if personal[8] == "OTHER" or personal[8] == "":
    school = "UNKNOWN"
  else:
    school = personal[8]
  
  if personal[9] == 0 or personal[9] == "":
    year = "UNKNOWN"
  else:
    year = personal[9]

  address = str(location[2]) + ", " + str(location[3]) + ", " + str(location[5]) + "\n" + str(location[4])
  



  return render_template("npi.html", name=name, specialty=specialty, gender=gender, cred=cred, medicare=medicare, school=school, year=year, address=address, violations=violations, services=services)
  #return str(personal)






if __name__ == '__main__':
  app.run()

