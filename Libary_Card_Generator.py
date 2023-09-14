import tkinter
import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk,Image
from ttkbootstrap.constants import *
class Generator():
    def __init__(self):
        self.window = ttk.Window(themename="vapor")
        self.window.geometry("600x600")
        self.window.title("Card-Generator")
        self.window.resizable(0,0)
        image = tk.PhotoImage(file="4-penguin-png-image.png")
        background_label = ttk.Label(self.window, image=image)
        background_label.image=image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.display_labels=self.create_label()



    def create(self):
        global topLevel
        topLevel=tkinter.Toplevel(self.window)
        self.window.withdraw()
        topLevel.title("Retrieve password")
        topLevel.geometry("600x600")
        topLevel.resizable(0,0)
        try:
            with open("user-card","r") as f:
                content=f.read()
            image=ImageTk.PhotoImage(Image.open("Screenshot 2023-09-14 182910.png"))
            label=ttk.Label(topLevel,text=content,foreground="lightblue",font=("Helvetica",23),image=image,compound=tk.CENTER )
            label.image=image
            label.text=content
            label.compound=tk.TOP
            label.pack(ipadx=400,ipady=250,padx=0)
        except FileNotFoundError:
            image = ImageTk.PhotoImage(Image.open("Screenshot 2023-09-14 182910.png"))
            label = ttk.Label(topLevel, text="You do not have a saved card", foreground="lightblue", font=("Helvetica", 23), image=image,
                              compound=tk.CENTER)
            label.image = image
            label.compound = tk.TOP
            label.pack(ipadx=400, ipady=250, padx=0)
        topLevel.protocol("WM_DELETE_WINDOW", self.call)

    def call(self):
        global topLevel
        topLevel.destroy()
        self.window.deiconify()
        self.window.attributes("-topmost", 1)








    def generate(self):
        global entry
        val=entry.get()
        try:
            with open("user-card","r") as f:
             if f.read():
                 return
        except FileNotFoundError:
            if val:
                new = str(hash(val))
                list1=["67"]
                for i in range(0,len(new)-1,1):
                    try:
                        list1.append(chr(int(new[i]+new[i+1])))
                    except:
                        continue
                list2=list(filter(lambda x: x.isalpha(),list1))
                new="".join(list2) + new[7:]+new[:3]
                print(new)
                with open("user-card", "w") as f:
                    f.write(new)

    def create_label(self):
        global value
        global entry
        value=tk.StringVar()
        label=ttk.Label(self.window,text="Welcome to Card Generator",font=("Arial",24,"bold","italic"),wraplength=400,justify="center")
        label.grid(row=0,column=0,padx=120,ipady=10)
        label2 = ttk.Label(self.window, text="Would you like to retrieve card number?", font=("Arial", 12))
        label2.grid(row=1, column=0,sticky=tk.W,pady=(20,20),padx=120)
        checkbutton=ttk.Checkbutton(self.window,variable=value,command=self.create,text="Click Here")
        checkbutton.grid(row=2,column=0,pady=(20,50))

        label3=ttk.Label(self.window, text="Create a new card?", font=("Arial", 20,"bold","italic"))
        label3.grid(row=3, column=0,sticky=tk.W,pady=10,padx=120,ipadx=25,ipady=10)
        label3 = tk.Label(self.window, text="Enter your national-id number:",font=("Arial", 12))
        label3.grid(row=4, column=0,sticky=tk.W,padx=120)
        entry=tk.Entry(self.window,justify=tk.CENTER,show="*")
        entry.grid(row=5,column=0,sticky=tk.W,columnspan=3,ipadx=100,padx=120)

        button=tk.Button(self.window,text=" Create ➜ ",command=self.generate,font=("Times",20) )
        button.grid(row=6,column=0,sticky=tk.W,padx=120,pady=30,ipadx=20,ipady=10)

        return label,label2



    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    generate=Generator()
    generate.run()