import tkinter as tk
from tkinter import ttk

import confiquration
from confiquration import heating_obj, light_obj, shades_obj, update


def callback():
    print('Button callback')


def scale(i):
    g.set(int(scale.get()))


def toggle_light(light):
    light.toggle()
    update(light_obj, heating_obj, shades_obj)
    print(light.value)
    light.buttonvalue.set(light.value)
    root.update()


def toggle_test(shade):
    #light.toggle()
    update(light_obj, heating_obj, shades_obj)
    shade.buttonvalue.set(shade.value)
    #light.toggle()

    #print('Button callback ' +str(light.buttonvalue)+" "+str(light.value)+" "+str(light.name))
    #print(type(value_dict[light.name].get()))
    #light.status()


#    light.toggle()



root = tk.Tk()
root.title('Free@Home_Vaari')
#root.resizable(False, False)

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
lights_height =60 + 60 * ((len(light_obj)//5)+1)
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
x1 = (shade_width/(len(test_shade)+1)) -50 +shade_x
y_shade = shade_y+(shade_height/2)
d = {}
i = 0
test = 0
#light.buttonvalue = tk.IntVar()
#light.buttonvalue.set(light.value)
#light.button = ttk.Checkbutton(root, style='Switch', variable=light.buttonvalue,command=lambda light=light: toggle_light(light), offvalue=0, onvalue=1)
#light.button.place(x=x1, y=y1)




for shade in shades_obj:
    label_name = ttk.Label(root,text=str(shade.name))
    label_name.place(x= x1, y=y_shade - 20)
    label0 = ttk.Label(root,text='0')
    label0.place(x= x1-10, y=shade_y+(shade_height/2))
    label100 = ttk.Label(root,text='100')
    label100.place(x= x1+100, y=y_shade)
    shade.button = ttk.Scale(root, from_=0, to=100, variable=shade.buttonvalue, command=scale,orient=tk.HORIZONTAL, length=100) #orient=tk.VERTICAL
    shade.button.place(x= x1, y=shade_y+(shade_height/2))


    label_name2 = ttk.Label(root,text='Angle')
    label_name2.place(x= x1, y=y_shade + 20)
    label02 = ttk.Label(root,text='/')
    label02.place(x= x1-10, y=shade_y+(shade_height/2)+40)
    label03 = ttk.Label(root,text="\\")
    label03.place(x= x1+105, y=y_shade+40)
    d["angle{0}".format(shade)] = ttk.Scale(root, from_=0, to=100, variable=test, command=test,orient=tk.HORIZONTAL, length=100) #orient=tk.VERTICAL
    d["angle{0}".format(shade)].place(x= x1, y=shade_y+(shade_height/2)+40)
    x1 += shade_width/(len(test_shade)+1)
    i += 1

value_dict = {}

x1 =lights_x +30
divide = 0
y1 = lights_y + 30

buttons = []
for light in light_obj:
    light.buttonvalue = tk.IntVar()
    light.buttonvalue.set(light.value)
    light.button = ttk.Checkbutton(root, style='Switch', variable=light.buttonvalue,command=lambda light=light: toggle_light(light), offvalue="0", onvalue="1")
    light.button.place(x=x1, y=y1)

    #Put name of button about middle of switch
    removed = light.name.replace("Light",'').strip().replace(" ",'\n').capitalize()
    adapt = 0



    labelname3 = ttk.Label(root,text=str(removed))
    labelname3.place(x= x1 - adapt, y=y1+25)
    x1 += 115   #150
    divide +=1
    if divide % 5 == 0:
        y1 += 70
        x1 =lights_x +30




#toggle = ttk.Checkbutton(root, text='Toggle button', style='Togglebutton', variable=f, offvalue=0, onvalue=1)
#toggle.place(x=250, y=420)



#    x_icon =x1 + 100/4
#    z = 0
#    for times in range(1-5):
#        progress = ttk.Progressbar(root, value=0, variable=shade, mode='determinate', orient='vertical', length=50)
#        progress.place(x=x_icon, y=200)
#        z += 10


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
