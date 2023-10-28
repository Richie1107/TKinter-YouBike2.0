import tkinter as tk
import Function
#%% function
def _add_clear():
    listBox.delete(0,"end")
    _add()

def _add():
    global siteName , roadName , SerchList , update_time , time , point ,\
           cityName
    
    cityName = value.get()
    siteName = Entrysite.get()
    roadName = Entryroad.get()    
    if siteName == '' and roadName == '':
        listBox.insert(0,'請輸入站名or路名查詢')
    else:
        SerchList=Function._judgeCity(cityName,siteName,roadName)            
        SerchList=[list(row) for row in SerchList]
        point = int(len(SerchList[0])/5)
        time = ''.join(SerchList[1])
        update_time = '更新時間:' + time + '\n共' + str(point) + '筆資料'
        for row in SerchList[0]:
            listBox.insert(tk.END,row)
        
    Label_update['text'] = update_time
    Entrysite.delete(0,'end')
    Entryroad.delete(0,'end')
    
#%% Win Basic parameter settings
wiN = tk.Tk()
wiN.title("共享單車查詢系統")
wiN.geometry("800x600+600+200")
wiN.iconbitmap('bikeimg.ico')
wiN.resizable(width=False, height=False)

#%%設定下拉選單
optionList = ['台北 Ubike','新北 Ubike','台中 Ubike']
value = tk.StringVar()
value.set('台北 Ubike')
menu = tk.OptionMenu(wiN, value, *optionList)
menu.config(width=20,height=2,fg='#6C6C6C')
menu.pack()

#%%文字輸入
Labelsite = tk.Label(wiN,text='請輸站名:',font=('Arial',12,'bold'))
Labelsite.pack() 
Entrysite=tk.Entry(wiN,font=("Arial",16),bd=5)
Entrysite.pack() 

Labelroad = tk.Label(wiN,text='輸入路名:',font=('Arial',12,'bold'))
Labelroad.pack() 
Entryroad=tk.Entry(wiN,font=("Arial",16),bd=5)
Entryroad.pack() 

Label_update = tk.Label(wiN,text='更新時間:',font=('Arial',10,'bold'))
Label_update.pack()
#%%按鈕
btnSerch = tk.Button(wiN, text="搜尋",fg="#5B5B5B", font=("Arial", 16), width=10, height=1 , command=_add_clear)
btnSerch.pack()

#%%顯示設定
sBar=tk.Scrollbar(wiN)
sBar.pack(side="right",fill="y")

listBox=tk.Listbox(wiN, font=("Arial", 20),yscrollcommand=sBar.set)
listBox.pack(side="bottom", fill="both")
sBar.config(command=listBox.yview)

#%%
wiN.mainloop()

