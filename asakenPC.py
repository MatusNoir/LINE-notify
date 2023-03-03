import requests
import time

toki = time.time()
jikoku = time.ctime(toki)

url = "https://notify-api.line.me/api/notify" 
token = "qc5GVWfxIRvkAMeAiyP1KFUzsvIz5s1PqUXkSOUqy5C"
headers = {"Authorization" : "Bearer "+ token} 
message =  {"\n【注意】13:30までです.\nhttps://ryohin.ccms.works-hi.co.jp/cws/mbl/MblActLogin"}
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload)