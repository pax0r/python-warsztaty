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
        self.waz = waz.Waz.losuj_punkt(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)
        self.jedzonko = waz.Punkt.losuj_punkt(self.CANVAS_WIDTH, self.CANVAS_HEIGHT)

        self.narysuj_weza()
        self.narysuj_jedzonko()

        self.zrob_krok()

    def narysuj_weza(self):
        self.canvas.create_rectangle(self.waz.x, self.waz.y, self.waz.x, self.waz.y,
                                     outline='blue')

    def narysuj_jedzonko(self):
        self.canvas.create_rectangle(self.jedzonko.x, self.jedzonko.y,
                                     self.jedzonko.x, self.jedzonko.y,
                                     outline='red')

    def zrob_krok(self):
        if self.waz.x != self.jedzonko.x or self.waz.y != self.jedzonko.y:
            self.waz.zrob_krok(self.jedzonko)
            self.narysuj_weza()
            self.after(20, self.zrob_krok)


if __name__ == '__main__':
    root = tkinter.Tk()
    main = MainWindow(root)
    main.pack()
    root.mainloop()

