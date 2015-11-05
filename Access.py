import time
import requests
import os
from bs4 import BeautifulSoup
import ast
import re
from Tkinter import *
import tkMessageBox
root = Tk()
root.geometry("400x200+0+0")
root.title('MHS Color Printing')
can_notify = False
class Sheets(object):
    def __init__(self):
        
        self.url = 'https://docs.google.com/spreadsheets/d/18py6NHCJipTqDTw2xncXgbUWlbQyK6rGmJFM6FHnG8I/edit?pli=1#gid=1279292193'
        
        self.user = 'icadetprintscraper@gmail.com'
        self.passw = 'iCadet_Print_Scraper'
        
    def update_page(self):
        page = requests.get(self.url,auth=(self.user,self.passw))
        data = page.content
        data = BeautifulSoup(data,'html.parser').prettify()
        data_index = str(data).find("firstchunk")
        data_end_index = str(data).find("topsnapshot")
        
        data_array = str(data)[data_index:data_end_index]
        data_array = data_array.replace('firstchunkid":"1279292193","firstchunk":',"")
        data_array = data_array.replace('null','None')
        data_array = data_array[:-2]
        pyArray = ast.literal_eval(data_array)
        pyArray = pyArray[0][1][4]
        
        
        
            
        result = []
        index = 0
        # sorting through the junk
        for i in pyArray:
            try:
                if type(i[3]) == list:
                    result.append(i[3][-1])
                else:
                    pass
                            
            except IndexError:
               pass
                
      
      
        
        
        
        mytime = time.strftime('%l:%M%p on %b %d, %Y')
        comments = result[-6]
        email = result[-7]
        delivery = result[-8]
        pages = result[-9]
        building = result[-10]
        description = result[-11]
        name = result[-12]
                
        return [name,building,delivery]
        
    
        

sheet = Sheets()
class Window(object):
    def __init__(self,interval):
        self.interval = interval
        self.last_update = Label(root,text="LAST UPDATE: %s" % time.strftime('%l:%M%p on %b %d, %Y'))
        self.last_update.pack()
        self.update()
    def update(self):
         
        self.last_update.destroy()
        self.last_update = Label(root,text="LAST UPDATE: %s" % time.strftime('%l:%M%p on %b %d, %Y'))
        self.last_update.pack()
        
        info = sheet.update_page()
        
        
        #info 0-7
        

        
        ### decide whether or not to play the image
        
        with open('new.txt','w') as new:
            new.write(str(info[0::7]))
        with open('old.txt','r') as old:
            old_info = old.readline()
        with open('new.txt','r') as new:
            new_info = new.readline()
        with open('old.txt','w') as old:
            old.write(str(info[0::7]))
            
        
        
        
        if old_info != new_info and can_notify:
            self.notify(info=info)
        
        
        
        root.after(self.interval,self.update)
    def notify(self,info):
        tkMessageBox.showinfo("New Print Request!", """Name:%s\nBuilding:%s\nDelivery:%s""" % (info[0],info[1],info[2]))
        root.update()
        
       
  
        
    
window = Window(interval=60000)
#interval is in milliseconds
can_notify = True

root.mainloop()



        