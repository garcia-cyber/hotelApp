from flask import Flask , render_template , session, redirect,request ,url_for, flash
import sqlite3


app = Flask(__name__)
app.secret_key = "deployOnrenderMukoko"

@app.route('/',methods =['GET','POST'])
@app.route('/login',methods =['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['user'] 
        pwd  = request.form['pwd'] 

        #connexion avec la base de donnee
        with sqlite3.connect("hotel.db") as con:
            cur = con.cursor()
            cur.execute("select * from users where username = ? or emailUser = ? and passwordUser = ?", [user, user,pwd]) 
            read = cur.fetchone()

            if read:
                session['hotel'] = True 
                session['id']    = read[0]
                session['name']  = read[1]
                session['email'] = read[2]

                return redirect('/admin')
            else:
                flash("acces errone")
    return render_template('login.html')

#admin page 
@app.route("/admin")
def admin():
    if 'hotel' in session :
        return render_template('index.html')
    else:
        return redirect('/')
    
## deconnexion 
#
@app.route('/deco')
def deco():
    session.clear()

    return redirect('/')

#create compte 
#
@app.route("/register", methods = ['POST','GET']) 
def register():
    if request.method == 'POST':
        name  = request.form['name'] 
        email = request.form['email']
        phone = str(request.form['phone']) 
        pwd   = request.form['pwd']
        pwd2  = request.form['pwd2'] 

         
        with sqlite3.connect('hotel.db') as con :

            #verification du phone existant
            cur = con.cursor()
            cur.execute("select * from users where phoneUser = ?", [phone]) 
            d = cur.fetchone() 

            
            if d:
                flash("le numero de telephone existe deja")
            #verification du mot de passe 
            # 
            elif pwd == pwd2:
                
                add = con.cursor()
                add.execute("insert into users(username,emailUser,phoneUser,passwordUser) values(?,?,?,?)",[name,email,phone,pwd])
                con.commit()
                return redirect('/')
            else:
                pass    

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)