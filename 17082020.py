import sys
import requests
from lxml import html

url = 'http://45.79.43.178/source_carts/wordpress/wp-login.php'
user_url = 'http://45.79.43.178/source_carts/wordpress/wp-admin/users.php'

info = {
    'log': 'admin', 
    'pwd': '123456aA'
    }
jar=requests.cookies.RequestsCookieJar()
jar.set('wordpress_test_cookie','WP+Cookie+check')
jar.set('tk_ai','woo%3Aif%2BZOxwi5PZuZCKOOqMrX0Ux')

s = requests.Session()
s.cookies = jar
res_login = s.post(url,data=info)
res_users = s.get(user_url)
doc = html.fromstring(res_users.content)
xpart_user ='//td[@class="username column-username has-row-actions column-primary"]//strong/a'
xpart_name ='//td[@class="name column-name"]'
res_user = doc.xpath(xpart_user)
res_name = doc.xpath(xpart_name)
for i in range(len(res_user)):
    if str(res_user[i].text) == info.get('log'):
        print(str(res_name[i].text))
        break