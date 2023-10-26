from tkinter import *
def ok_gomb_megnyomasa():
    dolgozo_neve = nev.get()
    print(dolgozo_neve)
    nev.delete(0,END)


ablak = Tk()

ablak.title("Dolozó")
ablak.geometry("600x400")
szoveg = Label(ablak, text="Név:")
gomb_ok = Button(ablak, text="OK", command=ok_gomb_megnyomasa)
gomb_esc = Button(ablak, text="Mégse", command=ablak.destroy)
nev = Entry(ablak, width=30)

"""szoveg.pack()
nev.pack()
gomb_ok.pack()
gomb_esc.pack()"""

szoveg.place(x=50, y=10)
nev.place(x=100, y=10)


ablak.mainloop()

