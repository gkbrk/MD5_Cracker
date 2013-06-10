def hashToCrackWithArgv():
    import sys
    
    if len(sys.argv)>1:
        return str(sys.argv[1])
    else:
        return raw_input('Enter the MD5 hash you would like to crack:')

def styledCrackResult(serviceName,md5):
    if md5:
        return "[+] Succesfully cracked with "+str(serviceName)+" - "+str(md5)
    else:
        return "[-] Failed to crack with "+str(serviceName)

def crackWithMd5OnlineOrg(md5):
    import re
    import mechanize
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open('http://www.md5online.org/')
    br.select_form(nr=0)
    br['md5'] = md5
    
    response2 = br.submit()
    source=response2.read()
    
    found=re.search("limegreen'>Found : <b>(.*?)</b></span>",source)
    if found:
        return found.group(1)
    else:
        return False

def crackWithCmd5Org(md5):
    import re
    import mechanize
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open('http://www.cmd5.org/')
    br.select_form(nr=0)
    br['ctl00$ContentPlaceHolder1$TextBoxInput'] = md5
    
    response2 = br.submit()
    source=response2.read()
    
    found=re.search('LabelAnswer">(.*?)</span>',source)
    if found:
        return found.group(1)
    else:
        return False

def crackWithTobtu(md5):
    import re
    import mechanize
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open('http://www.tobtu.com/md5.php?h='+str(md5))
    source=response.read()
    
    found=re.search(str(md5)+':.*?:(.*?)\n',source)
    if found:
        return found.group(1)
    else:
        return False

def crackWithDarkbyteRu(md5):
    import mechanize
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open('http://md5.darkbyte.ru/api.php?q='+str(md5))
    source=response.read()
    
    if len(source)>0:
        return source
    else:
        return False

def crackWithMD5net(md5):
    import re
    import mechanize
    
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open('http://www.md5.net/cracker.php')
    br.select_form(nr=0)
    br['hash'] = md5
    
    response2 = br.submit()
    source=response2.read()
    
    found=re.search('<input type="text" id="hash" size="32" value="(.*?)">',source)
    if found:
        return found.group(1)
    else:
        return False

print "Online MD5 Cracker"

hashToCrack = hashToCrackWithArgv()

print styledCrackResult("MD5online.org",crackWithMd5OnlineOrg(hashToCrack))
print styledCrackResult("CMD5.org",crackWithCmd5Org(hashToCrack))
print styledCrackResult("Tobtu.com",crackWithTobtu(hashToCrack))
print styledCrackResult("Darkbyte.ru",crackWithDarkbyteRu(hashToCrack))
print styledCrackResult("MD5.net",crackWithMD5net(hashToCrack))
