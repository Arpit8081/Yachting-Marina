from Tkinter import *
from tkFileDialog import askopenfilename

def sel():
	Lenght = float(var.get())
	rate = float(getTemp.get())
	print Lenght
	print rate
	print getTempN.get()
	values =str( Lenght * rate)
	ans.insert(INSERT, ( values))

def save():
  text = getTempN.get() + "," + getTemp.get() +  "," + ans.get() + "\n"
  with open("text.txt", "a") as f:
    f.write(text)
    print "file is a save."

def delete():
  getTemp.delete(0, END)
  getTempN.delete(0, END)
  ans.delete(0, END)
  print "delete successful"

def open2():
  name = askopenfilename(filetypes =(("Text File", ".txt"),("All Files","*.txt")),title = "Choose a file.")
  print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
  try:
      with open(name,'r') as UseFile:
        print(UseFile.read())
  except:
        print("No file exists")

win = Tk()
win.geometry('500x400')
hello = Label(master = win, text = 'Cardiff Yachting Marina',font=("Helvetica", 16), foreground="blue")
hello.pack(side=TOP)
askTemp = Label(master = win, text = 'Enter Your Name:')
askTemp.pack(side=TOP)
getTempN = Entry(win,width=40,bg="white")
getTempN.pack(side=TOP)
askTemp = Label(master = win, text = 'Enter the Yach Length in meters:')
askTemp.pack(side=TOP)
getTemp = Entry(win,width=40,bg="white")
getTemp.pack(side=TOP)
hour = Label(master = win, text = 'Rate for hourly ')
hour.pack(side=TOP)



var = IntVar()
R1 = Radiobutton(win, text="Hourly Rate: $0.50", variable=var, value=(0.50),
                  command=sel)
R1.pack( side=TOP)

R2 = Radiobutton(win, text="Daily Rate: $10.00", variable=var, value=(10.00),
                  command=sel)
R2.pack( side=TOP)

R3 = Radiobutton(win, text="Weekly Rate:  $60.00", variable=var, value=(60.00),
                  command=sel )
R3.pack( side=TOP)

R4 = Radiobutton(win, text="Monthly Rate: $180.00", variable=var, value=(180.00),
                  command=sel)
R4.pack( side=TOP)

R5 = Radiobutton(win, text="Annual Rate: $1320.50", variable=var, value=(1320.50),
                  command=sel )
R5.pack( side=TOP)


# Snip
a = Label(master = win, text = 'charge is')
a.pack(side=TOP)
ans = Entry(win,width=40,bg="white")
ans.pack(side=TOP)

B = Button(win, text="Save as a file", width=9, command=save)
B.pack()
D = Button(win, text="clear data", width=9, command=delete)
D.pack()
O = Button(win, text="open file", width=9, command=open2)
O.pack()
win.mainloop()