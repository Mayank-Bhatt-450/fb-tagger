import SendKeys
import time
import os
a12=['A', 'B','C','D','E','F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i1=True
def loaded(f,lst):
    h=open(str(f)+".txt","w")
    h.writelines(lst)
    h.close()
def time1():

    p=[''' 

                                   /$$$$$$      
                                  /$$$_  $$     
                                 | $$$$\ $$  
                                 | $$ $$ $$  
                                 | $$\ $$$$  
                                 | $$ \ $$$   
                                 |  $$$$$$/    
                                  \______/      

''','''                                                      
                                   /$$    
                                  /$$$$       
                                 |_  $$      
                                   | $$      
                                   | $$       
                                   | $$       
                                  /$$$$$$     
                                 |______/      

''','''                                                        
                                   /$$$$$$    
                                  /$$__  $$     
                                 |__/  \ $$     
                                   /$$$$$$/     
                                  /$$____/      
                                 | $$          
                                 | $$$$$$$$     
                                 |________/
''','''
                                   /$$$$$$ 
                                  /$$__  $$
                                 |__/  \ $$
                                    /$$$$$/
                                   |___  $$
                                  /$$  \ $$
                                 |  $$$$$$/
                                  \______/ 
''']
    for i in range(4):
        os.system('cls')
        print(p[3-i])
        if i!=4:
            time.sleep(1)
        else:
            time.sleep(0.3)
                                                        
def check(l5):
    l=l5
    l3=l5
    l1=[]
    l2=[]
    notlist=[]
    for i in range(len(l3)):
        no=0
        no1=0
        if l3[i]not in notlist:
            for j in range(len(l3)):
                if l3[i]==l3[j] and l3[j]:
                    no+=1
                    no1+=1
                    if no1 != 1:
                        notlist.append(l3[j])
                else:
                    pass
            
            if no>1:
                #print(no)
                l1.append(l3[i])
                l2.append(no)
            else:
                pass
    for i in range(len(l1)):
            for j in range(l2[i]-1):
                l.remove(l1[i])
    h=open("dublicates.txt","w")
    for i in range(len(l1)):
        h.write('one of them is taged                 {'+str(l1[i])+"="+str(l2[i])+"}"+"\n")
    h.close()
    return(l)

#----------------------------------------------------------------------------------------------------------------------------------

def clear(a):
    tem=''
    no=0
    if "?"in a:
        return("not")
    if " (" in a:
        
        while(no<len(a)):
            if a[no]==" " and a[no+1]=='(':
                while(a[no]!=")"):
                    no+=1
                no+=1
            else:
                tem+=a[no]
                no+=1
        return(tem)
    else:
        return(a)
#-----------------------------------------------------------------------------------------------------------------------------------------------
def listit():   
    f=open("123.txt","r")
    a=f.readlines()
    listoffriends=[]
    for i in a:
         x=clear(str(i))
         if x!="not":
             listoffriends.append(x.rstrip("\n"))
         else:
            pass
    f.close()
    #test(check(listoffriends))
    return(check(listoffriends))##########################################################################
#------------------------------------------------------------------------------------------------------------------------------------------------
def listdone(j,fy):
    sendit= str(l[j]).encode('utf-8')
    #print(sendit.decode('unicode-escape'))
    SendKeys.SendKeys(sendit,with_spaces=True,with_newlines=True)#just write is as it is
    time.sleep(fy)
    SendKeys.SendKeys("{UP}",with_spaces=True,with_newlines=True)
    SendKeys.SendKeys("{UP}",with_spaces=True,with_newlines=True)
    SendKeys.SendKeys("{ENTER}",with_spaces=True,with_newlines=True)
    #SendKeys.SendKeys('{DOWN}',with_spaces=True,with_newlines=True)
    
#---------------------------------------------------------------------------------------------------------------------------------------------------
tem=1
yf=0.3
while (tem==1):
    os.system('cls')
    print("                     ----------------welcome--------------")
    print("                     -------------------------------------") 
    q=raw_input('                     --{set time lag of net(in seconds)}--\n                                   :-')
    if q=='':
        yf=(0.3)
        tem=2
    else:
        try:
            yf=(float(q))
            tem=2
        except:
            print "error"
    print("-------------------------")
h=open("not taged.txt","w")
h.close()
#l=sorted(listit())
l=(listit())
#print l
j=0
kt=0
j1=0

#print(len(l))
while(j<=len(l)):
    not_tag=[]
    i2=1
    os.system('cls')
    print("total try:-"+str(j)+"/"+str(len(l)))
    print("total tag:-"+str(kt)+"/"+str(len(l)))
    wast=str(raw_input("press enter to proceed"))
    time1()
    while (i2<=100):
        if j<len(l):
            for k in a12:
                try:
                    a=open(k+':\\cmd.txt','r')
                    b=a.read()
                    a.close()
                    if 'stop' in b:
                        i1=False
                        break
                    else:
                        pass
                except:
                    pass
            if i1 ==True:
                try:
                    
                    listdone(j,yf)###################################################################################
                    #print(l[j])
                    kt+=1
                    i2+=1
                    #time.sleep(1)
                except:
                    try:
                        not_tag.append(l[j])
                    except:
                        
                        #print(l[j],)
                        pass
            else:
                j1=j
                j=len(l)+1
                break
            os.system('cls')
            print("total try:-"+str(j)+"/"+str(len(l)))
            print("total tag:-"+str(kt)+"/"+str(len(l)))
            j+=1
        else:
            j1=j
            j=len(l)+1
            break
    h=open("not taged.txt","a+")
    for i in not_tag:
        h.write("not taged              {"+i+"}"+"\n")
    h.close()
os.system('cls')
print("total try:-"+str(j1)+"/"+str(len(l)))
print("total tag:-"+str(kt)+"/"+str(len(l)))
raw_input('''\nALL TAGED
PRESS ENTER TO CLOSE''')
