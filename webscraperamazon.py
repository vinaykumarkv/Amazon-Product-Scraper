from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv
import re


# Set Chrome options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

# Launch browser
driver_path = r"C:\Users\vinay\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(options=options)
search_url = "https://www.amazon.in"
driver.get(search_url)
time.sleep(7)
search_url = "https://www.amazon.in/s?k=wireless+earbuds"
driver.get(search_url)
# Let page load
time.sleep(8)

# Parse page
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find product containers
products = soup.select("div.s-main-slot div[data-component-type='s-search-result']")

# CSV setup
with open("amazon_products.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating", "Link"])

    for product in products:
        # Product Name
        # Product Name
        name_tag = product.select_one("h2")
        name = name_tag.get_text(strip=True) if name_tag else "N/A"
        name = re.sub(r'\s+', ' ', name).strip()


        # Price
        price = product.select_one("span.a-price > span.a-offscreen")
        price = price.text.strip() if price else "N/A"
        if price != "N/A":
            price = re.sub(r'[^0-9.]', '', price)  # Remove all non-numeric characters except the decimal point
            price = float(price)  # Convert to float
        # Rating
        rating = product.select_one("span.a-icon-alt")
        rating = rating.text.strip() if rating else "N/A"

        # Link
        link = product.select_one("h2 a")
        link = "https://www.amazon.in" + link["href"] if link else "N/A"

        writer.writerow([name, price, rating, link])

print("✅ Data extracted and saved to amazon_products.csv")
driver.quit()
