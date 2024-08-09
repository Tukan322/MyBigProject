def buffCheck(poke):
    poke.workUpCountBuffed -= 1
    if poke.workUpCountBuffed == 0:
        poke.attack = poke.norm_attack
        return "Усиление атаки закончилось."
