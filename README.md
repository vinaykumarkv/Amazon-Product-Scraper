# Amazon Product Scraper

This script uses Selenium and BeautifulSoup to scrape product information from
Amazon. It extracts the product name, price, rating, and link for wireless
earbuds and saves the data to a CSV file.

## Prerequisites

Before running the script, ensure you have the following installed:

  1. **Python:** Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
  2. **ChromeDriver:** Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/) and place it in a directory. Note the path to `chromedriver.exe`.
  3. **Python Libraries:** Install the required Python libraries using pip. 
         
         pip install selenium beautifulsoup4

## Instructions

  1. **Clone the Repository:**
         
         git clone https://github.com/your-username/your-repo-name.git
         cd your-repo-name

  2. **Update ChromeDriver Path:** Open the script in a text editor and update the `driver_path` variable with the path to your `chromedriver.exe`. 
         
         driver_path = r"C:\path\to\your\chromedriver.exe"

  3. **Run the Script:** Execute the script using Python. 
         
         python amazon_scraper.py

  4. **Check the Output:** After the script runs, you will find a file named `amazon_products.csv` in the same directory. This file contains the extracted product information.

## Script Explanation

### Import Libraries

    
    
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    import time
    import csv
    import re

### Set Chrome Options

    
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

### Launch Browser

    
    
    driver_path = r"C:\Users\vinay\chromedriver-win64\chromedriver.exe"
    driver = webdriver.Chrome(options=options)
    search_url = "https://www.amazon.in"
    driver.get(search_url)
    time.sleep(7)
    search_url = "https://www.amazon.in/s?k=wireless+earbuds"
    driver.get(search_url)
    time.sleep(8)

### Parse Page

    
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = soup.select("div.s-main-slot div[data-component-type='s-search-result']")

### CSV Setup

    
    
    with open("amazon_products.csv", mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Price", "Rating", "Link"])
    
        for product in products:
            name_tag = product.select_one("h2")
            name = name_tag.get_text(strip=True) if name_tag else "N/A"
            name = re.sub(r'\s+', ' ', name).strip()
    
            price = product.select_one("span.a-price > span.a-offscreen")
            price = price.text.strip() if price else "N/A"
            if price != "N/A":
                price = re.sub(r'[^0-9.]', '', price)
                price = float(price)
    
            rating = product.select_one("span.a-icon-alt")
            rating = rating.text.strip() if rating else "N/A"
    
            link = product.select_one("h2 a")
            link = "https://www.amazon.in" + link["href"] if link else "N/A"
    
            writer.writerow([name, price, rating, link])

### Close Browser

    
    
    print("✅ Data extracted and saved to amazon_products.csv")
    driver.quit()

## Notes

  * Ensure that the ChromeDriver version matches your installed version of Chrome.
  * The script is designed to scrape wireless earbuds. You can modify the `search_url` variable to scrape other products.
  * Be mindful of Amazon's terms of service regarding web scraping.

