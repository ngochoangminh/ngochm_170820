import requests
import json
import csv
data={}
url= r"https://438c5683f94854983321bfb375a0a401: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@minhngochoang.myshopify.com/admin/api/2020-07/customers.json"
s = requests.Session() 
res= s.get(url)
with open('customers.json','w',encoding='utf-8') as f:
    f.write(res.text)
with open('customers.json','r') as r:
    data = json.load(r)
customers=data.get('customers')
keysList=list(customers[0].keys())
addressList=[]
for i in keysList:
    if 'addres' in i: 
        addressList.append(i)
        keysList.remove(i)
with open('customers.csv','w') as wFile:
    writer = csv.writer(wFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(keysList)
    for customer in customers:
        templist=[]
        for key,val in customer.items():
            if key not in addressList:
                templist.append(val)
        writer.writerow(templist)

print("Done!");