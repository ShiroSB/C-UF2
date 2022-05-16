import functions
import mysql.connector
from mysql.connector import errorcode


connection_args = {
    'host': 'mysql-shirosb.alwaysdata.net',
    'user': 'shirosb',
    'password': '39709796',
    'database': 'shirosb_db'
}

def insert_data(identificador,nombre, autor,fecha,idioma):
    try:
        cnx = mysql.connector.connect(**connection_args)
        sql = ("INSERT INTO libros "
               "(identificador,nombre,autor,fecha,idioma) "
               "VALUES (%s, %s, %s, %s, %s)")
        data = (identificador,nombre, autor,fecha,idioma)
        crs = cnx.cursor()
        crs.execute(sql, data)
        cnx.commit()
        print(crs.rowcount, "hecho")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrecta")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)
    else:
        cnx.close()

def create_table():
    connection_args.update({'database': 'shirosb_db'})
    try:
        cnx = mysql.connector.connect(**connection_args)
        table = (
            "CREATE TABLE `libros` ("
            "  `identificador` int(50) NOT NULL AUTO_INCREMENT,"
            "  `nombre` varchar(50) NOT NULL,"
            "  `autor` varchar(50) NOT NULL,"
            "  `fecha` varchar(20) NOT NULL,"
            "  `idioma` varchar(50) NOT NULL,"
            "  PRIMARY KEY (`identificador`)"
            ") ENGINE=InnoDB")

        crs = cnx.cursor()
        crs.execute(table)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrecta")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)
    else:
        cnx.close()
