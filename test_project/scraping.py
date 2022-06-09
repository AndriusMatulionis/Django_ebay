import sqlite3
import requests
from bs4 import BeautifulSoup
from product import Product

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
url = 'https://www.ebay.com/sch/i.html?_nkw='


def extract(asin, items_per_page):
    data = requests.get(url + str(asin) + '&_ipg=' + str(items_per_page)).text
    soup = BeautifulSoup(data, 'html.parser')
    product_block = soup.find_all('div', class_='s-item__info clearfix')
    return product_block


def main():
    items = extract("lego", "240")
    item_id = 0
    c.execute("  DROP TABLE IF EXISTS scraped")
    print("Table 'scraped' DELETED")
    c.execute("""CREATE TABLE IF NOT EXISTS scraped(
            id,
            item,
            price,
            location,
            condition,
            seller,
            url
    )""")
    print("Table 'scraped' CREATED")
    for item in items:
        products = Product(item)
        if products.seller == 'Top Rated Seller':
            item_id += 1
            attribute_list = [item_id, products.item, products.price,
                              products.location, products.condition, products.seller, products.url]
            c.execute("INSERT OR IGNORE INTO scraped VALUES (?,?,?,?,?,?,?)", attribute_list)
    print("Scraped data sent to database")
    
    conn.commit()
    conn.close()
        
        
if __name__ == "__main__":
    main()
