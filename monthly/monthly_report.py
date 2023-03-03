import requests

url = "https://notify-api.line.me/api/notify"
# input token from Line Notify Service when you connect first 
token = "9T6wLfV6Knmk225oaJyDz8C30vqJ72xUPmVNQLveK3l"
headers = {"Authorization" : "Bearer "+ token} 
message =  {"type massage here"}
payload = {"Wow" :  message} 
r = requests.post(url, headers = headers, params=payload)