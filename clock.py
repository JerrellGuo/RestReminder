#coding=utf-8
from Tkinter import *
import threading
from screensave import *
import datetime

root = Tk()
root.title('Time to rest')
root.geometry('500x150') #width*height
root.resizable(width = False, height = False) #限制改变窗口大小

frame = Frame(root, bg = '#4169E1')
frame.pack(expand = YES, fill = BOTH)

frame_up = Frame(frame, bg = '#4169E1')
frame_up.pack()

label_str ='每'
label_str.decode('utf-8')
label = Label(frame_up, bg = '#4169E1', text = label_str, font = ("simhei", 16))
label.pack(side = LEFT)

list1 = Listbox(frame_up)
list1_item = [0.5, 0.75, 1, 2, 3]
for item in list1_item:
	list1.insert(END, item)
list1.pack(side = LEFT)
list1.config(height = 1) #使得listbox只显示1行
list1.yview(2) #向下移动两个，移动到1，即默认为1小时
list1.select_set(2) #默认选中第二个，即1
remain_time = list1.get(list1.curselection()) #初始化距离下次休息的时间

scrollbar1 = Scrollbar(frame_up)
scrollbar1.pack(side = LEFT)
# attach list1 to scrollbar1
list1.config(yscrollcommand = scrollbar1.set)
scrollbar1.config(command = list1.yview)

#根据当前scroll坐标确定当前被选中的列表项，由于对scrollbar和listbox不熟悉，采用了比较笨的方法
def list1ScrollSelect(event):
    global remain_time
    index = float(scrollbar1.get()[0]) * 5 #由于列表长度为5，所以scrollbar1.get()[0]返回的值为0,0.2,0.4，0.6,0.8，*5转换为index
    index = int(index)
    list1.select_clear(0, 4) #清除之前所选项
    list1.select_set(index)
    remain_time = list1.get(list1.curselection())
    #print list1.get(list1.curselection())

def list1MouseSelect(event):
    global remain_time
    remain_time = list1.get(list1.curselection())
    #print list1.get(list1.curselection())

#添加scrollbar和listbox响应函数
scrollbar1.bind('<ButtonRelease-1>', list1ScrollSelect) 
list1.bind('<ButtonRelease-1>', list1MouseSelect)

labe2 = Label(frame_up, bg = '#4169E1', text = '小时休息', font = ("simhei", 16))
labe2.pack(side = LEFT)

list2 = Listbox(frame_up)
list2_item = [3, 5, 10, 15]
for item in list2_item:
	list2.insert(END, item)
list2.pack(side = LEFT)
list2.config(height = 1)
list2.select_set(0)
rest_time = list2.get(list2.curselection()) #初始化每次休息的时间

scrollbar2 = Scrollbar(frame_up)
scrollbar2.pack(side = LEFT)
# attach listbox to scrollbar
list2.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=list2.yview)

def list2ScrollSelect(event):
    global rest_time
    index = float(scrollbar2.get()[0]) * 4 
    index = int(index)
    print index
    list2.select_clear(0, 3)
    list2.select_set(index)
    rest_time = list2.get(list2.curselection())
    print list2.get(list2.curselection())

def list2MouseSelect(event):
    global rest_time
    rest_time = list2.get(list2.curselection())
    print list2.get(list2.curselection())

scrollbar2.bind('<ButtonRelease-1>', list2ScrollSelect)
list2.bind('<ButtonRelease-1>', list2MouseSelect)

labe3 = Label(frame_up, bg = '#4169E1', text = '分钟', font = ("simhei", 16))
labe3.pack(side = LEFT)

label4_str = StringVar()
label4_str.set('')
label4 = Label(frame, bg = '#4169E1', textvar = label4_str, font = ("simhei", 16))
label4.pack(side = TOP, pady = 10)
is_on = False #开关状态
call_id = 0
def callScreenSaver():
    global call_id
    #启动屏保
    screen_saver = ScreenSaver()
    screen_saver.setDuration(rest_time * 60)
    #screen_saver.setDuration(5)
    screen_saver.run()
    
    #如果提醒开启，启动下一次的屏保
    if is_on:
        remain_time_in_ms = int(remain_time * 3600 * 1000)
        #remain_time_in_ms = 10000
        call_id = root.after(remain_time_in_ms, callScreenSaver)
        #计算下次休息时间
        ltime = datetime.datetime.now() + datetime.timedelta(hours = remain_time)
        time_str = ltime.strftime('%H:%M:%S')
        label4_str.set('下次休息时刻:' + time_str)

def rest():
    global call_id
    changeButtonText()
    remain_time_in_ms = int(remain_time * 3600 * 1000)
    #remain_time_in_ms = 10000 
    if is_on:
        call_id = root.after(remain_time_in_ms, callScreenSaver)

button_var = StringVar()
button = Button(frame, textvariable = button_var, font = ("simhei", 16), command = rest) #创建button并绑定rest函数
button_var.set('ON')
button.pack(side = TOP, pady = 10)

#改变开关状态
def changeButtonText():
    global is_on
    if button_var.get() == 'ON':
        #ltime = time.localtime(time.time()) + datetime.timedelta(hours = 1)
        ltime = datetime.datetime.now() + datetime.timedelta(hours = remain_time)
        #print ltime
        time_str = ltime.strftime('%H:%M:%S')
        label4_str.set('下次休息时刻:' + time_str)
        button_var.set('OFF')
        is_on = True 
    else:
        print 'cancel'
        root.after_cancel(call_id)
        label4_str.set('')
        button_var.set('ON')
        is_on = False 

root.mainloop()

