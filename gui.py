import tkinter as tk
from tkinter import ttk

from confiquration import heating_obj, light_obj, shades_obj, weather_obj, update


def callback():
    print('Button callback')



def toggle_light(light):
    light.toggle()
    update_gui()


def weather(weather_obj):
    weather_x = 20
    weather_y =10
    for data in weather_obj:
        label_name = ttk.Label(root,text=str(data.name.replace("_",' ')), font=("Helvetica",12))
        label_name.place(x= weather_x +10, y=weather_y +20)
        label_value = ttk.Label(root,text=data.value, font=("Helvetica",15))
        label_value.place(x= weather_x +195, y=weather_y +20)
        weather_y += 50

def set_heating(heating_obj):
    temperature_x = 310
    temperature_y = 10
    for heat in heating_obj:
        heat.button_plus = ttk.Button(root, text="+",command=lambda heat=heat: heat_up(heat),width=2)
        heat.button_plus.place(x=temperature_x + 130, y=temperature_y + 20)

        heat.button_minus = ttk.Button(root, text="-",command=lambda heat=heat: heat_down(heat),width=2)
        heat.button_minus.place(x=temperature_x + 225, y=temperature_y + 20)

        labelname_temperature = ttk.Label(root,text=heat.name.replace("controller",'').replace("contorller",''),font=("Helvetica",12))
        labelname_temperature.place(x= temperature_x + 10, y=temperature_y + 20)

        labelname_ctemperature = ttk.Label(root, text=heat.temperature, font=("Helvetica",20))
        labelname_ctemperature.place(x= temperature_x + 20, y=temperature_y + 40)

        labelname_ttemperature = ttk.Label(root,text=heat.target, font=("Helvetica",18))
        labelname_ttemperature.place(x= temperature_x + 170, y=temperature_y + 20)

        temperature_y += 60


def move_shade(shade, object):
    print((shade))
    print(object)
    shade.buttonvaluepos.set(object)
    #shade.move_position(object)
    #shade.move_position(shade.buttonvalueang)
    update_gui()

def angle_shade(shade, object):
    print((shade))
    print(object)
    shade.buttonvalueang.set(object)
    #shade.move_position(object)
    #shade.move_position(shade.buttonvalueang)
    update_gui()


def heat_up(heating):
    heating.target_up()
    update_gui()

def heat_down(heating):
    heating.target_down()
    update_gui()

def update_gui():
    update(light_obj, heating_obj, shades_obj, weather_obj)
    weather(weather_obj)
    set_heating(heating_obj)
    root.update()


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



# Weather info
weather(weather_obj)


# Temperature
set_heating(heating_obj)



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
    shade.buttonvaluepos = tk.IntVar()
    shade.buttonvaluepos.set(shade.position)
    shade.button1 = ttk.Scale(root, from_=0, to=100, variable=shade.buttonvaluepos,command=lambda position=shade.buttonvaluepos: move_shade(shade,position), orient=tk.HORIZONTAL, length=100) #orient=tk.VERTICAL
    shade.button1.place(x= x1, y=shade_y+(shade_height/2))

    print(shade.button1.get())
    print(shade.buttonvaluepos.get())
    print(type(shade))


    label_name2 = ttk.Label(root,text='Angle')
    label_name2.place(x= x1, y=y_shade + 20)
    label02 = ttk.Label(root,text='/')
    label02.place(x= x1-10, y=shade_y+(shade_height/2)+40)
    label03 = ttk.Label(root,text="\\")
    label03.place(x= x1+105, y=y_shade+40)

    shade.buttonvalueang = tk.IntVar(master=root, value=shade.angle)
    shade.button2 = ttk.Scale(root, from_=0, to=100, variable=shade.buttonvalueang, command=lambda angle=shade.buttonvalueang: angle_shade(shade, angle), orient=tk.HORIZONTAL, length=100) #orient=tk.VERTICAL
    shade.button2.place(x= x1, y=shade_y+(shade_height/2)+40)
    x1 += shade_width/(len(test_shade)+1)
    i += 1



# Light Buttons

x1 =lights_x +30
divide = 0
y1 = lights_y + 30

for light in light_obj:
    light.buttonvalue = tk.IntVar(master=root, value=light.value)
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




root.mainloop()
