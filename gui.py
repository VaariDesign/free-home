import tkinter as tk


# Basic
window = tk.Tk()

# extra
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

# Temperatures
# Shades
# Lights

# Nappi
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 0.5}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 0.5}"

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")


#Frameja jaetaan pohja
frame1 = tk.Frame(master=window, width=200, height=100, bg="black")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="black")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


# Frameja tietyssä kohtaa

frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)


# Frameja liikkuu
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)


window.mainloop()
