from PIL import ImageTk, Image
import tkinter


def titleBar(topF):
    img = ImageTk.PhotoImage(Image.open(
        r"C:\Users\Admin\Downloads\fol\fol\iiit.jpg").resize((400, 120), Image.ANTIALIAS))
    logo = tkinter.Label(topF, bg="red", borderwidth=0,
                         image=img, height=120, width=400)
    logo.image = img
    logo.place(relx=0, rely=0)
