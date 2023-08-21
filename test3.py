import mysql.connector
from bs4 import BeautifulSoup
import requests
def connect_to_database():
    try:
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "rootroot",
            "auth_plugin":'caching_sha2_password'
        }

        connection = mysql.connector.connect(**db_config)
        print("Connected to the database.")
        return connection

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

def fetch_books():
    url = "https://books.toscrape.com/"
    requrl = requests.get(url)
    html = requrl.content
    soup = BeautifulSoup(html,"html.parser")

    lielements = BeautifulSoup.find_all('li',class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")
    booksnames =[]

    divelements= BeautifulSoup.find_all('div',class_='product_price')
    booksprices=[]

    for l in lielements:
        tags=l.find_all("h3")
        for tag in tags :
            booksnames.append(tags.text.strip())

    for d in divelements :
        ptags=d.find_all("p")
        for ptag in ptags :
            booksprices.append(ptags.taxt)

    connection = connect_to_database()
    if connection:
        try:
            cursor= connection.cursor()
            insert_query="INSERT INTO books (title) VALUE (%s)"
            cursor.execute(insert_query,(booksnames))
            connection.commit()
            print("stored succesfuly")
        except mysql.connector.error as err:
            print("error at data storing")
        finally :
            cursor.close()
            connection.close()






    return booksnames



def main():

   if __name__ == "__main__":
    connect_to_database()


