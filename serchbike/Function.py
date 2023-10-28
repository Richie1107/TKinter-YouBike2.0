def _TCC(siteName,roadName):    
    import requests  
    import json
    from datetime import datetime 
    global SerchList , update_time
    url="https://datacenter.taichung.gov.tw/swagger/OpenData/86dfad5c-540c-4479-bb7d-d7439d34eeb1"      
    data=requests.get(url).text 
    bikeList=json.loads(data)    
    bike=bikeList['retVal']
    
    SerchList=[]
    #設定更新時間
    date=bike[0]['mday']
    date_format='%Y%m%d%H%M%S'
    try:
        update_time=datetime.strptime(date, date_format)
    except ValueError:
       update_time = '查無更新時間'    
    
    if len(siteName)>0  :
        inputName = siteName
        for i in range(len(bike)):
            bike2=bike[i]
            if bike2['sna'].find(inputName) >= 0:
                SerchList.append('站名:'+bike2['sna'])
                SerchList.append('可借:'+bike2['sbi'])
                SerchList.append('可停:'+bike2['bemp'])
                SerchList.append('地址:'+bike2['ar'])
                SerchList.append('-'*40)
    else:
        inputName = roadName        
        for i in range(len(bike)):
            bike2=bike[i]
            if bike2['ar'].find(inputName) >= 0:
                SerchList.append('站名:'+bike2['sna'])
                SerchList.append('可借:'+bike2['sbi'])
                SerchList.append('可停:'+bike2['bemp'])
                SerchList.append('地址:'+bike2['ar'])
                SerchList.append('-'*40)
    

    return SerchList , str(update_time)

def _NTPC(siteName,roadName):
    import requests  
    import json
    from datetime import datetime 
    global SerchList , update_time

    url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1100"      
    data = requests.get(url).text
    bikeList = json.loads(data)
    bike = bikeList
    
    SerchList=[]
    #設定更新時間
    date=bike[0]['mday']
    date_format='%Y%m%d%H%M%S'
    try:
        update_time=datetime.strptime(date, date_format)
    except ValueError:
        update_time = '查無更新時間'
        
    if len(siteName)>0  :
        inputName = siteName
        for i in range(len(bike)):
            bike2=bike[i]
            if bike2['sna'].find(inputName) >= 0:
                SerchList.append('站名:'+bike2['sna'])
                SerchList.append('可借:'+bike2['sbi'])
                SerchList.append('可停:'+bike2['bemp'])
                SerchList.append('地址:'+bike2['ar'])
                SerchList.append('-'*40)
    else:
        inputName = roadName        
        for i in range(len(bike)):
            bike2=bike[i]
            if bike2['ar'].find(inputName) >= 0:
                SerchList.append('站名:'+bike2['sna'])
                SerchList.append('可借:'+bike2['sbi'])
                SerchList.append('可停:'+bike2['bemp'])
                SerchList.append('地址:'+bike2['ar'])
                SerchList.append('-'*40)
    
    return SerchList , str(update_time)

def _TPC(siteName,roadName):    
    import requests  
    import json
    from datetime import datetime 
    global SerchList , update_time

    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"      
    data = requests.get(url).text
    bikeList = json.loads(data)
    bike = bikeList
    
    SerchList=[]
    #設定更新時間
    date=bike[0]['mday'].replace('-','').replace(':','').replace(' ','')
    date_format='%Y%m%d%H%M%S'
    try:
        update_time=datetime.strptime(date, date_format)
    except ValueError:
        update_time = '查無更新時間'
        
    if len(siteName)>0  :
        inputName = siteName
        for i in range(len(bike)):
            bike2=bike[i]
            if bike2['sna'].find(inputName) >= 0:
                SerchList.append('站名:'+bike2['sna'])
                SerchList.append('可借:'+str(bike2['sbi']))
                SerchList.append('可停:'+str(bike2['bemp']))
                SerchList.append('地址:'+bike2['ar'])
                SerchList.append('-'*40)
    else:
        inputName = roadName        
        for i in range(len(bike)):
            bike2=bike[i]
            if bike2['ar'].find(inputName) >= 0:
                SerchList.append('站名:'+bike2['sna'])
                SerchList.append('可借:'+str(bike2['sbi']))
                SerchList.append('可停:'+str(bike2['bemp']))
                SerchList.append('地址:'+bike2['ar'])
                SerchList.append('-'*40)
    
    return SerchList , str(update_time)

def _judgeCity(cityName,siteName,roadName):
    global SerchList , update_time 
    if cityName in '台北 Ubike':
        _TPC(siteName, roadName)
        return SerchList , str(update_time)
    elif cityName in '新北 Ubike':
        _NTPC(siteName, roadName)
        return SerchList , str(update_time)
    else:
        _TCC(siteName, roadName)
        return SerchList , str(update_time)


