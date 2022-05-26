number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
small_Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital_Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


import os
from flask import Flask, current_app, jsonify, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql.cursors
from wtforms import SelectField
from flask_wtf import FlaskForm
from flaskext.mysql import MySQL
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kalide1:12345@localhost/studentdb'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'studentdb'
app.config['MYSQL_DATABASE_USER'] = 'kalide1'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'


mysql = MySQL(app, cursorclass=pymysql.cursors.DictCursor)

db = SQLAlchemy(app)

class State(db.Model):
    __tablename__ = 'state'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

class Local(db.Model):
    __tablename__ = 'local'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    state_id = db.Column(db.Integer)
    state_name_id = db.Column(db.String(55))

class Form(FlaskForm):
    state = SelectField('state', choices=[])
    local = SelectField('local', choices=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students/portal')
def portal_form():
    form = Form()
    form.state.choices = [(state.name, state.name) for state in State.query.all()]
    return render_template('portal.html', form=form)

@app.route('/local/<get_local>')
def localbystate(get_local):
    local = Local.query.filter_by(state_name_id=get_local).all()
    localArray = []
    for each in local:
        localObj = {}
        localObj['id'] = each.id
        localObj['name'] = each.name
        localArray.append(localObj)
    return jsonify({'statelocal' : localArray})

@app.route('/admin/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        query_name = request.form['queryname']
        by_admission_status = request.form['by_admission_status']
        by_gender = request.form['by_gender']
        by_jambscore = request.form['by_jambscore']
        if query_name == "":
            if by_jambscore == "":
                if by_admission_status == "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    # cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and jambscore = %s', ())
                    cur.execute('select * from students')
                    rv = cur.fetchall()
                elif by_admission_status == "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where gender = %s', (by_gender))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where admis_status = %s', (by_admission_status))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where admis_status = %s and gender = %s', (by_admission_status, by_gender))
                    rv = cur.fetchall()
            elif by_jambscore != "":
                if by_admission_status == "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    # cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and jambscore = %s', ())
                    cur.execute('select * from students where jambscore = %s', (by_jambscore))
                    rv = cur.fetchall()
                elif by_admission_status == "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where gender = %s and jambscore = %s', (by_gender, by_jambscore))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where admis_status = %s and jambsore = %s', (by_admission_status, by_jambscore))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where admis_status = %s and gender = %s and jambscore = %s', (by_admission_status, by_gender, by_jambscore))
                    rv = cur.fetchall()
        elif query_name != "":
            if by_jambscore == "":
                if by_admission_status == "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where firstname like %s or lastname like %s or middlename like %s', (query_name, query_name, query_name))
                    # cur.execute('select * from students where ')
                    rv = cur.fetchall()
                elif by_admission_status == "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and gender = %s', (query_name, query_name, query_name, by_gender))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and admis_status = %s', (query_name, query_name, query_name, by_admission_status))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and admis_status = %s and gender = %s', (query_name, query_name, query_name, by_admission_status, by_gender))
                    rv = cur.fetchall()
            elif by_jambscore != "":
                if by_admission_status == "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    # cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and jambscore = %s', ())
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and jambscore = %s', (query_name, query_name, query_name, by_jambscore))
                    rv = cur.fetchall()
                elif by_admission_status == "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and gender = %s and jambscore = %s', (query_name, query_name, query_name, by_gender, by_jambscore))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender == "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and admis_status = %s and jambsore = %s', (query_name, query_name, query_name, by_admission_status, by_jambscore))
                    rv = cur.fetchall()
                elif by_admission_status != "none" and by_gender != "none":
                    conn = mysql.get_db()
                    cur = conn.cursor()
                    cur.execute('select * from students where (firstname like %s or lastname like %s or middlename like %s) and admis_status = %s and gender = %s and jambscore = %s', (query_name, query_name, query_name, by_admission_status, by_gender, by_jambscore))
                    rv = cur.fetchall()
    else:
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select * from students')
        rv = cur.fetchall()
        # return render_template('dashboard.html', students=rv)

    if len(rv) > 0:
        user_response = rv
    return render_template('dashboard.html', students=rv)


@app.route('/student', methods=['POST'])
def add_student():
    nameArray = []
    for i in range(1, 4):
        nameArray.append(random.choice(capital_Letters))
        nameArray.append(random.choice(small_Letters))
        nameArray.append(random.choice(number_list))
    print(nameArray)
    random.shuffle(nameArray)
    print(nameArray)

    nameString = ""
    nameArray2 = []
    for char in nameArray:
        nameArray2.append(char)
        nameString += char
    # nameString += ".png"
    nameString += "0"
    print(nameString)

    dir  = os.path.join(current_app.root_path, f'static/images/{nameString}')
    if not os.path.exists(dir):
        os.mkdir(dir)
    req = request.get_json()
    firstname = req['firstname']
    lastname = req['lastname']
    dateofbirth = req['dateofbirth']
    phonenumber = req['phonenumber']
    state = req['state']
    gender = req['gender']
    nextofkin = req['nextofkin']
    middlename = req['middlename']
    emailaddress = req['emailaddress']
    address = req['address']
    local = req['local']
    jambscore = req['jambscore']
    admis_status = req['admis_status']
    if firstname == '' or lastname == '' or dateofbirth == '' or phonenumber == '' or state == '' or nextofkin == '' or middlename == '' or emailaddress == '' or address == '' or local == '' or jambscore == '':
        flash('Please fill in all fields, to add a new word', 'flash_error')
    else:
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('insert into students(firstname, lastname, middlename, dateofbirth, phonenumber, state, gender, nextofkin, emailaddress, address, local, jambscore, admis_status, img_string) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (firstname, lastname, middlename, dateofbirth, phonenumber, state, gender, nextofkin, emailaddress, address, local, jambscore, admis_status, nameString))
        conn.commit()
        cur.close()

    return json.dumps('success')

@app.route('/admin/students/<id>')
def get_student(id):
    conn = mysql.get_db()
    cur = conn.cursor()
    cur.execute('select * from students where id = %s', (id))
    rv = cur.fetchall()
    print(rv)
    origi_id = rv[0]['img_string']
    filepath = os.path.join(current_app.root_path, 'static/images/' + origi_id + '/image.png')
    if os.path.exists(filepath):
        displayVal = 1
    else:
        displayVal = 0

    return render_template('student.html', student_information=rv, displayVal=displayVal)

@app.route('/updateadmisstatus', methods=['POST'])
def update_admis_status():
    req = request.get_json()
    admis_status = req['admis_status']
    student_id = req['student_id']
    
    conn = mysql.get_db()
    cur = conn.cursor()
    cur.execute('update students set admis_status = %s where id = %s', (admis_status, student_id))
    conn.commit()
    cur.close()

    return json.dumps('success')

@app.route('/student/addprofileimg', methods=['POST'])
def addprofileImg():
    image = request.files['file']
    student_id = request.form['student_id']
    
    if image:
        conn = mysql.get_db()
        cur = conn.cursor()
        cur.execute('select img_string from students where id = %s', (student_id))
        rv = cur.fetchall()
        origi_id = rv[0]['img_string']
        print(origi_id)
        origi_id_str = str(origi_id)
        filepath = os.path.join(current_app.root_path, 'static/images/' + origi_id_str + '/image.png')
        image.save(filepath)
    else:
        print('There is no image.')

    
    return render_template('student.html')


if __name__ == "__main__":
    app.run(debug=True, port=5051)