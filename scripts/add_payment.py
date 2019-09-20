import requests

url = "https://edge.qiwi.com/checkout/api/bill/search?statuses=READY_FOR_PAY&rows=50"
headers = {'Accept': 'application/json',
           'Authorization': 'Bearer 6c374418ff51afdff99b11558c859ab7',
           'Host': 'edge.qiwi.com',
           "User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers)
print(r.json())

POST / checkout / invoice / pay / wallet
HTTP / 1.1
Accept: application / json
Content - type: application / json
Authorization: Bearer ** *
Host: edge.qiwi.com
User - Agent: ** **

{
    "invoice_uid": "1063702405",
    "currency": "643"
}
