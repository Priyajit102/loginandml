
from flask import Flask,render_template,url_for,request,redirect,session
import mysql.connector
import pickle
import os
app = Flask(__name__)
app.secret_key=os.urandom(24)
conn=mysql.connector.connect(host='remotemysql.com',user="b5l0CiGJb2",password="FShP3SWVKl",database="b5l0CiGJb2")
cursor=conn.cursor()
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('index.html')
    else:
        return redirect('/')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')


    cursor.execute("""SELECT * FROM `user` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(email,password))
    user=cursor.fetchall()
    if len(user)>0:
        session['user_id']=user[0][0]
        email1 = request.form['email']
        return render_template('index.html',email=email1)
    else:
        return redirect('/')

@app.route('/add_user',methods=['GET','POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cursor.execute("""INSERT INTO `user` (`name`,`email`,`password`) VALUES('{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return redirect('/')

reg = pickle.load(open('mlmodel.pkl', 'rb'))
@app.route('/predict', methods=['POST'])
def predict():
    milage = int(request.form.get('milage'))
    age = int(request.form.get('age'))
    carnl = request.form.get('car')

    car = list(carnl)
    int_car = [int(x) for x in car]
    car = int_car

    feature_list = [[milage, age] + car]

    prediction = reg.predict(feature_list)

    output = round(prediction[0], 2)

    return render_template('index.html', pretxt="The value on that year is Rs.{}".format(output))

@app.route('/dropsession')
def dropsession():
    session.pop('user_id',None)
    return render_template('login.html')

if __name__=="__main__":
    app.run(debug=True)

