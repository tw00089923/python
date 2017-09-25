import sys
import imaplib
#import getpass
import email
import datetime
import os 
from email.mime.text import MIMEText
from email.mime.message import MIMEMessage
from email.header import decode_header
import unicodedata
class read_email :
    def __init__(self):
        self.server = "imap.gmail.com"
        self.user = "tw00089923@cycu.org.tw"
        self.pwd = "kcr01260"
        self.observer = "wendypeng@kcr.com.tw"
        self.email_dict = {}
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
        bytes1 = bytes(str(max_mail-5), encoding = "utf-8")
        tpy , dat =M.fetch(bytes1,'(RFC822)')

        parser_mail2bytes = email.message_from_bytes(dat[0][1])
        print(email.parser.HeaderParser(dat[0][1]))
        parse_a = MIMEText(parser_mail2bytes['subject'],'plain',"gb2312")
        #print(email.header.make_header(email.header.decode_header(parser_mail2bytes['subject'])))
        b = decode_header(parser_mail2bytes['subject'])
        
        
    
        #print(parse_mail)
           # byte_number = self.byte2int(last_email_id)
           # print(byte_number)
            #for i in range(1,int(str(last_email_id,'utf-8'))+1,1):
               # tpy , dat =M.fetch(bytes(str(i), encoding = "utf-8"),'(RFC822)')
               # sub = email.message_from_bytes(dat[0][1])
               # parse_subject = email.header.make_header(email.header.decode_header(sub['subject']))
               # print(parse_subject)

                #for i in dat:
                    
                   # print(dat[0][1])

                
                #for response_part in dat:
                   # if isinstance(response_part, tuple):
                      #  if tpy == "OK":      

                            #sub = email.message_from_bytes(dat[0][1])
                            #print(sub)
                          #  parse_subject = email.header.make_header(email.header.decode_header(sub['Subject']))
                            #print(parse_subject)
                            #print(parse_subject)
                           # if parse_from == self.observer:
                               # print(parse_from)
                            #self.email_dict.append(str(parse_subject))
                           # self.email_dict['subject'] = str(parse_subject)
                        #  for response_part in dat:
        #except:
           # print("false!")
    def read_email_by_label_2(self,label):
        M = imaplib.IMAP4_SSL(self.server)
        try:
            M.login(self.user,self.pwd)
            print("success to login "+self.user)
            rv , data = M.select(label)
            a = data[0].split()
            first_email_id = a[0]
            last_email_id = a[-1]
            print(last_email_id)
            for i in range(1,int(str(last_email_id,'utf-8'))+1,1):
                tpy , dat =M.fetch(bytes(str(i), encoding = "utf-8"),'(RFC822)') 
                if tpy == "OK":                    
                    sub = email.message_from_bytes(dat[0][1])
                    print(sub)
                    parse_subject = email.header.make_header(email.header.decode_header(sub['Subject']))
                    
                    parse_from = sub['From']
                   
                    if parse_from == self.observer:
                        print(parse_from)
                    self.email_dict.append(str(parse_subject))

        except:
            print("false!")
            


a = read_email()
a.read_email_by_label_1("KCR")


#a = b'3'

#print(int(str(a,'utf-8')))

#b= str(a,'utf-8')
#for i in range(1,int(str(a,'utf-8')),1):
  # print(bytes(str(i), encoding = "utf-8"))
