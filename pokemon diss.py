class Pokemon:
    basic_attack = 'Fling'
    damage = 40;

    def __init__(self, Lucario, TJ):
        self.name = Lucario
        self.trainer = TJ
        self.level = 1
        self.hp = 50
        self.paralyzed = False
        self.probability = 1

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, ' fainted!')
