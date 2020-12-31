import sys
import json
dict = {}
def create(key,value):
    if (type(key)!=str):
        print('please enter key with string value')
    elif (len(key)>32):
        print('please enter value of key within 33 characters')
    elif (sys.getsizeof(value)>16*1024):
        print('please enter value within 16kb')        
    elif (key  in dict):
        print('please enter unique key')
    else:
        dict[key] = value
        j = json.dumps(dict)
        with open('record.json','w') as f:
            f.write(j)
            #print(dict)

def read(key):
            with open('record.json','r') as r:
                data = json.load(r)
                if (key in data):
                    print(key+ ": " +str(data[key]))
                else:
                    print('key is not present') 
            
def delete(key):
    with open('record.json','r') as r:
            data = json.load(r)
            if (key in data):
                data.pop(key)
                j = json.dumps(data)
                with open('record.json','w') as f:
                    f.write(j)
            else:
                print('key is not present') 

