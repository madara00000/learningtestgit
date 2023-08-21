import mysql.connector
from bs4 import BeautifulSoup
import requests
def connect_to_database():
    try:
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "rootroot",
            "auth_plugin":'caching_sha2_password',
            "database" : "db1",
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
    soup = BeautifulSoup(html, "html.parser")

    lielements = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    booksnames = []
    booksprices = []

    for l in lielements:
        tags = l.find_all("h3")
        ptags = l.find_all("p",class_="price_color")

        for tag in tags:
            booksnames.append(tag.text.strip())
        for ptag in ptags:
            price = ptag.text.strip().replace('£', '').replace('$', '')  # Remove currency symbols
            booksprices.append(float(price))



    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO books (title) VALUES (%s)"

            for book_title in booksnames:
                cursor.execute(insert_query, (book_title,))

            connection.commit()
            print("Books stored successfully.")

        except mysql.connector.Error as err:
            print("Error at data storing:", err)

        finally:
            cursor.close()
            connection.close()

    return booksnames

def main():
    booksnames,booksprices = fetch_books()

    print("Books:")
    for book in booksnames:
        print(book)
    pront("prices:")
    for price in booksprices :
        print("price")

if __name__ == "__main__":
    main()
