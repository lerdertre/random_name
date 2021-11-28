from random import randint
import wx



class RandomName(wx.Frame):
    def __init__(self):
        super().__init__(None, title = '随机点名器', size = (600,400))
        panel = wx.Panel(parent = self)

        self.statictext = wx.StaticText(parent = panel,label = '点击下方按钮开始随机点名')
        button = wx.Button(parent = panel,label = '开始')
        self.Bind(wx.EVT_BUTTON,self.on_click,button)

        global random_name
        random_name = wx.StaticText(panel, label = '  ')
        random_name.SetFont(wx.Font(200,wx.SWISS,wx.NORMAL,wx.NORMAL))

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statictext,flag = wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border = 10)
        vbox.Add(random_name,proportion = 10,flag = wx.ALIGN_CENTRE,border = 10)
        vbox.Add(button,flag = wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM,border = 10)

        panel.SetSizer(vbox)

    def on_click(self,event):
        randnum = randint(1,64)
        if randnum < 10:
            randnum = '0'+str(randnum)
        else:
            randnum = str(randnum)
        random_name.SetLabel(randnum)



if __name__ == '__main__':
    app = wx.App()
    windows = RandomName()
    windows.Show()
    app.MainLoop()