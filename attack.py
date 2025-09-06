import creatures

def calculate_attack_damage(power, attack, defense, atkbuff, defbuff):
    damage=round(power*(((attack*0.1)*atkbuff)-((defense*0.1)*defbuff)))
    print(damage)
calculate_attack_damage(20,7,4,1,1)