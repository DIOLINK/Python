import datetime
import os

import pymysql
from dotenv import load_dotenv

load_dotenv()


class DataBase:
    def __init__(self):
        self.TABLE_ATRACCTIONS = "CREATE TABLE atracciones ( id INTEGER PRIMARY KEY NOT NULL,nombre VARCHAR(255),costo INT, durasion DECIMAL(10, 2), cupo INT,tipo VARCHAR(255))"
        self.TABLE_PROMOTIONS = "CREATE TABLE promociones (id INTEGER PRIMARY KEY NOT NULL,tipo VARCHR(255),nombre_promo VARCHAR(255),categoria VARCHAR(255),atraccion_1 VARCHAR(255), atraccion_2 NULL VARCHAR(255),atraccion_n NULL VARCHAR(255),descuento INT)"
        self.TABLE_USERS = "CREATE TABLE usuarios (id INTEGER PRIMARY KEY NOT NULL,nombre_apellido VARCHAR(255),categoria VARCHAR(255),presypuesto INT, tiempo_disponible DECIMAL(10, 2))"
        self.TABLE_AUTH = "CREATE TABLE auth (id int NOT NULL AUTO_INCREMENT, user_id int DEFAULT NULL, email varchar(45) NOT NULL,pass varchar(255) NOT NULL,isAdmin tinyint NOT NULL DEFAULT '0',isDelete tinyint NOT NULL DEFAULT '0',PRIMARY KEY (id), UNIQUE KEY email_UNIQUE (email),UNIQUE KEY user_id_UNIQUE (user_id),CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES usuarios (id) ON DELETE RESTRICT ON UPDATE CASCADE) ENGINE = InnoDB AUTO_INCREMENT = 6 DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci"
        self.TABLE_USERS_PROMOTIONS = "CREATE TABLE users_promotions (id INTEGER PRIMARY KEY NOT NULL,id_user INT,id_promotion INT,FOREIGN KEY (id_user) REFERENCES usuarios(id), FOREIGN KEY (id_promotion) REFERENCES Promotion(id));"
        self.INSERT_TABLE_USERS = 'INSERT INTO usuarios VALUES(1,"Harry","AVENTURA",10,8.0),(2,"Hermione","PAISAJES",100,6.0),(3,"Ron","DEGUSTACION",36,8.0),(4,"Dumbledore","PAISAJES",10,8.0),(5,"Hagrid","AVENTURA",100,24.0)'
        self.INSERT_TABLE_ATRACCTIONS = 'INSERT INTO atracciones VALUES(1,"Hogwarts",10,2,6,"AVENTURA"),(2,"Gringots",5,2,25,"PAISAJE"),(3,"Callejon diagon",3,6.5,150,"DEGUSTACION"),(4,"Caldero Chorreante",25,2,15,"AVENTURA"),(5,"Valle de Godric",5,2,15,"PAISAJE"),(6,"Ollivanders",35,1,30,"DEGUSTACION"),(7,"Hogsmeade",12,3,32,"PAISAJE"),(8,"Anden nueve y tres cuartos",3,4,12,"AVENTURA"),(9,"Azkaban",15,4,6,"AVENTURA"),(10,"Ministerio de Magia",28,5,25,"DEGUSTACION"),(11,"Emporio de la Lechuza",30,9,15,"PAISAJE"),(12,"Mansion Malfoy",8,3,15,"DEGUSTACION"),(13,"Bosque Prohibido",17,8.5,12,"PAISAJE")'
        self.INSERT_TABLE_PROMOTIONS = 'INSERT INTO promociones VALUES(1,"Por","PACK AVENTURA","AVENTURA","Anden nueve y tres cuartos","Caldero Chorreante",NULL,20),(2,"Abs","PACK DEGUSTACION","DEGUSTACION","Ollivanders","Callejon diagon",NULL,36),(3,"AxB","PACK TRIPLE PAISAJE","PAISAJE","Gringots","Valle de Godric","Hogsmeade",100),(4,"Por","PACK DOBLE AVENTURA","AVENTURA","Hogwarts","Caldero Chorreante",NULL,10),(5,"Abs","PACK DOBLE PAISAJE","PAISAJE","Hogsmeade","Gringots",NULL,15),(6,"AxB","PACK TRIPLE AVENTURA","AVENTURA","Hogwarts","Caldero Chorreante","Anden nueve y tres cuartos",100),(7,"Por","PACK SIMPLE DEGUSTACION","DEGUSTACION","Callejon diagon",NULL,NULL,15),(8,"Abs","PACK SIMPLE AVENTURA","AVENTURA","Caldero Chorreante",NULL,NULL,20),(9,"AxB","PACK 2X1 DE PAISAJE","PAISAJE","Hogsmeade","Valle de Godric",NULL,100),(10,"Abs","PACK LO MEJOR EN PAISAJE","PAISAJE","Emporio de la Lechuza","Bosque Prohibido",NULL,43),(11,"AxB","PACK 2X1 DEGUSTACION","DEGUSTACION","Ministerio de Magia","Mansion Malfoy",NULL,100)'

    def conectar(self):
        self.connection = pymysql.connect(host=os.getenv('MYSQL_HOST'), user=os.getenv('MYSQL_USER'), password=os.getenv('MYSQL_PASSWORD'), db=os.getenv('MYSQL_DATABASE'))
        self.cursor = self.connection.cursor()
        print(f'Connection started')

    def desconectar(self):
        self.cursor.close()
        print(f'Connection closed')

    def createTables(self):
        try:
            self.cursor.execute(self.TABLE_ATRACCTIONS)
            self.cursor.execute(self.TABLE_PROMOTIONS)
            self.cursor.execute(self.TABLE_USERS)
            self.cursor.execute(self.TABLE_USERS_PROMOTIONS)
            print(f'Created')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)

    def sendQuery(self, query, props=None):
        res:None
        try:
            self.conectar()
            if props is not None:
                self.cursor.execute(query, props)
                res = self.cursor.fetchall()
            else:
                self.cursor.execute(query)
                res = self.cursor.fetchall()
            print(f'OK Susses Query')
            return res
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
            return error
        finally:
            self.desconectar()

    def addNewUser(self, user, email, password):
        try:
            self.conectar()
            userQuery = "INSERT INTO usuarios (nombre_apellido,categoria,presupuesto,tiempo_disponible, timestamp) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(userQuery, (user['nombreApellido'], user['categoria'],user['presupuesto'], user['tiempoDisponible'], user['timestamp']))
            self.connection.commit()
            get_user_query = "SELECT id FROM usuarios WHERE timestamp = %s"
            self.cursor.execute(get_user_query, (user['timestamp']))
            response_user_id = self.cursor.fetchone()
            authQuery = "INSERT INTO auth (user_id,email,pass) VALUES(%s,%s,%s)"
            self.cursor.execute(authQuery, (response_user_id, email, password))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def upDateUser(self, userId, userUpdate):
        try:
            self.conectar()
            query_up_date = "UPDATE usuarios SET nombre_apellido= %s,categoria= %s,presupuesto= %s,tiempo_disponible= %s WHERE id = %s"
            self.cursor.execute(query_up_date, (userUpdate['nombreApellido'], userUpdate['categoria'],userUpdate['presupuesto'], userUpdate['tiempoDisponible'], userId))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def chagesIsDeleteAuthUser(self, isDelete, email, password):
        try:
            self.conectar()
            query_auth = "UPDATE auth SET isDelete=%s WHERE email=%s AND pass=%s"
            self.cursor.execute(query_auth, (isDelete, email, password))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def chagesPassAuthUser(self, email, passwordOld, passwordNew):
        try:
            self.conectar()
            query_auth = "UPDATE auth SET pass=%s WHERE email=%s AND pass=%s"
            self.cursor.execute(query_auth, (passwordNew, email, passwordOld))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def addNewPromotion(self, promotion):
        try:
            self.conectar()
            promotionQuery = "INSERT INTO promosiones (nombre,categoria,atraccion_1,atraccion_2,atraccion_n,descuento) VALUES(%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(promotionQuery, (promotion['name'], promotion['category'], promotion['atractions_one'],promotion['atractions_two'], promotion['atractions_three'], promotion['discount']))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def upDatePromotion(self, id_promotion, promotion):
        try:
            self.conectar()
            promotionQuery = "UPDATE promosiones SET nombre=%s,categoria=%s,atraccion_1=%s,atraccion_2=%s,atraccion_n=%s,descuento=%s WHERE id=%s"
            self.cursor.execute(promotionQuery, (promotion['name'], promotion['category'], promotion['atractions_one'],promotion['atractions_two'], promotion['atractions_three'], promotion['discount'], id_promotion))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def deletePromotion(self, id_promotion):
        try:
            self.conectar()
            promotionQuery = "DELETE FROM promosiones WHERE id = %s"
            self.cursor.execute(promotionQuery, (id_promotion))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def addNewAttraction(self, attraction):
        try:
            self.conectar()
            attractionQuery = "INSERT INTO atracciones (nombre,costo,duracion,cupo,tipo) VALUES(%s,%s,%s,%s,%s)"
            self.cursor.execute(attractionQuery, (attraction['name'], attraction['category'], attraction['atractions_one'],attraction['atractions_two'], attraction['atractions_three'], attraction['discount']))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()
    def upDateAttraction(self, id_attraction, attraction):
        try:
            self.conectar()
            attractionQuery = "UPDATE atracciones SET nombre=%s,costo=%s,duracion=%s,cupo=%s,tipo=%s WHERE id=%s"
            self.cursor.execute(attractionQuery, (attraction['name'], attraction['category'], attraction['atractions_one'],attraction['atractions_two'], attraction['atractions_three'], attraction['discount'], id_attraction))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def deleteAttraction(self, id_attraction):
        try:
            self.conectar()
            attractionQuery = "DELETE FROM atracciones WHERE id = %s"
            self.cursor.execute(attractionQuery, (id_attraction))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def addNewUserPromotion(self, id_user, id_promotion):
        try:
            self.conectar()
            userPromotionQuery = "INSERT INTO users_promotion (id_user=%s,id_promotion=%) VALUES(%s,%s)"
            self.cursor.execute(userPromotionQuery, (id_user, id_promotion))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()

    def deleteUserPromotion(self, id_userPromotion):
        try:
            self.conectar()
            attractionQuery = "DELETE FROM users_promorion WHERE id = %s"
            self.cursor.execute(attractionQuery, (id_userPromotion))
            self.connection.commit()
            print(f'OK Susses')
        except pymysql.Error as error:
            # Capturar y manejar el error
            print("Error de PyMySQL:", error)
        finally:
            self.desconectar()
