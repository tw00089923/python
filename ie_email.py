#import sys
import imaplib
#import getpass
import email
import datetime
#import os 
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.header import decode_header
import re


class read_email :
    def __init__(self,user,pwd):
        self.server = "imap.gmail.com"
        self.user = user
        self.pwd = pwd
        self.observer = "wendypeng@kcr.com.tw"
        self.email_dict = []
    def connect_gmail(self):
        M = imaplib.IMAP4_SSL(self.server)
        try:
            M.login(self.user,self.pwd)
            print("Login Success!!" + self.user)
        except:
            print("fail to login" + self.user)
    def read_email_by_label_1(self,label):
        M = imaplib.IMAP4_SSL(self.server)
        #try:
        M.login(self.user,self.pwd)
        print("success to login "+self.user)
        rv , data = M.select(label)
   
        uids =data[0].split()
        max_mail = int(str(uids[0],'utf-8'))   
        save = {}
        for i in range(0,max_mail,1):
            bytes1 = bytes(str(max_mail-i), encoding = "utf-8")
            typ , dat = M.fetch(bytes1,'(RFC822)')
            sub = email.message_from_bytes(dat[0][1])
            if sub.is_multipart:             
                parse_subject = email.header.decode_header(sub['subject'])
                #from_kcr = email.header.decode_header(sub['from'])
                print(parse_subject[0])
                #print(type(sub.get_payload()[0].get_payload()))
                #print(sub.get_all)
                
                
                #if sub.is_multipart:
                    #charset = parse_subject[0][1]
                    #patten = r'RT-[0-9]{5}'
                    #match = re.findall(patten,sub.get_payload()[0].get_payload())
                    #print(match)     
                        
                    #if charset == "gb2312":
                        #title = parse_subject[0][0].decode("gbk")
                        #save[title] = [1]
                        #save.update({from_kcr[1][0].decode('gbk'):parse_subject[0][0].decode("gbk")})
                    #elif charset is None:
                        #save.update({from_kcr[1][0]:parse_subject[0][0]})
                    #else:
                        #save.update({from_kcr[1][0].decode(charset):parse_subject[0][0].decode(charset)})
                #else:
                   # charset = parse_subject[0][1]
                    #print(patten,sub.get_payload()[0].get_payload())
                   # if charset == "gb2312":
                       # title = parse_subject[0][0].decode("gbk")
                        #save[title] = [1]
        print(save)
    


       
user =""
pwd =""
a = read_email(user,pwd)
a.read_email_by_label_1("KCR_EC")



#a = b'3'

#print(int(str(a,'utf-8')))

#b= str(a,'utf-8')
#for i in range(1,int(str(a,'utf-8')),1):
  # print(bytes(str(i), encoding = "utf-8"))
