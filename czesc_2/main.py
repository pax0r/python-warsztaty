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


if __name__ == '__main__':
    root = tkinter.Tk()
    main = MainWindow(root)
    main.pack()
    root.mainloop()

