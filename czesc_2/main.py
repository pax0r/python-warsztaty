import tkinter
import waz


class MainWindow(tkinter.Frame):
    CANVAS_WIDTH = 500
    CANVAS_HEIGHT = 500

    def __init__(self, root):
        super().__init__(root)

        self.label = tkinter.Label(self, text="Waz szuka jedzonka")
        self.label.pack()

        self.canvas = tkinter.Canvas(self, width=self.CANVAS_WIDTH,
                                     height=self.CANVAS_HEIGHT)
        self.canvas.pack()

        self.przycisk_losuj = tkinter.Button(self, text="Losuj", command=self.losuj)
        self.przycisk_losuj.pack()
        self.przycisk_idz = tkinter.Button(self, text="Idz", command=self.zrob_krok)
        self.przycisk_idz.pack()
        self.przycisk_czysc = tkinter.Button(self, text="Czysc", command=self.czysc_plansze)
        self.przycisk_czysc.pack()

        self.waz = None
        self.jedzonko = None
        self.losuj()

    def losuj(self):
        self.waz = waz.Waz.losuj_punkt(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.jedzonko = waz.Punkt.losuj_punkt(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.narysuj_weza()
        self.narysuj_jedzonko()

    def narysuj_weza(self):
        self.canvas.create_rectangle(self.waz.x, self.waz.y, self.waz.x, self.waz.y,
                                     outline='blue')

    def narysuj_jedzonko(self):
        self.canvas.create_rectangle(self.jedzonko.x, self.jedzonko.y,
                                     self.jedzonko.x, self.jedzonko.y,
                                     outline='red')

    def zrob_krok(self):
        if self.waz.x != self.jedzonko.x or self.waz.y != self.jedzonko.y:
            self.przycisk_czysc["state"] = tkinter.DISABLED
            self.przycisk_idz["state"] = tkinter.DISABLED
            self.przycisk_losuj["state"] = tkinter.DISABLED
            self.waz.zrob_krok(self.jedzonko)
            self.narysuj_weza()
            self.after(20, self.zrob_krok)
        else:
            self.przycisk_czysc["state"] = tkinter.ACTIVE
            self.przycisk_idz["state"] = tkinter.ACTIVE
            self.przycisk_losuj["state"] = tkinter.ACTIVE

    def czysc_plansze(self):
        self.canvas.delete('all')


if __name__ == '__main__':
    root = tkinter.Tk()
    main = MainWindow(root)
    main.pack()
    root.mainloop()

