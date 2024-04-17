class Enemy:
    '''
    Base class for all enemies.
    '''

    def __init__(self, health=10, attack=3, defense=3):
        '''
        Initialize Enemy object.

        Args:
            health (int): The health points of the enemy.
            attack (int): The attack power of the enemy.
            defense (int): The defense power of the enemy.
        '''
        self.health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense

    def attack_hero(self, hero):
        '''
        Attack a hero.

        Args:
            hero (Hero): The hero to attack.
        '''
        damage = max(0, self.attack - hero.defense)
        hero.current_health -= damage
        print(f"{self.__class__.__name__} attacks {hero.__class__.__name__} for {damage} damage!")

class Goblin(Enemy):
    '''
    Goblin class inheriting from Enemy.
    '''

    def __init__(self):
        '''
        Initialize Goblin object.
        '''
        super().__init__(health=8, attack=4, defense=2)

class Orc(Enemy):
    '''
    Orc class inheriting from Enemy.
    '''

    def __init__(self):
        '''
        Initialize Orc object.
        '''
        super().__init__(health=12, attack=5, defense=4)

class Dragon(Enemy):
    '''
    Dragon class inheriting from Enemy.
    '''

    def __init__(self):
        '''
        Initialize Dragon object.
        '''
        super().__init__(health=20, attack=8, defense=6)

    def breathe_fire(self, hero):
        '''
        Breathe fire on a hero.

        Args:
            hero (Hero): The hero to breathe fire on.
        '''
        damage = 10
        hero.current_health -= damage
        print(f"Dragon breathes fire on {hero.__class__.__name__} for {damage} damage!")