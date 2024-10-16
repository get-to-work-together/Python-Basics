import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# This is not needed if chromedriver is already on your path:
chromedriver_path = '/opt/homebrew/bin/chromedriver'

service = Service(executable_path=chromedriver_path)

options = Options()
options.add_argument("--window-size=1920x1080")
options.add_argument("--verbose")
# options.add_argument("--headless")

# Set up the WebDriver (assuming Chrome)
driver = webdriver.Chrome(service = service, options = options)

url = 'https://www.mcb.nl'
username = 'william.cuylits@asml.com'
password = 'CE@ASML#20A'

# Open a web page
driver.get(url)

# Retrieve and print the title of the page
print(driver.title)

# Just for not let the browser immediate closed
time.sleep(10)

# Close the browser
driver.quit()
