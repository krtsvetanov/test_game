class Hero:
    '''
    Base class for all heroes.
    '''

    def __init__(self, health=10, attack=3, defense=3, magic_power=0):
        '''
        Initialize Hero object.

        Args:
            health (int): The health points of the hero.
            attack (int): The attack power of the hero.
            defense (int): The defense power of the hero.
            magic_power (int): The magical power of the hero.
        '''
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic_power = magic_power

    def attack_enemy(self, enemy):
        '''
        Attack an enemy.

        Args:
            enemy (Hero): The enemy to attack.
        '''
        damage = max(0, self.attack - enemy.defense)
        enemy.health -= damage
        print(f"{self.__class__.__name__} attacks {enemy.__class__.__name__} for {damage} damage!")

    def drink_potion(self, potion):
        '''
        Restore health by eating.
        '''
        if potion == 'Healing potion':
            self.health += 5
            print(f"{self.__class__.__name__} drinks potion and restores health.")
        elif potion == 'Potion of power':
            self.attack += 1
            print(f"{self.__class__.__name__} drinks potion and becomes stronger.")
        else:
            print('Enter valid potion name')

    def sleep(self):
        '''
        Restore health and mana by sleeping.
        '''
        self.health += 10
        print(f"{self.__class__.__name__} sleeps and restores health.")

class Warrior(Hero):
    '''
    Warrior class inheriting from Hero.
    '''

    def __init__(self):
        '''
        Initialize Warrior object.
        '''
        super().__init__(health=13, attack=6, defense=5)

    def rage(self):
        '''
        Use rage ability.
        '''
        self.attack += 3
        print("Warrior uses rage and increases attack power!")

class Rogue(Hero):
    '''
    Rogue class inheriting from Hero.
    '''

    def __init__(self):
        '''
        Initialize Rogue object.
        '''
        super().__init__(health=10, attack=5, defense=3)

    def sneak_attack(self, enemy):
        '''
        Perform a sneak attack on an enemy.

        Args:
            enemy (Hero): The enemy to attack.
        '''
        damage = self.attack * 2
        enemy.health -= damage
        print(f"Rogue performs a sneak attack on {enemy.__class__.__name__} for {damage} damage!")

class Wizard(Hero):
    '''
    Wizard class inheriting from Hero.
    '''

    def __init__(self):
        '''
        Initialize Wizard object.
        '''
        super().__init__(health=8, attack=3, defense=2, magic_power=10)

    def cast_spell(self, enemy):
        '''
        Cast a spell on an enemy.

        Args:
            enemy (Hero): The enemy to cast the spell on.
        '''
        damage = self.magic_power * 2
        enemy.health -= damage
        print(f"Wizard casts a spell on {enemy.__class__.__name__} for {damage} damage!")