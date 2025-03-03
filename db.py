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

## creation de la table chambre 
#
# add.execute("drop table chambres") 
add.execute("""
    create table if not exists chambres(
            idChambre integer primary key autoincrement , 
            libelle varchar(20) , 
            prixCh decimal(7,2) , 
            devise char(3) default 'usd',
            image text ,
            idAdmin integer , 
            foreign key(idAdmin) references users(idUser)) 
""")

#
#
# reservation 


add.execute("""
            create table if not exists reservations(
            idR integer primary key autoincrement ,
            dateE date , 
            clientID integer ,
            chambreID integer ,
           
            nombrePer varchar(100), 
            sejour varchar(30) , 
            statut varchar(3) default 'non', 
            foreign key(clientID) references users(idUser) , 
            foreign key(chambreID) references chambres(idChambre))
            """)
add.commit()