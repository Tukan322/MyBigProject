from tkinter import *


class Menu:

    def __init__(self):
        self.main = Tk()
        self.textFrame = Frame(self.main)
        self.textbox = Text()
        self.panelFrame = Frame(self.main)
        self.leftFrame = Frame(self.main)
        self.rightFrame = Frame(self.main)
        self.left_text = Text()
        self.right_text = Text()

    def options_return(self, *args):
        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, "returning to main menu")
        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.leftFrame.destroy()
        self.rightFrame.destroy()
        self.main_menu()

    def start_foo(self, *args):
        self.textbox.insert(1.0, "there should be start\n")
        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.battle_window()

    def collection_foo(self, *args):
        self.textbox.insert(1.0, "there should be collection\n")

    def options_foo(self, *args):
        self.textbox.delete(1.0, "end")
        self.textbox.insert(1.0, "there should be options")
        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.options_window()

    def GuiExit(self, *args):
        self.main.destroy()

    def main_menu(self):
        self.textFrame = Frame(self.main, height=100, width=1000, bg="gray")
        self.textFrame.pack(side="top", fill="x", expand=0)
        self.panelFrame = Frame(self.main, height=400, width=1000, bg="gray")
        self.panelFrame.pack(side="bottom", fill="both", expand=1)

        self.textbox = Text(self.textFrame, font="Arial 8", wrap="word")
        self.textbox.pack(fill="both")

        play = Button(self.panelFrame, text="Play")
        play.bind("<Button-1>", self.start_foo)
        play.place(x=0, y=0, width=1000, height=100)

        collection_button = Button(self.panelFrame, text="Collection")
        collection_button.bind("<Button-1>", self.collection_foo)
        collection_button.place(x=0, y=100, width=1000, height=100)

        options_button = Button(self.panelFrame, text="Options")
        options_button.bind("<Button-1>", self.options_foo)
        options_button.place(x=0, y=200, width=1000, height=100)

        exit_but = Button(self.panelFrame, text="Exit")
        exit_but.bind("<Button-1>", self.GuiExit)
        exit_but.place(x=0, y=300, width=1000, height=100)

        self.main.mainloop()

    def options_window(self):
        self.textFrame = Frame(self.main, height=100, width=1000, bg="gray")
        self.textFrame.pack(side="top", fill="both", expand=0)
        self.panelFrame = Frame(self.main, height=400, width=1000, bg="gray")
        self.panelFrame.pack(side="bottom", fill="both", expand=1)

        self.textbox = Text(self.textFrame, font="Arial 8", wrap="word")
        self.textbox.pack(fill="both")

        ret_but = Button(self.panelFrame, text="Return to main menu")
        ret_but.bind("<Button-1>", self.options_return)
        ret_but.place(x=0, y=0, width=1000, height=200)

        exit_but = Button(self.panelFrame, text="Exit")
        exit_but.bind("<Button-1>", self.GuiExit)
        exit_but.place(x=0, y=200, width=1000, height=200)

    def battle_window(self):
        self.textFrame = Frame(self.main, height=100, width=800, bg="gray")
        self.textFrame.pack(side="top", fill="both", expand=0)

        self.panelFrame = Frame(self.main, height=400, width=1000, bg="gray")
        self.panelFrame.pack(side="bottom", fill="both", expand=1)

        self.textbox = Text(self.textFrame, font="Arial 14", wrap="word", height=7, width=1)
        self.textbox.pack(fill="both")

        self.leftFrame = Frame(self.main, height=100, width=100, bg="gray")
        self.rightFrame = Frame(self.main, height=100, width=100, bg="gray")
        self.leftFrame.pack(side="left", fill="both", expand=1)
        self.rightFrame.pack(side="right", fill="both", expand=1)

        self.left_text = Text(self.leftFrame, font="Arial 14", wrap="word",  height=7, width=1)
        self.right_text = Text(self.rightFrame, font="Arial 14", wrap="word",  height=7, width=1)

        self.left_text.pack(fill="both")
        self.right_text.pack(fill="both")

        options_button = Button(self.panelFrame, text="main menu")
        options_button.bind("<Button-1>", self.options_return)
        options_button.place(x=0, y=300, width=1000, height=100)

