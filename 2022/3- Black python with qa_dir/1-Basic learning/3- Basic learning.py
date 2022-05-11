#اول برای جلوگیری از تداخل ماژول ها بهتره یاد بگیری که virtual environment  رو اجرا کنی.
#First, to avoid module interference, it is better to learn to run a virtual environment.

import platform,socket,re,uuid,json,psutil,logging

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


# print(json.loads(getSystemInfo()))

dict_ = json.loads(getSystemInfo())

for key, value in dict_.items():
    print(f'{key} = {value}')
