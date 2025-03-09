def println(str):
    print(str + "\n")


import random
import math
def battle(difficulty):
    attack = math.ceil(math.ceil(math.log(difficulty) + 1) / 1.5)
    defend = math.ceil(math.log(difficulty))
    hp = math.ceil(math.log(difficulty) * 2.5 + 10)
    heal =math.ceil(math.log(difficulty) * 2 + 1)
    healstock = math.ceil(math.log(difficulty))
    enemyattack = math.ceil(math.ceil(math.log(difficulty) + 1))
    temp = 0
    enemyhp = math.ceil(math.log(difficulty) * 3 + 5)
    enemyheal = math.ceil(math.log(difficulty))
    println("The monster has " + str(enemyhp) + " health and " + str(enemyattack) + " attack and can heal " + str(enemyheal) + " health at a time.")
    println("You have " + str(hp) + " health and " + str(attack) + " attack and " + str(defend) + " defence")
    while True :
        enemyattack = math.ceil(math.log(difficulty) + 1)
        action = str(input("You have " + str(healstock) + " heals left. Choose an action between attack, defend or heal:"))
        if action != "attack" and action != "defend" and action != "heal":
            continue
        if action == "attack":
            println("You chose to attack")
            enemyhp = enemyhp - attack
            println("The monster has " + str(enemyhp) + " health")
            if enemyhp <= 0:
                println("You win")
                break
        if action == "defend":
            println("You chose to defend")
            temp = defend
        if action == "heal":
            if healstock > 0:
                println("You chose to heal")
                hp = hp + heal
                healstock-=1
                println("You have "+ str(hp) + " health and you may heal " + str(healstock) + " times")
            else:
                println("You cannot heal")
        enemychoice = random.randint(1, 5)
        if enemychoice <= 3:
            println("The enemy chose to attack")
            if enemyattack - temp <= 0:
                enemyattack = 0
            else:
                enemyattack = enemyattack - temp
            hp = hp - enemyattack
            println("You have " + str(hp) + " hp left")
        if enemychoice >= 4:
            println("The monster chose to heal")
            enemyhp = enemyhp + enemyheal
            println("The monster has " + str(enemyhp) + " health")
        temp = 0
        if hp <= 0:
            println("You lose")
            exit()


def multi(x):
    battle(x)
    println("Next Battle")
    battle(x+1)
    println("Final Battle")
    battle(x*2)

multi(100)
