import requests
from requests.auth import HTTPBasicAuth 
from requests import session
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'
response = requests.get(url, auth = HTTPBasicAuth('admin', '123456aA')) 
 
# print(response.cookies.keys) 
print(response) 


info = {
    'username': 'admin',
    'password': '123456aA'
}
with session() as c:
    c.post(url, data=info)
    response = c.get(url)
    print(response.headers)
    # print(response.text)

##### selenium ####
# driver = webdriver.Firefox()
# driver.get(url)
# username = driver.find_element_by_id("username")
# password = driver.find_element_by_id("password")
# username.send_keys("admin")
# password.send_keys("123456aA")
# driver.find_element_by_name("submit").click()

