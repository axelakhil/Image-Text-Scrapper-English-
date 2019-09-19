from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
import pytesseract
from tkinter.filedialog import askopenfilename
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

##### function to copy to clipboard

def copy():
    window.clipboard_clear()  # clear clipboard contents
    window.clipboard_append(resultpath.get(1.0,END))
    tkinter.messagebox.showinfo("success", "text copied successfully")

###function to show image using Imagetk.Photoimage

def show():
    root=Tk()
    root.title("IMAGE")
    root.geometry("600x600+100+50")

    source= insertpath.get('1.0', 'end-1c')
    if source:
        try:
            img = Image.open(source)
            img = img.resize((500, 500), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img, master=root)

            panel = Label(root, image=img)
            panel.pack(side='bottom', fill='both', expand='yes')
        except:
            panel = Label(root, text="FILE DON'T EXIST")
            panel.pack()


    else:
        panel = Label(root, text="NO FILE HAS BEEN SELECTED")
        panel.pack()

    root.mainloop()


# function to browse the file copy the path to insertpath text box
def Openfile():
    FILEname = askopenfilename(initialdir="/",  filetypes =(("PNG File", "*.png"),("BMP File", "*.bmp"),("JPEG File", "*.jpg")) )
    insertpath.delete("1.0",END)
    insertpath.insert(END,FILEname)

#function to get the path from the insertpath and use tesseract to get the text and show it to resultpath

def Readimage():
        source = insertpath.get('1.0', 'end-1c')
        if source:
            try:
                image = Image.open(source)
                result = pytesseract.image_to_string(image, lang='eng')
                resultpath.delete('1.0', END)
                resultpath.insert(END, result)
            except:
                resultpath.delete('1.0', END)
                resultpath.insert(END, "FILE DOESN'T EXIST")

        elif source=="":
            resultpath.delete('1.0',END)
            resultpath.insert(END,"NO FILE IS SELECTED")


window=Tk()
window.title("IMAGE READER")
window.state('zoomed')
window.config(bg="#f2f2f2")
window.colormapwindows()

# the heading section@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
source=StringVar()
T=Label(window,text="WELCOME TO IMAGE READER",height=3,width=100,fg="white",bg="#000000",font=('Copperplate Gothic Bold',30))
T.pack()

#karambhommi section@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

mainframe=Frame(window,bg="#f2f2f2")
mainframe.place(relx=0.1,rely=0.58,anchor=(W))

######input section ##########################################

# inputlabel=Label(mainframe,text="INPUT IMAGE :",fg="blue",font=('Copperplate Gothic Bold',16),bg="#f2f2f2")
# inputlabel.grid(row=0,column=0,sticky=(W),pady=10)

pathlabel=Label(mainframe,text="INPUT IMAGE PATH:",fg="blue",font=('Copperplate Gothic Bold',16),bg="#f2f2f2")
pathlabel.grid(row=0,column=0)

insertpath=Text(mainframe,height=2,bd=4,font=('Copperplate Gothic Bold',10))
insertpath.grid(row=0,column=1,columnspan=2)

browse=Button(mainframe,text="BROWSE IMAGE",fg="white",font=('Copperplate Gothic Bold',13),bg="#000000",command=Openfile,cursor="hand2",activebackground="#3333ff")
browse.grid(row=0,column=3,sticky=(E),pady=10,padx=10)

#######RESULT SECTION ************************************

reslabel=Label(mainframe,text="RESULT TEXT :",fg="blue",font=('Copperplate Gothic Bold',16),bg="#f2f2f2")
reslabel.grid(row=2,column=0,sticky=(W),pady=60)

resultpath=Text(mainframe,height=10,bd=4,font=('Copperplate Gothic Bold',10))
resultpath.grid(row=2,column=1,columnspan=2,pady=60)

readimage=Button(mainframe,text="READ IMAGE",fg="white",font=('Copperplate Gothic Bold',13),bg="#000000",command=Readimage,cursor="hand2", activebackground="#3333ff")
readimage.grid(row=2,column=3,pady=60,padx=10,sticky=(E),ipadx=13)

show=Button(mainframe,text="SHOW IMAGE",bd=5,fg="white",font=('Copperplate Gothic Bold',13),bg="#000000",command=show,cursor="hand2", activebackground="#3333ff")
show.grid(row=3,column=1,padx=6,sticky=(E),ipadx=10)

copyy=Button(mainframe,text="COPY TEXT",bd=5,fg="white",font=('Copperplate Gothic Bold',13),bg="#000000",command=copy,cursor="hand2", activebackground="#3333ff")
copyy.grid(row=3,column=2,padx=6,sticky=(W),ipadx=10)

window.mainloop()
