import requests
from requests.auth import HTTPBasicAuth
from selenium import webdriver

url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'
user_url = "http://45.79.43.178/source_carts/wordpress/wp-admin/users.php"
response = requests.get(url, auth = HTTPBasicAuth('admin', '123456aA')) 
 
# print(response.cookies.keys) 
print(response.content) 


chrome_ex = r"/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_ex)
driver.get(url)
username = driver.find_element_by_id("user_login")
password = driver.find_element_by_id("user_pass")
username.send_keys("admin")
password.send_keys("123456aA")
driver.find_element_by_name("wp-submit").click()
res = driver.get(user_url)
res = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[4]")
res = driver.find_element_by_xpath("//form")
res = driver.find_element_by_xpath("//table//tbody//tr[@id='user-1']")
res = driver.find_element_by_xpath("//td[2]")
print(res)