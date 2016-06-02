#coding=utf-8
import Tkinter,sys,time
class ScreenSaver():
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.wm_attributes('-topmost',1) #窗口置顶
        #label_text = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        label_text = ''
        self.label = Tkinter.Label(self.root, font = ("simhei", 30), text = label_text)
        self.duration = 5
    def setDuration(self, _duration):
        self.duration = _duration
    def run(self):
        self.root.minsize(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        self.root.config(bg = '#4169E1')
        self.label.place(anchor = 'center', relx = 0.5, rely = 0.45)
        self.label2 = Tkinter.Label(self.root, font = ("simhei", 30), text = '休息时间到了，起来活动一下吧')
        self.label2.place(anchor = 'center', relx = 0.5, rely = 0.55)
        top_title = self.root.winfo_toplevel()
        top_title.overrideredirect(True) #去掉标题边框
        self.trickit(self.duration)
        try:
            self.root.mainloop()
        except:
            pass
    def trickit(self,num):
        for j in range(num,0,-1):
            #self.Label1["text"]=j
            minutes = int(j / 60)
            seconds = j % 60
            label_text = str(minutes) + '分钟' + str(seconds) + '秒'
            #self.label["text"]= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            self.label["text"]= label_text
            self.root.update()
            time.sleep(1)
        self.root.quit
        self.root.destroy()
        del self.root #只有这一句能使窗口完全退出
#test
#screen_saver = ScreenSaver()
#screen_saver.run()

