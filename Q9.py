'''

Assume any database includes below columns and you are requested to process Stats_Access_Link column and extract pure url information inside per device type. 

    Rules: 
-   Xml tags and protocol parts is guaranteed to be lower case  
-   Access link part that we are interested in can have alpha-numeric, case insensitive characters, underscore ( _ ) character and dot ( . ) character only.  

What would you use for this task, please write your detailed answer with exact solution? Please  provide the link to your code as answer to this question 

Example: for the device type AXO145, we would like to get xcd32112.smart_meter.com regardless from its access protocol is SSL secured or not.

'''


import re

database_records = [
    {"Device_Type": "AXO145", "Stats_Access_Link": "https://xcd32112.smart_meter.com/data"},
    {"Device_Type": "BZY987", "Stats_Access_Link": "http://abcd5678.smart_meter.com/info"},
    {"Device_Type": "AXO145", "Stats_Access_Link": "http://abcd1234.smart_meter.com/detail"},
    {"Device_Type": "CDE456", "Stats_Access_Link": "https://efg7890.smart_meter.com/page"},
    {"Device_Type": "FHI123", "Stats_Access_Link": "http://hij4567.smart_meter.com/home"}
]


pure_urls_per_device = {}


for record in database_records:
    device_type = record["Device_Type"]
    url = record["Stats_Access_Link"]
    match = re.search(r'(?<=://)[a-z0-9_.]+(?=/)', url, re.IGNORECASE)
    if match:
        pure_url = match.group(0)
        if device_type in pure_urls_per_device:
            pure_urls_per_device[device_type].append(pure_url)
        else:
            pure_urls_per_device[device_type] = [pure_url]

for device_type, urls in pure_urls_per_device.items():
    print(f"{device_type}: {urls}")




#outputs will be :

'''

AXO145: ['xcd32112.smart_meter.com', 'abcd1234.smart_meter.com']
BZY987: ['abcd5678.smart_meter.com']
CDE456: ['efg7890.smart_meter.com']
FHI123: ['hij4567.smart_meter.com']

'''
