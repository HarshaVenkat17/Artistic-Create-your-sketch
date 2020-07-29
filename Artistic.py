
import cv2
import tkinter as tk

class Artistic(object):
    def __init__(self, master, **kwargs):
        l1=tk.Label(text="Artistic",font=("Lucida Handwriting",100,"bold"),activeforeground="black",fg="black",bg="yellow")
        l1.place(x=440,y=30)
        l2=tk.Label(text="Let your child colour the picture of his choice",font=("Segoe Print",30,"bold"),activeforeground="black",fg="black",bg="yellow")
        l2.place(x=280,y=180)
        l3=tk.Label(text="Select Image",font=("Segoe Print",22,"bold"),activeforeground="black",fg="black",bg="yellow")
        l3.place(x=110,y=340)
        btn3 = tk.Button(root, text="Browse", bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",12,'bold'), command=lambda:self.open_img(textBox))
        btn3.place(x=1095,y=460)
        textBox = tk.Text(height =3, width =70,relief="sunken",bd=5,font=("Helvetica",18))
        textBox.configure(state='disabled')
        textBox.place(x=320,y=330)
                
        btn4 = tk.Button(root, text="Get sketch", bd=5,activeforeground="#ffffff",activebackground="violet",
                         fg="white",bg="#ed91af",width=12, height=1,font=("verdana",15,'bold'), command=self.perform)
        btn4.place(x=110,y=530)

    def perform(self):
        try:
            f=root.filename
            image = cv2.imread(f)
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2LUV)
            blur3= cv2.bilateralFilter(gray,9,5,30)
            edged3 = cv2.Canny(blur3,100,180)
            thresh3= cv2.threshold(edged3,100, 255, cv2.THRESH_BINARY_INV)[1]
            cv2.imwrite(f[:f.rfind(".")]+"(1).png",thresh3)
        except:
            pass
        
    def open_img(self,textBox2):
        root.filename =  tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg")))
        textBox2.configure(state='normal')
        textBox2.delete("1.0","end")
        textBox2.insert('end',root.filename)
        textBox2.configure(state='disabled')
root=tk.Tk()
root.title("Artistic: Colour your favourite characters")
pad=10
root._geom='1300x600+0+0'
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-pad,root.winfo_screenheight()-pad))
root.resizable(width = True, height = True) 
root.configure(bg="#fbff12")
app=Artistic(root)
root.mainloop()

