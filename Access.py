import requests
import time
import os
from bs4 import BeautifulSoup
import ast
import re
from datetime import datetime

class Timer(object):
    def __init__(self,interval):
        self.interval = interval
        
        self.url = 'https://docs.google.com/spreadsheets/d/18py6NHCJipTqDTw2xncXgbUWlbQyK6rGmJFM6FHnG8I/edit?pli=1#gid=1279292193'
        
        self.user = 'icadetprintscraper@gmail.com'
        self.passw = 'iCadet_Print_Scraper'
        self.filename = 'raw_data.txt'
        
        print self.update_page() #change to update() later 
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
                
      
      
        
        
        
        time = datetime.utcnow()
        comments = result[-6]
        email = result[-7]
        delivery = result[-8]
        pages = result[-9]
        building = result[-10]
        description = result[-11]
        name = result[-12]
                
        info = "%s (%s) printed  '%s' from %s at %s. It consists of %s pages. %s. Comments: %s. " % (name,email,description,building,time,int(pages),delivery,comments)
        
        
        
            
        return info
            
        
            
            
 
    def update(self):
        new_text = self.update_page()
        
        with open('parsed.txt','r') as parseddoc:
            old_text = parseddoc.readline()
        
        if str(old_text) != str(new_text):
            print new_text, old_text
            
        with open('parsed.txt','w') as parseddoc:
            parseddoc.write(new_text)
        
        
    
        
        
        
        
timer = Timer(interval=30)
        