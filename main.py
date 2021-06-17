# -*- coding:utf8 -*-
#!bin/python3

import wx

class calculator(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "caluator", size=(350,480))

        self.operator = ""
        self.flag = 0

        ## Menu ##
        menu_file  = wx.Menu()
        menu_exit  = menu_file.Append(wx.ID_EXIT, "Exit")

        menu_bar = wx.MenuBar()
        menu_bar.Append(menu_file, "&File")
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.OnExit, menu_exit)




        ## main ##
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.textctrl = wx.TextCtrl(self, wx.ID_ANY, "0", style = wx.TE_RIGHT | wx.TE_READONLY)
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.textctrl.SetFont(font)

        
        self.panel = wx.Panel(self, -1)
        sizer = wx.GridSizer(5,4,10,10)
        
        self.Button_AC = wx.Button(self.panel, -1, "AC")
        sizer.Add(self.Button_AC, 1, wx.GROW)
        self.Button_AC.Bind(wx.EVT_BUTTON, self.OnAC)
        #self.Bind(wx.)

        self.panel_space1 = wx.Panel(self.panel, -1)
        sizer.Add(self.panel_space1, 1, wx.GROW)
        self.panel_space2 = wx.Panel(self.panel, -1)
        sizer.Add(self.panel_space2, 1, wx.GROW)

        self.Button_div = wx.Button(self.panel, -1, "÷")
        sizer.Add(self.Button_div, 1, wx.GROW)
        self.Button_div.Bind(wx.EVT_BUTTON, self.OnDivision)

        self.Button_1 = wx.Button(self.panel, -1, "1")
        sizer.Add(self.Button_1, 1, wx.GROW)
        self.Button_1.Bind(wx.EVT_BUTTON, lambda event, arg="1": self.EnterNumber(event, arg))

        self.Button_2 = wx.Button(self.panel, -1, "2")
        sizer.Add(self.Button_2, 1, wx.GROW)
        self.Button_2.Bind(wx.EVT_BUTTON, lambda event, arg="2": self.EnterNumber(event, arg))

        self.Button_3 = wx.Button(self.panel, -1, "3")
        sizer.Add(self.Button_3, 1, wx.GROW)
        self.Button_3.Bind(wx.EVT_BUTTON, lambda event, arg="3": self.EnterNumber(event, arg))

        self.Button_times = wx.Button(self.panel, -1, "×")
        sizer.Add(self.Button_times, 1, wx.GROW)
        self.Button_times.Bind(wx.EVT_BUTTON, self.OnTimes)

        self.Button_4 = wx.Button(self.panel, -1, "4")
        sizer.Add(self.Button_4, 4, wx.GROW)
        self.Button_4.Bind(wx.EVT_BUTTON, lambda event, arg="4": self.EnterNumber(event, arg))

        self.Button_5 = wx.Button(self.panel, -1, "5")
        sizer.Add(self.Button_5, 1, wx.GROW)
        self.Button_5.Bind(wx.EVT_BUTTON, lambda event, arg="5": self.EnterNumber(event, arg))

        self.Button_6 = wx.Button(self.panel, -1, "6")
        sizer.Add(self.Button_6, 1, wx.GROW)
        self.Button_6.Bind(wx.EVT_BUTTON, lambda event, arg="6": self.EnterNumber(event, arg))
        
        self.Button_minus = wx.Button(self.panel, -1, "-")
        sizer.Add(self.Button_minus, 1, wx.GROW)
        self.Button_minus.Bind(wx.EVT_BUTTON, self.OnMinus)

        self.Button_7 = wx.Button(self.panel, -1, "7")
        sizer.Add(self.Button_7, 1, wx.GROW)
        self.Button_7.Bind(wx.EVT_BUTTON, lambda event, arg="7": self.EnterNumber(event, arg))

        self.Button_8 = wx.Button(self.panel, -1, "8")
        sizer.Add(self.Button_8, 1, wx.GROW)
        self.Button_8.Bind(wx.EVT_BUTTON, lambda event, arg="8": self.EnterNumber(event, arg))

        self.Button_9 = wx.Button(self.panel, -1, "9")
        sizer.Add(self.Button_9, 1, wx.GROW)
        self.Button_9.Bind(wx.EVT_BUTTON, lambda event, arg="9": self.EnterNumber(event, arg))

        self.Button_pum = wx.Button(self.panel, -1, "+")
        sizer.Add(self.Button_pum, 1, wx.GROW)
        self.Button_pum.Bind(wx.EVT_BUTTON, self.OnPlus)

        self.Button_0 = wx.Button(self.panel, -1, "0")
        sizer.Add(self.Button_0, 1, wx.GROW)
        self.Button_0.Bind(wx.EVT_BUTTON, lambda event, arg="0": self.EnterNumber(event, arg))
        
        self.Button_00 = wx.Button(self.panel, -1, "00")
        sizer.Add(self.Button_00, 1, wx.GROW)
        self.Button_00.Bind(wx.EVT_BUTTON, lambda event, arg="00": self.EnterNumber(event, arg))

        self.Button_point = wx.Button(self.panel, -1, ".")
        sizer.Add(self.Button_point, 1, wx.GROW)
        self.Button_point.Bind(wx.EVT_BUTTON, self.OnPoint)

        self.Button_equal = wx.Button(self.panel, -1, "=")
        sizer.Add(self.Button_equal, 1, wx.GROW)
        self.Button_equal.Bind(wx.EVT_BUTTON, self.OnEqual)
        
        self.panel.SetSizer(sizer)

        sizer1.Add(self.textctrl, 1, wx.GROW)
        sizer1.Add(self.panel, 5, wx.GROW)
        self.SetSizer(sizer1)


    def OnExit(self, event):
        self.Close()

    def EnterNumber(self, event, num):
        if (self.flag == 1):
            self.textctrl.SetValue("")
            self.flag = 0
        before_val = self.textctrl.GetValue()
        if (before_val == "0"):
            before_val = ""
        after_val = str(before_val) + str(num)
        self.textctrl.SetValue(after_val)

    def OnAC(self, event):
        self.before_term = ""
        self.operator = ""
        self.textctrl.SetValue("0")
        self.flag = 0
        self.Button_point.Enable()

    def OnPoint(self, event):
        before_val = self.textctrl.GetValue()
        after_val = str(before_val) + "."
        self.textctrl.SetValue(after_val)
        self.Button_point.Disable()

    def OnPlus(self, event):
        self.OnEqual(event)
        self.before_term = self.textctrl.GetValue()
        self.operator = "plus"
        self.flag = 1
        self.Button_point.Enable()

    def OnMinus(self, event):
        self.OnEqual(event)
        self.before_term = self.textctrl.GetValue()
        self.operator = "minus"
        self.flag = 1
        self.Button_point.Enable()

    def OnDivision(self, event):
        self.OnEqual(event)
        self.before_term = self.textctrl.GetValue()
        self.operator = "division"
        self.flag = 1
        self.Button_point.Enable()

    def OnTimes(self, event):
        self.OnEqual(event)
        self.before_term = self.textctrl.GetValue()
        self.operator = "times"
        self.flag = 1
        self.Button_point.Enable()

    def OnEqual(self, event):
        self.after_term = self.textctrl.GetValue()
        if (self.operator == "plus"):
            self.answer = float(self.before_term) + float(self.after_term)
            self.textctrl.SetValue(str(self.answer))
            self.operator = ""
        if (self.operator == "minus"):
            self.answer = float(self.before_term) - float(self.after_term)
            self.textctrl.SetValue(str(self.answer))
            self.operator = ""
        if (self.operator == "division"):
            self.answer = float(self.before_term) / float(self.after_term)
            self.textctrl.SetValue(str(self.answer))
            self.operator = ""
        if (self.operator == "times"):
            self.answer = float(self.before_term) * float(self.after_term)
            self.textctrl.SetValue(str(self.answer))
            self.before_term = self.answer
            self.operator = ""
        self.Button_point.Disable()


if __name__ == "__main__":
    application = wx.App(False)
    frame = calculator(None)
    frame.Show()
    application.MainLoop()
