import requests
import prettytable
import os
#from playsound import playsound
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import time
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict"

querystring = {"district_id": "395"}

language = 'en'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Host": "cdn-api.co-vin.in",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"

}
dates = ["12-05-2021","13-05-2021","14-05-2021","15-05-2021","16-05-2021"]
while True:
    table = prettytable.PrettyTable(["name", "id", "date", "capacity", "pincode"])
    try:
        for date in dates:
            querystring["date"] = date
            response = requests.request("GET", url,proxies=proxyDict, headers=headers, params=querystring, verify=False)
            data = response.json()
            for centers in data['centers']:
                if 'sessions' in centers.keys() and centers['sessions'] is not None:
                    if centers['sessions'][0]['min_age_limit'] == 18 and centers['sessions'][0][
                        'available_capacity'] > 0:
                        # myobj = gTTS(text=centers['name'], lang=language, slow=False)
                        # myobj.save('center.mp3')
                        table.add_row([centers['name'], centers['center_id'], centers['sessions'][0]['date'],
                                       centers['sessions'][0]['available_capacity'], centers['pincode']])
                        #print(table)
                        #playsound("cowin_alert.mp3")
                        # os.remove('center.mp3')
    except:
        pass

    print(table)
    time.sleep(0.5)
