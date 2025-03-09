class PlayerClass:
    def __init__(self, attack, defence, hp):
        self.attack = attack
        self.defence = defence
        self.hp = hp
    def __str__(self):
        return  " has " + str(self.attack) + " attack and " + str(self.defence) + " defence and " + str(self.hp) + " health"

class Buff:
    def __init__(self,type, mod, op):
        self.type = type
        self.mod = mod
        self.op = op

    def apply(self, player, stat):
        if self.op == "+":
            return stat + self.mod
        elif self.op == "*":
            return stat * self.mod

class Skill(Buff):
    def __init__(self, type, mod):
        Buff.__init__(self, type, mod, "+")

attackSkill = Skill("attack", 1)
defenceSkill = Skill("defence", 1)

class Player:
    def __init__(self, name, skill, attackOrClass, defence = 1, hp = 10):
        self.name = name
        self.buffs.append(skill)
        if isinstance(attackOrClass, PlayerClass):
            self.attack = attackOrClass.attack
            self.defence = attackOrClass.defence
            self.hp = attackOrClass.hp
        elif (attackOrClass + defence + hp) <= 15:
            self.attack = attackOrClass
            self.defence = defence
            self.hp = hp
    attack = 2
    defence = 1
    hp = 10
    lastpotion = None
    applieddefence = False
    buffs = []
    def drink(self, potion):
        self.buffs.append(potion)
        self.lastpotion = potion

    def getattack(self):
        stat = self.attack
        for buff in self.buffs:
            if buff.type == "attack":
                stat = buff.apply(self, stat)
        return stat

    def getdefence(self):
        stat = self.defence
        for buff in self.buffs:
            if buff.type == "defence":
                stat = buff.apply(self, stat)
        return stat
    def __str__(self):
        return self.name + " has " + str(self.getattack()) + " attack and " + str(self.getdefence()) + " defence and " + str(self.hp) + " health"

def println(str):
    print(str)
    print("\n")

class Potion(Buff):
    def __init__(self, type, mod, op):
        Buff.__init__(self, type, mod, op)


rage = Potion("attack", 2, "*")
rock = Potion("defence", 3, "+")

class UI:
    def __init__(self):
        return
    def interact(self, player):
        println(player)
        name = input("What is your name:")
        println("Available classes:")
        println("warrior:" + str(warrior))
        println("tank:" + str(tank))
        klass = input("Choose your class between warrior tank or custom:")
        skill = input("Choose your skill, either attack or defence:")
        if skill == "attack":
            chosenskill = attackSkill
        if skill == "defence":
            chosenskill = defenceSkill
        if klass == "custom":
            attack = int(input("What would you like to have as your attack value:"))
            defence = int(input("What would you like to have as your defence value:"))
            hp = int(input("What would you like to have as your hp value:"))
            return Player(name, chosenskill, attack, defence, hp)
        elif klass == "warrior":
            klass = warrior
        elif klass == "tank":
            klass = tank
        return Player(name, chosenskill, klass)

warrior = PlayerClass(3,2,10)
tank = PlayerClass(1,3,15)

class Game:

    def __init__(self, ui):
        self.ui = ui
        self.player1 = ui.interact("Player 1")
        self.player2 = ui.interact("Player 2")
        println(self.player1)
        println(self.player2)

    def start(self):
        while True:
            self.tick()

    def tick(self):
        self.buff(self.player1)
        self.action(self.player1)
        self.player2.buffs = filter(lambda buff: not issubclass(Potion, buff))
        # self.player2.lastpotion = None
        self.player2.applieddefence = False
        self.buff(self.player2)
        self.action(self.player2)
        self.player1.buffs = filter(lambda buff: not issubclass(Potion, buff))
        # self.player1.lastpotion = None
        self.player1.applieddefence = False
        println(self.player1)
        println(self.player2)

    def action(self, player):
        action = input(player.name + ", Choose an action between attack and defend:")
        match action:
            case "attack":
                self.attack(player, self.player2 if player != self.player2 else self.player1)
            case "defend":
                self.defend(player)

    def attack(self, attacker, reciever):
        if attacker.getattack() > reciever.getdefence():
            reciever.hp = reciever.hp - (attacker.getattack() - (reciever.getdefence() if reciever.applieddefence else 0))
        if reciever.hp <= 0:
            println(attacker.name + " has won the bout")
            exit()

    def defend(self, defender):
        defender.applieddefence = True

    def buff(self, drinker):
        drink = input(drinker.name + " Would you like to buff?")
        if drink == "yes":
            type = input("Do you buff your attack or buff your defence?")
            match type:
                case "attack":
                    potion = rage
                    stat = drinker.attack
                case "defence":
                    potion = rock
                    stat = drinker.defence
            drinker.buffs.append(potion)
            # drinker.lastpotion = potion

def main():
    ui = UI()
    game = Game(ui)
    game.start()

main()