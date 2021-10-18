from re import I
import requests,json

from requests.exceptions import MissingSchema
def GetData(code,link):
    url=link+code
    r=requests.get(url)
    jsons=r.json()
    return jsons
def BuildString(data):
    msg="" 
    for data in data["data"]:
        msg=msg+"*******\n"
        for name in data:
            if name=="name":
                msg=msg+"基金名:"+data[name]+"\n"
            if name=="netWorth":
                msg=msg+"单位净值:"+str(data[name])+"\n"
            if name=="expectGrowth":
                msg=msg+"估算日涨幅"+str(data[name])+"%"+"\n"
            if name=="dayGrowth":
                msg=msg+"净值日涨幅"+str(data[name])+"%"+"\n"
    return msg






