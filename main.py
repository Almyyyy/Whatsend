from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import *
from methods import *



    # init window #
window = Tk()
window.title("Whatsend v0.3 - prerelease") #window name
window.resizable(False, False) #block window resizing
tab_control = ttk.Notebook(window) #create tabs inside window






    # positioning objects #

#init first tab
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Main')

#label
lbl1 = Label(tab1, text="Select phone numbers file")
lbl1.grid(column=0, row=0, sticky="w")

#file directory text box
filedir = Entry(tab1, width=30) #text entry 
filedir.grid(column=0, row=1) #position of the objects

#choose file button
def choose_file():
    window.filename =  filedialog.askopenfilename(title = "Seleziona un file .txt", filetypes = (('text files', 'txt'),))
    filedir.config(state=NORMAL)
    
    filedir.delete(0, END)
    filedir.insert(0, window.filename)
    filedir.config(state=DISABLED)
    

filebtn = Button(tab1, text="Choose file", width=10, command=choose_file)
filebtn.grid(column=1, row=1)
filedir.config(state=DISABLED)



#space
space1 = Label(tab1)
space1.grid(column=0, row=2)



#label
lbl2 = Label(tab1, text="Write the message")
lbl2.grid(column=0, row=3, sticky="w")

#text area
txt = scrolledtext.ScrolledText(tab1, width=50, height=3)
txt.grid(column=0, row=4, columnspan=2)



#space
space2 = Label(tab1)
space2.grid(column=0, row=5)



#start button
def start():
    if not filedir.get() or len(txt.get("1.0", "end-1c")) == 0:
        print("not ok")
        #startbtn["state"] = "disabled"
    else:
        vai(filedir.get(), txt.get("1.0", "end-1c"));
        print(filedir.get())
        print(txt.get("1.0", "end-1c"))
        #startbtn["state"] = "normal"

startbtn = Button(tab1, text="Start", width=10, command=start)
startbtn.grid(column=0, row=6, columnspan=2)



#space
space3 = Label(tab1)
space3.grid(column=0, row=7)

bar = Progressbar(tab1, length=350)
bar.grid(column=0, row=8, columnspan=2)
bar['value'] = 20




#init second tab
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='About')



_license = scrolledtext.ScrolledText(tab2, width=50, height=20)
#txt.configure(background='#f1f1f1')
_license.insert(INSERT, 
"""
MIT License
Copyright (c) 2021 Giovanni Almirante
""")
_license.grid(column=0, row=4, columnspan=2)
_license.configure(state ='disabled')






tab_control.pack(expand=1, fill='both')



    # end of program #
window.mainloop()