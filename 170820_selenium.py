from selenium import webdriver

url = 'http://45.79.43.178/source_carts/wordpress/wp-admin'
########### Selenium ############

chrome_ex = r"/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_ex)
driver.get(url)
username = driver.find_element_by_id("user_login")
password = driver.find_element_by_id("user_pass")
username.send_keys("admin")
password.send_keys("123456aA")
driver.find_element_by_name("wp-submit").click()

res = driver.get('http://45.79.43.178/source_carts/wordpress/wp-admin/users.php')
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div[4]")
driver.find_element_by_xpath("//form//table//tbody")
res1 = driver.find_elements_by_xpath("//td[@class='username column-username has-row-actions column-primary']//strong//a")
res2 = driver.find_elements_by_xpath("//td[@class='name column-name']")
for i in range(len(res1)):
    if str(res1[i].text)=='admin':
        print(str(res2[i].text))