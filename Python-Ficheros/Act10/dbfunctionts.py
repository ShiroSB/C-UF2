import functions
import mysql.connector
from mysql.connector import errorcode


connection_args = {
    'host': 'mysql-shirosb.alwaysdata.net',
    'user': 'shirosb',
    'password': '39709796',
    'database': 'shirosb_db'
}

def insert_data(identificador,cantante,cancion,fecha,visualizaciones):
    try:
        cnx = mysql.connector.connect(**connection_args)
        sql = ("INSERT INTO grades "
               "(identificador,cantante,cancion,fecha,visualizaciones) "
               "VALUES (%s, %s, %s, %s, %s)")
        data = (identificador,cantante, cancion,fecha,visualizaciones)
        crs = cnx.cursor()
        crs.execute(sql, data)
        cnx.commit()
        print(crs.rowcount, "registres inserits.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()

def create_table():
    connection_args.update({'database': 'shirosb_db'})
    try:
        cnx = mysql.connector.connect(**connection_args)
        table = (
            "CREATE TABLE `grades` ("
            "  `identificador` int(11) NOT NULL AUTO_INCREMENT,"
            "  `cantante` varchar(50) NOT NULL,"
            "  `cancion` varchar(50) NOT NULL,"
            "  `fecha` varchar(20) NOT NULL,"
            "  `visualizaciones` int(255) NOT NULL,"
            "  PRIMARY KEY (`identificador`)"
            ") ENGINE=InnoDB")
        '''creem el cursor,
        executem la sentència i fem commit
        '''
        crs = cnx.cursor()
        crs.execute(table)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()
