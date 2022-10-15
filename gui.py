import tkinter as tk
from tkinter import ttk


def callback():
    print('Button callback')


def scale(i):
    g.set(int(scale.get()))

root = tk.Tk()
root.title('Free@Home_Vaari')

window_width = 600
window_height = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

style = ttk.Style(root)
root.tk.call('source', 'azuredark2/azuredark3.tcl')
style.theme_use('azure')

options = ['', 'OptionMenu', 'Value 1', 'Value 2']
a = tk.IntVar()
b = tk.IntVar()
b.set(1)
c = tk.IntVar()
d = tk.IntVar()
d.set(2)
e = tk.StringVar()
e.set(options[1])
f = tk.IntVar()
g = tk.IntVar()
g.set(75)
h = tk.IntVar()

# Frame height and widths locations used to locate button places
weather_width = (window_width/2) - 30
weather_height = 200
weather_x = 20
weather_y =10


temperature_width = (window_width/2) - 30
temperature_height = 200
temperature_x = ((window_width/2) + 10)
temperature_y =10

shade_width = (window_width - 40)
shade_height = 200
shade_x = 20
shade_y =weather_y + weather_height +10

lights_width = (window_width - 40)
lights_height = 200
lights_x = 20
lights_y =shade_y + shade_height +10



# Lists:

test_shade = [1,2,3]
test_lights = [1,2,3,4,5,6,7,8,9,10,11,12]


# Weather info
frame1 = ttk.LabelFrame(root, text='Weather', width=weather_width, height=weather_height)
frame1.place(x=weather_x, y=weather_y)

frame2 = ttk.LabelFrame(root, text='Temperature', width=((window_width/2) - 30), height=temperature_height)
frame2.place(x=temperature_x , y=temperature_y)


frame3 = ttk.LabelFrame(root, text='Shades', width=shade_width, height=shade_height)
frame3.place(x=shade_x, y=shade_y)

frame4 = ttk.LabelFrame(root, text='Lights', width=lights_width, height=lights_height)
frame4.place(x=lights_x, y=lights_y)


# Shade buttons
for shade in test_shade:
    scale = ttk.Scale(root, from_=0, to=100, variable=g, command=scale)
    scale.place(x=80, y=620)




progress = ttk.Progressbar(root, value=0, variable=g, mode='determinate')
progress.place(x=80, y=600)

scale = ttk.Scale(root, from_=0, to=100, variable=g, command=scale)
scale.place(x=80, y=620)

# Light Buttons
switch = ttk.Checkbutton(root, text='Toggle switch', style='Switch', variable=h, offvalue=0, onvalue=1)
switch.place(x=40, y=700)
switch.invoke()




#entry = ttk.Entry(root)
#entry.place(x=250, y=20)
#entry.insert(0, 'Entry')

#spin = ttk.Spinbox(root, from_=0, to=100, increment=0.1)
#spin.place(x=250, y=70)
#spin.insert(0, 'Spinbox')

#combo1 = ttk.Combobox(root, value=['Combobox', 'Editable item 1', 'Editable item 2'])
#combo1.current(0)
#combo1.place(x=250, y=120)

#combo2 = ttk.Combobox(root, state='readonly', value=['Readonly combobox', 'Item 1', 'Item 2'])
#combo2.current(0)
#combo2.place(x=250, y=170)



root.mainloop()