import sqlite3 


add = sqlite3.connect("hotel.db")
#add.execute('drop table users')
#creation de la table users
add.execute("""
    create table if not exists users(
            idUser integer primary key autoincrement, 
            username varchar(30), 
            emailUser varchar(30), 
            phoneUser varchar(15), 
            role varchar(20) default 'client', 
            passwordUser varchar(20),
            dateCreate timestamp default current_timestamp)
""")

# information par defaut 
#add.execute("insert into users(username,emailUser,phoneUser,role,passwordUser) values('hotel','hotel@gmail.com','982484573','admin','hotel')")


add.commit()