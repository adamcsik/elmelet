from tkinter import *
from tkinter import messagebox


"""def sugo():
    messagebox.showinfo("Súgó", "Lásd az interneten")

app = Tk()
app.title("Menüvezérelt program")

menusor = Menu()

menusor.add_command(label="Fájl", command=app.destroy)
menusor.add_command(label="Sűgó", command=sugo)
app.config(menu=menusor)

app.mainloop()"""

def megnyitas():
    messagebox.showinfo("Megnyitás", "Fájl open")


app = Tk()
app.title("Menüvezérelt program")

menusor = Menu(app)

fajl = Menu(menusor)
fajl.add_command(label="Megnyitás", command=megnyitas)
fajl.add_command(label="Kilépés", command=app.destroy)
menusor.add_cascade(label="Fájl", menu=fajl)

sugo = Menu(menusor)
sugo.add_command(label="Névjegy", command=app.destroy)
menusor.add_cascade(label="Súgó", menu=sugo)


app.config(menu=menusor)
app.mainloop()

