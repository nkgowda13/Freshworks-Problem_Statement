gg#!/usr/bin/env python
# coding: utf-8

# In[126]:


import json
import threading
import time
data = {}
threads = {}
print('_____________________________________________________________________________________')

#-----------------------------------------------------------------------------------------------------------#

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        global threads
        global data
        print("Starting " + self.name)
        print_time(self.name, 1, self.counter)
        try :
            delete(threads[self.name])
        except:
            pass
        print("Exiting " + self.name)

#-----------------------------------------------------------------------------------------------------------#

def print_time(threadName, counter, delay):
    global threads
    global data
    while counter:
        time.sleep(delay)
        counter -= 1
    
#-----------------------------------------------------------------------------------------------------------#

def create(k,v,threadID,ttl) :
    global data
    global threads
    if len(k) > 32 :
        return print('Key is too big')
    if len(v) > 16000 :
        return print('Value is too big')
    try :
        data[k]
        return print('Key already exists')
    except :
        data[k] = v
        with open(location,'w') as f :
            f.write(json.dumps(data))
        name = 'thread' + str(threadID)
        threads[name] = k
        xd = myThread(threadID,name,ttl)
        xd.start()
                    
#-----------------------------------------------------------------------------------------------------------#

def read(k) :
    global data
    with open(location,'r') as f :
            print(json.load(f)[k])

#-----------------------------------------------------------------------------------------------------------#

def delete(k) :
    global data
    with open(location,'r') as f :
            x = json.load(f)
    x.pop(k)
    data.pop(k)
    with open(location,'w') as f :
            f.write(json.dumps(x))

#-----------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':

    print('FILE PATH')
    x = input()
    try :
        x = x + '/data.json'
        open(x,'r')
        location = x
    except :
        print('Location entered is INVALID')
        print('Taking Default Location')
        location = 'data.json'
    print('_____________________________________________________________________________________')

#-----------------------------------------------------------------------------------------------------------#

    print('TIME TO LIVE(in seconds)')
    try :
        ttl = int(input())
    except :
        print('INVALID INPUT')
        print('Default TTL - 300 seconds')
        ttl = 300
    
    print('_____________________________________________________________________________________')

#-----------------------------------------------------------------------------------------------------------#
    threadID = 1
    print('''The methods allowed are 1.create
                            2.read
                            3.delete
                            4.quit or exit''')
    while True :
        x = input()
        if x == 'quit' or x == 'exit' :
            break
        if 'create' in x :
            try :
                gg = x[7:-1]
                y = gg.split(',')
                create(y[0],y[1],threadID,ttl)
                threadID += 1
            except :
                print('INVALID INPUT')
                print('the format should be : create(key,value)')
        elif 'delete' in x :
            try :
                delete(x[7:-1])
            except :
                print('INVALID INPUT')
                print('The format should be : delete(key)')
        elif 'read' in x :
            try :
                read(x[5:-1])
            except :
                print('INVALID INPUT')
                print('The format should be : read(key)')
        else :
            print('Please provide a proper input')
            print('''The methods allowed are 1.create
                            2.read
                            3.delete
                            4.quit or exit''')
        print('_____________________________________________________________________________________')
    

