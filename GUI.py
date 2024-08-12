from tkinter import *

import Pokemons
import Utility


def cd_change_heal(but, i):
    if i > 0:
        but['text'] = "heal" + "(" + str(i) + ")" + "\n if you press it while it has CD, you'll auto attack"
        but['bg'] = '#555555'
    else:
        but['text'] = "heal"
        but['bg'] = "#ffffff"


def cd_change_workup(but, i):
    if i > 0:
        but['text'] = "powerup" + "(" + str(i) + ")" + "\n if you press it while it has CD, you'll auto attack"
        but['bg'] = '#555555'
    else:
        but['text'] = "powerup"
        but['bg'] = "#ffffff"


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
        self.heal_button = Button()
        self.powerup_button = Button()

    # return to main menu
    def options_return(self, *args):
        self.textbox.delete(1.0, "end")
        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.leftFrame.destroy()
        self.rightFrame.destroy()
        self.main_menu()

    # first button on main menu - start game and choose pokemon
    def start_foo(self, *args):
        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.choose_poke_window()

    # second button on main menu - show all owned pokemons
    def collection_foo(self, *args):
        self.textbox.insert(1.0, "there should be collection\n")
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

    # third button on main menu - open options
    def options_foo(self, *args):
        self.textbox.delete(1.0, "end")

        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.leftFrame.destroy()
        self.rightFrame.destroy()
        self.options_window()

    # fourth button on main menu - exit from application
    def GuiExit(self, *args):
        self.main.destroy()

    # Pokemon choose func
    def choose_furfrou(self, *args):
        self.panelFrame.destroy()
        self.textFrame.destroy()

        self.battle_window("Furfrou")

    def attack_enemy(self, poke1, poke2):
        s1 = poke1.Attack(poke2) + "\n"
        self.textbox.insert(1.0, s1)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        if self.death_check_enemy(poke2):
            self.winning_screen(True)
            return

        s2 = poke2.auto_battle(poke1)
        self.textbox.insert(1.0, s2)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        if self.death_check(poke1):
            self.winning_screen(False)
            return

        s = Utility.buffCheck(poke1)
        s += Utility.buffCheck(poke2)
        self.textbox.insert(1.0, s)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        cd_change_heal(self.heal_button, Utility.cooldown_check_rest(poke1))
        cd_change_workup(self.powerup_button, Utility.cooldown_check_workup(poke1))

        self.update_status(poke1)
        self.update_status_enemy(poke2)

    def heal_but(self, poke1, poke2):
        if poke1.now_cd_rest < poke1.cd_rest:
            self.attack_enemy(poke1, poke2)
            return

        s1 = poke1.rest()
        self.textbox.insert(1.0, s1)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        s2 = poke2.auto_battle(poke1)
        self.textbox.insert(1.0, s2)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        if self.death_check(poke1):
            self.winning_screen(False)
            return

        cd_change_heal(self.heal_button, Utility.cooldown_check_rest(poke1))
        cd_change_workup(self.powerup_button, Utility.cooldown_check_workup(poke1))

        s = Utility.buffCheck(poke1)
        s += Utility.buffCheck(poke2)
        self.textbox.insert(1.0, s)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        self.update_status(poke1)
        self.update_status_enemy(poke2)

    def powerup_but(self, poke1, poke2):
        if poke1.now_cd_workup < poke1.cd_workup:
            self.attack_enemy(poke1, poke2)
            return

        s1 = poke1.workup()
        self.textbox.insert(1.0, s1)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        s2 = poke2.auto_battle(poke1)
        self.textbox.insert(1.0, s2)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        if self.death_check(poke1):
            self.winning_screen(False)
            return

        cd_change_heal(self.heal_button, Utility.cooldown_check_rest(poke1))
        cd_change_workup(self.powerup_button, Utility.cooldown_check_workup(poke1))

        s = Utility.buffCheck(poke1)
        s += Utility.buffCheck(poke2)
        self.textbox.insert(1.0, s)
        self.textbox.tag_add('title', 1.0, 'end')
        self.textbox.tag_config('title', justify=CENTER)

        self.update_status(poke1)
        self.update_status_enemy(poke2)

    def death_check(self, poke):
        if poke.current_health <= 0:
            self.panelFrame.destroy()
            self.textFrame.destroy()
            self.leftFrame.destroy()
            self.rightFrame.destroy()
            return True

    def update_status(self, poke):
        self.left_text.delete(1.0, "end")
        left_info = (poke.name + "\n" +
                     "HP: " + str(poke.current_health) + "\n" +
                     "Attack value: " + str(poke.attack))
        self.left_text.insert(1.0, left_info)
        self.left_text.tag_add('title', 1.0, 'end')
        self.left_text.tag_config('title', justify=CENTER)

    def update_status_enemy(self, poke):
        self.right_text.delete(1.0, "end")
        right_info = (poke.name + "\n" +
                      "HP: " + str(poke.current_health) + "\n" +
                      "Attack value: " + str(poke.attack))
        self.right_text.insert(1.0, right_info)
        self.right_text.tag_add('title', 1.0, 'end')
        self.right_text.tag_config('title', justify=CENTER)

    def death_check_enemy(self, poke):
        if poke.current_health <= 0:
            self.panelFrame.destroy()
            self.textFrame.destroy()
            self.leftFrame.destroy()
            self.rightFrame.destroy()
            return True

    def winning_screen(self, won):
        self.textFrame = Frame(self.main, height=100, width=1000, bg="gray")
        self.textFrame.pack(side="top", fill="x", expand=0)
        self.panelFrame = Frame(self.main, height=400, width=1000, bg="gray")
        self.panelFrame.pack(side="bottom", fill="both", expand=1)

        self.textbox = Text(self.textFrame, font="Arial 8", wrap="word")
        self.textbox.pack(fill="both")

        if won:
            self.textbox.insert(1.0, "\n" + "YOU WON" + "\n")
            self.textbox.tag_add('title', 1.0, 'end')
            self.textbox.tag_config('title', justify=CENTER)
        else:
            self.textbox.insert(1.0, "\n" + "YOU LOSE" + "\n")
            self.textbox.tag_add('title', 1.0, 'end')
            self.textbox.tag_config('title', justify=CENTER)

        return_to_mm_but = Button(self.panelFrame, text="Return to main menu")
        return_to_mm_but.bind("<Button-1>", self.return_to_main_menu)
        return_to_mm_but.place(x=0, y=0, width=1000, height=400)

    def return_to_main_menu(self, *args):

        self.panelFrame.destroy()
        self.textFrame.destroy()
        self.leftFrame.destroy()
        self.rightFrame.destroy()
        self.main_menu()

    # main menu window
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

    # options window
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

    # Pokemon choose window
    def choose_poke_window(self):
        self.textFrame = Frame(self.main, height=100, width=1000, bg="gray")
        self.textFrame.pack(side="top", fill="both", expand=0)
        self.panelFrame = Frame(self.main, height=400, width=1000, bg="gray")
        self.panelFrame.pack(side="bottom", fill="both", expand=1)

        self.textbox = Text(self.textFrame, font="Arial 8", wrap="word")
        self.textbox.pack(fill="both")

        poke1_but = Button(self.panelFrame, text="Furfrou")
        poke1_but.bind("<Button-1>", self.choose_furfrou)  # add func name
        poke1_but.place(x=0, y=0, width=1000, height=100)

        options_button = Button(self.panelFrame, text="main menu")
        options_button.bind("<Button-1>", self.options_return)
        options_button.place(x=0, y=300, width=1000, height=100)

    # window where battle happens
    def battle_window(self, name):
        your_poke = Pokemons.Furfrou(0)
        if name == "Furfrou":
            your_poke = Pokemons.Furfrou(1)
        enemy_poke = Pokemons.Furfrou(0)
        enemy_poke.name = "Enemy " + enemy_poke.name

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

        self.left_text = Text(self.leftFrame, font="Arial 14", wrap="word", height=7, width=1)
        self.right_text = Text(self.rightFrame, font="Arial 14", wrap="word", height=7, width=1)

        self.left_text.pack(fill="both")
        self.right_text.pack(fill="both")

        left_info = (your_poke.name + "\n" +
                     "HP: " + str(your_poke.current_health) + "\n" +
                     "Attack value: " + str(your_poke.attack))

        self.left_text.insert(1.0, left_info)
        self.left_text.tag_add('title', 1.0, 'end')
        self.left_text.tag_config('title', justify=CENTER)

        right_info = (enemy_poke.name + "\n" +
                      "HP: " + str(enemy_poke.current_health) + "\n" +
                      "Attack value: " + str(enemy_poke.attack))

        self.right_text.insert(1.0, right_info)
        self.right_text.tag_add('title', 1.0, 'end')
        self.right_text.tag_config('title', justify=CENTER)

        # add list with attack with sliding window
        default_attack_button = Button(self.panelFrame, text="attack")
        default_attack_button.bind("<Button-1>",
                                   lambda e, p1=your_poke, p2=enemy_poke: self.attack_enemy(p1, p2))
        default_attack_button.place(x=0, y=0, width=1000, height=100)
        default_attack_button['bg'] = "#ffffff"

        self.heal_button = Button(self.panelFrame, text="heal")
        self.heal_button.bind("<Button-1>",
                              lambda e, b=self.heal_button, p1=your_poke, p2=enemy_poke: self.heal_but(p1, p2))
        self.heal_button.place(x=0, y=100, width=1000, height=100)
        self.heal_button['bg'] = "#ffffff"

        self.powerup_button = Button(self.panelFrame, text="power up")
        self.powerup_button.bind("<Button-1>",
                                 lambda e, b=self.powerup_button, p1=your_poke, p2=enemy_poke: self.powerup_but(p1, p2))
        self.powerup_button.place(x=0, y=200, width=1000, height=100)
        self.powerup_button['bg'] = "#ffffff"

        options_button = Button(self.panelFrame, text="main menu")
        options_button.bind("<Button-1>", self.options_return)
        options_button.place(x=0, y=300, width=1000, height=100)
        options_button['bg'] = "#ffffff"


"""
        default_attack_button = Button(self.panelFrame, text="attack")
        heal_button = Button(self.panelFrame, text="heal")
        powerup_button = Button(self.panelFrame, text="power up")
        options_button = Button(self.panelFrame, text="main menu")
"""
