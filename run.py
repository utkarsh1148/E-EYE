
import sys
from flask import *
import pymongo
from flask_pymongo import PyMongo



app=Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)



@app.route('/',methods=['GET','POST'])
def home():   
    return render_template("facedetection.html")


@app.route('/managefaces.html',methods=['GET','POST'])
def manage():   
    return render_template("managefaces.html")


@app.route('/home.html',methods=['GET','POST'])
def basic():   
    return render_template("home.html")

@app.route('/team.html',methods=['GET','POST'])
def team():   
    return render_template("team.html")

@app.route('/FinalDocumentation.html',methods=['GET','POST'])
def doc():   
    return render_template("Final Documentation.html")

@app.route('/signup.html',methods=['GET','POST'])
def signup():
    flag=0
    if request.method=="POST":
        
        username=request.form['username']
        password=request.form['password']
        
        data={'Username':username,
              'Password':password}
        mongo.db.EEYE_SIgnup.insert_one(data)
        flag=1
        return redirect(url_for('signin'))
    if (flag!=1):
        return render_template("signup.html")


@app.route('/signin.html',methods=['GET','POST'])
def signin():
    flag=0
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        
        data={'Username':username,'Password':password}
        status=mongo.db.EEYE_SIgnup.find_one(data)
        if (status!=None):
            flag=1
            return redirect(url_for('basic'))
    if(flag!=1):
        return render_template("signin.html")

if __name__=='__main__':
    app.run(debug=True)
