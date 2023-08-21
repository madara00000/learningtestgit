from bs4 import BeautifulSoup
import requests
import mysql.connector



def connecttothedbase():
    try:
        dbconfig={
            "host" :"localhost",
            "username":"root",
            "password":"rootroot"

        }
        cnx=mysql.connector.connect(**dbconfig)
        print("succesfuly connected")
        return cnx

    except mysql.connector.Error as err:
        print("error at connecting to the server :",err)