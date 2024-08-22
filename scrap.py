import requests
from urllib3.exceptions import InsecureRequestWarning
import warnings
from bs4 import BeautifulSoup
import pandas as pd
import os
from urllib.parse import urljoin

os.system("clear")

folder_name = 'name your folder'
excel_name = 'name your excel file.xlsx'

warnings.simplefilter('ignore', InsecureRequestWarning)

def download_image(url, filename):
    print(f"Attempting to download image from {url}")
    try:
        response = requests.get(url, verify=False, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image successfully saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download image from {url}")
        print(f"Error: {e}")
        return False
    return True

print("Starting web scraping process...")

url = "https://example.com"
print(f"Sending GET request to {url}")
response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the webpage")
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Parsed HTML content")

    products = soup.find_all('div', class_='mid-pop')
    print(f"Found {len(products)} products on the page")

    names = []
    codes = []
    prices = []
    image_urls = []

    print("Extracting product information...")
    for i, product in enumerate(products, 1):
        name = product.find('h6').text.strip()
        code = name.split()[-1]
        price = product.find('p').text.strip().split()[0].replace('$', '')
        image_url = product.find('img')['src']
        
        names.append(name)
        codes.append(code)
        prices.append(price)
        image_urls.append(image_url)
        
        print(f"Processed product {i}: {code}")

    print("Creating DataFrame...")
    df = pd.DataFrame({
        'Name': names,
        'Code': codes,
        'Price': prices
    })

    print("Exporting data to Excel...")
    df.to_excel(excel_name, index=False)
    print(f"Data exported to {excel_name}")

    if not os.path.exists(folder_name):
        print(f"Creating {folder_name} directory...")
        os.makedirs(folder_name)
        print(f"{folder_name} directory created")

    print("Downloading product images...")
    for i, (code, image_url) in enumerate(zip(codes, image_urls), 1):
        full_url = urljoin(url, image_url)
        filename = f"{folder_name}/{code}.jpg"
        if download_image(full_url, filename):
            print(f"Processed image {i} of {len(codes)}")
        else:
            print(f"Skipped image {i} of {len(codes)}")

print("Scraping completed.")
