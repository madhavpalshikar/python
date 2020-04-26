import re

def validateIP(ipa):
    regex = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'

    if(re.search(regex, ipa)):
        return 1
    else:
        return 0

def recComb(s):
    for i in range(1,4):
        for j in range(4,7):
            for k in range(7,10):
                ip = s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:]
                if(validateIP(ip)==1):
                    print(ip)

recComb('2542540123')