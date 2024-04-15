import tkinter
from PIL import ImageTk, Image
bg = "white"
fenetre = tkinter.Tk()
fenetre.title("My Mini Profile")
fenetre.config(bg=bg)
img = ImageTk.PhotoImage(Image.open("watermarked-files/img1.jpeg"))
mon_label = tkinter.Label(fenetre, image=img)
mon_label.pack()
fenetre.mainloop()