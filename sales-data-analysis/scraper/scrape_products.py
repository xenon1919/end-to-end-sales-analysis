import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = []

for book in soup.select(".product_pod"):
    name = book.h3.a["title"]

    price_text = book.select_one(".price_color").text
    price = price_text.replace("£", "").replace("Â", "").strip()

    rating = book.p["class"][1]

    products.append({
        "ProductName": name,
        "ScrapedPrice": float(price),
        "Rating": rating
    })


df_scraped = pd.DataFrame(products)
df_scraped.to_csv("scraped_products.csv", index=False)

print("Scraped data saved as scraped_products.csv")
