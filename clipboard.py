import os
from time import sleep

def macSetClipboard(text):
    outf = os.popen('pbcopy', 'w')
    outf.write(text)
    outf.close()

def macGetClipboard():
    outf = os.popen('pbpaste', 'r')
    content = outf.read()
    outf.close()
    return content
clipboardHistory = [""] *  10
counter = 0
listBoxNumber = 1
import tkinter
top = tkinter.Tk()
def loop():
    global counter
    global listBoxNumber
    top.after(1000, loop) 
    value = macGetClipboard()
    if(value not  in clipboardHistory):                        
        if (counter == 10):                
            counter = -1
        clipboardHistory[counter] = value
        Lb1.insert(listBoxNumber, value)
        listBoxNumber += 1
        counter = counter + 1
    
        


Lb1 = tkinter.Listbox(top)
def helloCallBack():
    index = Lb1.curselection()
    value = Lb1.get(index)
    macSetClipboard(value)


B = tkinter.Button(top, text ="COPY", command = helloCallBack)



Lb1.pack()
B.pack()
top.after(1000, loop)
top.title("CLIPBOARDER")
top.mainloop()
