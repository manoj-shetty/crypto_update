import wx
import threading
import requests
import time

class MyFrame(wx.Frame):    
    def __init__(self):
        self.status = True
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)    
        my_start_btn = wx.Button(panel, label='Start')
        my_stop_btn = wx.Button(panel, label='Stop')
        self.my_cryp_name = wx.Button(panel, label='Crypto Name: ')
        self.my_cryp_percentage = wx.Button(panel, label='Crypto Change Percenatge: ')
        self.my_cryp_price = wx.Button(panel, label='Crypto Price: ')
        my_start_btn.Bind(wx.EVT_BUTTON, self.on_start)
        my_stop_btn.Bind(wx.EVT_BUTTON, self.on_stop)
        my_sizer.Add(my_start_btn, 0, wx.ALL | wx.CENTER, 5)   
        my_sizer.Add(my_stop_btn, 0, wx.ALL | wx.CENTER, 5)   
        my_sizer.Add(self.my_cryp_name, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.my_cryp_percentage, 0, wx.ALL | wx.EXPAND, 5)
        my_sizer.Add(self.my_cryp_price, 0, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_start(self, event):
        self.status = True
        x = threading.Thread(target=self.get_price)
        x.start()
        # index = 0
        # while self.status:
        #     self.my_cryp_name.SetLabel(f'Crypto Name: "{index}"')
        #     self.my_cryp_percentage.SetLabel(f'Crypto Change Percenatge: "{index}"')
        #     index += 1
        #     print(index)

    def get_price(self):
        while self.status:
            rep = requests.get("https://api.binance.com/api/v3/ticker/24hr")
            max_change = 0.0
            print("Total number of coins:{}".format(len(rep.json())))
            max_change_crypto = ""
            last_price = 0.0
            for in_json in rep.json():
                try:
                    if "USDT" not in in_json["symbol"]:
                        continue
                    price_change = round(float(in_json["priceChangePercent"]), 2)
                    if price_change > max_change:
                        max_change = price_change
                        max_change_crypto = in_json["symbol"]
                        last_price = in_json["lastPrice"]
                except:
                    continue
            self.my_cryp_name.SetLabel(f'Crypto Name:  {max_change_crypto}')
            self.my_cryp_percentage.SetLabel(f'Crypto Change Percenatge: {max_change}')
            self.my_cryp_price.SetLabel(f'Crypto Price : {last_price}')
            time.sleep(3)
    
    def on_stop(self, event):
        self.status = False

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()