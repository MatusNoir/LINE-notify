import requests

url = "https://notify-api.line.me/api/notify" 
token = "9T6wLfV6Knmk225oaJyDz8C30vqJ72xUPmVNQLveK3l"
headers = {"Authorization" : "Bearer "+ token} 
message =  {"\n【注意】13:30までです.\nhttps://ryohin.ccms.works-hi.co.jp/cws/mbl/MblActLogin"}
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload)