from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader #pip install pyPDF2
import os

root=Tk()
root.title("pdf protector")
root.geometry("600x430+300+100")
root.resizable(False,False)


def browse():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select Image File",
                                        filetype=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END,filename)

def Protect():
    mainfile = source.get()
    protectfile = target.get()
    code = password.get()

    if mainfile == "" or protectfile == "" or code == "":
        messagebox.showerror("Invalid", "All entries are empty!!")
    elif not mainfile.endswith('.pdf'):
        messagebox.showerror("Invalid", "Please select a valid PDF file!!")
    elif not protectfile.endswith('.pdf'):
        messagebox.showerror("Invalid", "Please select a valid PDF file!!")
    else:
        try:
            out = PdfWriter()
            file = PdfReader(mainfile, 'rb')
            num = len(file.pages)
            print(num)
            for idx in range(num):
                page = file.pages[idx]
                out.add_page(page)

            # password
            out.encrypt(str(code))

            with open(protectfile, "wb") as f:
                out.write(f)

            messagebox.showinfo("Success", "PDF file protected successfully!!")

        except Exception as e:
            #messagebox.showerror("Invalid", e)
            raise(e)




#icon
image_icon=PhotoImage(file=r"icon.png")
root.iconphoto(False,image_icon)

#main
Top_image=PhotoImage(file=r"top_image.png")
Label(root,image=Top_image).pack()

frame=Frame(root,width=580,height=290,bd=5,relief=GROOVE)
frame.place(x=10,y=130)


###########
source=StringVar()
Label(frame,text="Source PDF File:",font="arial 10 bold",fg="#4c4542").place(x=30,y=50)
entry1=Entry(frame,width=30,textvariable=source,font="arial 15",bd=1)
entry1.place(x=150,y=48)

Button_icon=PhotoImage(file=r"pngwing.com.png")
Button(frame,image=Button_icon,width=35,height=24,bg="#d3cdcd",command=browse).place(x=500,y=50)

###########
target=StringVar()
Label(frame,text="Target PDF File:",font="arial 10 bold",fg="#4c4542").place(x=30,y=100)
entry2=Entry(frame,width=30,textvariable=target,font="arial 15",bd=1)
entry2.place(x=150,y=100)

###########
password=StringVar()
Label(frame,text="set user password:",font="arial 10 bold",fg="#4c4542").place(x=15,y=150)
entry3=Entry(frame,width=30,textvariable=password,font="arial 15",bd=1)
entry3.place(x=150,y=150)


button_icon=PhotoImage(file=r"protected.png")
Protect=Button(root,text="Protect PdF File",compound=LEFT,image=button_icon,width=400,height=40,bg="#bfb9b9",font="arial 14 bold",command=Protect)
Protect.pack(side=BOTTOM,pady=40)



root.mainloop( )