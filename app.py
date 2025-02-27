from flask import Flask , render_template , session, redirect,request ,url_for
import sqlite3


app = Flask(__name__)
app.secret_key = "deployOnrenderMukoko"

@app.route('/',methods =['GET','POST'])
@app.route('/login',methods =['GET','POST'])
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)