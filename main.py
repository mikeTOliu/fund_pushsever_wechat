import get
import push
import time
import config
def main():
    data=get.GetData(config.code,config.link)
    msg=get.BuildString(data)
    msg=msg+"\n"+time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    #print(data)
    push.message(msg,config.Secret,config.corpid,config.agentid)
main()