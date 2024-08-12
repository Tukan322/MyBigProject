def buffCheck(poke):
    poke.workUpCountBuffed -= 1
    if poke.workUpCountBuffed == 0:
        poke.attack = poke.norm_attack
        return "Усиление атаки " + poke.name + " закончилось.\n"
    return ""


def cooldown_check_rest(poke):
    poke.now_cd_rest += 1
    if poke.now_cd_rest <= poke.cd_rest:
        return poke.cd_rest - poke.now_cd_rest
    else:
        return 0

def cooldown_check_workup(poke):
    poke.now_cd_workup += 1
    if poke.now_cd_workup <= poke.cd_workup:
        return poke.cd_workup - poke.now_cd_workup
    else:
        return 0

