def getminvalue(power,armor):
    total_damage= sum(power)
    max_reducation = 0 
    for i in range(len(power)):
        max_reducation = max(max_reducation,min(power[i],armor))

    return total_damage = max_reducation +1

                             
                             