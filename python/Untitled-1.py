from tkinter import *

pro = Tk()

pro.geometry('500x500+900+100')

pro.resizable(False,True) 

pro.title('NASHAWN') #teitel

pro.config(background='gray')

pro.iconbitmap('C:\\Users\\nashwan\\Desktop\\python\\summer_sunny_sun_weather_forecast_sky_bright_icon_253959.ico')
'''
sc1 = Scale(pro, from_=1 , to= 100 , orient=HORIZONTAL)
sc1.pack()

sc2 = Scale(pro, from_=1 , to= 100 , orient=VERTICAL)
sc2.pack()

sc3 = Scale(pro, from_=1 , to= 100 , orient=VERTICAL)
sc3.place(x=10,y=10)


cs_baar1 = Scrollbar(pro, orient=VERTICAL)
cs_baar1.pack(side=RIGHT,fill=Y)

cs_baar2 = Scrollbar(pro, orient=HORIZONTAL)
cs_baar2.pack(side=BOTTOM,fill=X)
'''
nb = ttk.Notebook(pro)
nb.pack()

f1 = Frame(nb)
nb.add(f1,Text='tools',)
f2 = Frame(nb)




pro.mainloop()



