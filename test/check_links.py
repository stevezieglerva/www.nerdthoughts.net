from bs4 import BeautifulSoup,SoupStrainer
import urllib.request
import colorama,re,queue,threading
from colorama import Fore
from urllib.parse import *

class check_link():
    def __init__(self,address):
        self.address=address        
    def check(self,address):   
        try:
            print("Checking: " + address)
            req=urllib.request.Request(url=address)
            resp=urllib.request.urlopen(req)
            if resp.status in [400,404,403,408,409,501,502,503]:print (Fore.RED+resp.status+"-"+resp.reason+"-->"+address)               
            else: print (Fore.GREEN+"no problem in-->"+address)
                              
        except Exception as e:
            print (Fore.YELLOW+"{}-{}".format(e,address))
            pass   
def pattern_adjust(a):  
    print("\tAdjusting pattern: " + a)
    try:
        if re.match('^#' ,a):return 0 
        r=urlsplit(a)
        if r.scheme=='' and (r.netloc!='' or r.path!=''):
            d=urlunsplit(r)
            if re.match('^//' ,d):
                m= re.search('(?<=//)\S+', d)
                d=m.group(0)  
                m="https://"+d
                print("\t\tReturning match")
                return m
        elif r.scheme=='' and r.netloc=='':
            print("\t\tReturning address" + a)
            return address+a
        else:return a
    except Exception as e:
        pass
def extract_link(address):
    print("Extract link: " + address)
    tags= {'a':'href', 'img':'src', 'script':'src', 'link':'href' }
    for key,value in iter(tags.items()):    
        try:
            res=urllib.request.urlopen(address)
            response=res.read().decode('utf-8') #needs improvement
            for link in BeautifulSoup(response,"html.parser",parse_only=SoupStrainer(key)): 
                if link.has_attr(value):
                    print("\tLink has value: " + link[value])
                    p=pattern_adjust(link[value])
                    print("Found link: " + p)
                    if p!=0 and str(p)!='None':        
                        print("\t\tReal link")
                        newcheck=check_link(p)
                        newcheck.check(p)
                        if p not in hyperlinks:
                            print("Addding " + p)
                            hyperlinks.add(p)
                            if website.split('.')[1] in p:#needs improvement
                                if not website.endswith(('.png','.jpeg','.js','jpg')):
                                    q.put(p)
                                    print("*** Queue size: " + str(q.qsize()))                    
        except Exception as e:
            print (e,address)                                
def threader():
    while True:
        value=q.get() 
        print("\n\nGot queue item: " + value) 
        result=extract_link(value)
        q.task_done()
        print("*** Queue size left: " + str(q.qsize())) 

if __name__=="__main__":
    colorama.init()
    q=queue.Queue()
    global hyperlinks,website
    hyperlinks=set()
    #website=input("Please enter the website address: ") 
    website = "https://www.cnn.com/"
    for x in range(30):
        t=threading.Thread(target=threader)
        t.deamon=True
        t.start()   
    q.put(website.strip())
    q.join()