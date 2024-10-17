import time
from csv import DictWriter

import requests
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ------------------------------------------------------------------------
# Set up the WebDriver (assuming Chrome)

# This is not needed if chromedriver is already on your path:
chromedriver_path = '/opt/homebrew/bin/chromedriver'
service = Service(executable_path=chromedriver_path)

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
# options.add_argument("--headless")

driver = webdriver.Chrome(service = service, options = options)

# ------------------------------------------------------------------------
# Home page

url = 'https://www.mcb.nl'
driver.get(url)

# Retrieve and print the title of the page
print(driver.title)

# Just for not let the browser immediate closed
time.sleep(2)

# Pass Cookie Dialog Button id="CybotCookiebotDialogBodyButton"
button = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonAccept")
button.click()

time.sleep(1)

# ------------------------------------------------------------------------
# Login

url = 'https://www.mcb.eu/nl/login'
driver.get(url)

username = 'william.cuylits@asml.com'
password = 'CE@ASML#20A'

username_input = driver.find_element(By.NAME, "j_username")
username_input.send_keys(username)

password_input = driver.find_element(By.NAME, "j_password")
password_input.send_keys(password)

submit_button = driver.find_element(By.ID, "submit_login_form")
submit_button.click()

time.sleep(1)

# ------------------------------------------------------------------------
# Products

products = {
    'Aluminium EN AW-6060 T66 ronde buis': {
        'product_url': 'https://www.mcb.eu/nl/aluminium/aluminium-buizen/rond/aluminium-en-aw-6060-t66-ronde-buis/p/2810-0050?',
        'article_number': '2810-0050-81',
        'minimum_quantity': 250,
    },
    'Aluminium EN AW-2033 T8 rond nagetrokken h11': {
        'product_url': 'https://www.mcb.eu/nl/aluminium/aluminium-profielen-en-staven/rond/aluminium-en-aw-2033-t8-rond-nagetrokken-h11/p/2860-0150?',
        'article_number': '2860-0150-10',
        'minimum_quantity': 250,
    },
}

# Copy cookies from Selenium to requests

with requests.Session() as session:
    selenium_user_agent = driver.execute_script("return navigator.userAgent;")
    session.headers.update({"user-agent": selenium_user_agent})
    for cookie in driver.get_cookies():
        session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

    collected_information = []

    for product_name, product_settings in products.items():
        product_url = product_settings['product_url']
        article_number = product_settings['article_number']
        minimum_quantity = product_settings['minimum_quantity']

        print(f'{product_name} - {article_number}')

        driver.get(product_url)

        prices_url = product_url[:product_url.rfind('/')+1] + article_number + '/price'

        # Use requests to get price information

        response = session.get(prices_url)
        bulk_price = response.json()[article_number]['prices'][str(minimum_quantity)]

        currency = bulk_price['currencyIso']
        price = bulk_price['value']

        # Add to collected_information

        collected_information.append({
            'product_name': product_name,
            'product_url': product_url,
            'article_number': article_number,
            'minimum_quantity': minimum_quantity,
            'currency': currency,
            'price': price,
        })

        currency = None
        price = None


# ------------------------------------------------------------------------
# Export to csv file

filename = 'mcb_collected_prices.csv'

# Export using csv
# with open(filename, 'w') as f:
#     writer = csv.DictWriter(f,
#                             delimiter=';',
#                             quoting=csv.QUOTE_NONNUMERIC,
#                             fieldnames=collected_information[0].keys())
#     writer.writeheader()
#     for row in collected_information:
#         writer.writerow(row)

# Export using pandas
df = pd.DataFrame.from_records(collected_information)
df.to_csv(filename, sep=';', index=False, quoting=csv.QUOTE_NONNUMERIC)

# ------------------------------------------------------------------------
# Close the browser
print('Done')
driver.quit()
