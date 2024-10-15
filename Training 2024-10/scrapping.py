"""
Scrapping website for prices

site url: www.mcb.nl
user name: william.cuylits@asml.com
password: CE@ASML#20A
"""

import requests
import bs4
import time

site_url = 'https://www.mcb.eu/nl'

security_check_page = '/j_spring_security_check'
login_page = '/login'

products = {
    'Aluminium EN AW-6082 T6 rond geperst': '/aluminium/aluminium-profielen-en-staven/rond/aluminium-en-aw-6082-t6-rond-geperst/p/2860-0020'
}

username = 'william.cuylits@asml.com'
password = 'CE@ASML#20A'

# Get CSRF token
r = requests.get(site_url + login_page)
if r.status_code == 200:
    soup = bs4.BeautifulSoup(r.text, features="lxml")
    login_form = soup.find('form', {"id": "loginForm"})
    csrf_token = login_form.find('input', {'name': 'CSRF_TOKEN'})
    print(csrf_token['value'])
else:
    print(r.status_code)


# with requests.Session() as session:
#
#     payload = {
#         'j_username': username,
#         'j_password': password,
#         'CSRF_TOKEN': csrf_token
#     }
#
#     # pass strict security check
#     r = session.post(site_url + security_check_page, data = payload)
#     print(r.status_code)
#
#     # login
#     for description, product_url in products.items():
#         print(description, site_url + product_url)
#         r = session.post(site_url + product_url, data = payload)
#         print(r.status_code)
#         if r.status_code == 200:
#             print('OK')
#
#         else:
#             print(f'Could not pass login form. Status code: {r.status_code}')
