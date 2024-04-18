from weather import Calendar, WeatherToday
from magic_system import MagicSystem
from hero import Warrior, Rogue, Wizard
from npcs import Goblin

def choose_hero_class():
    '''
    Prompt the player to choose a hero class.
    '''
    print("Choose your hero class:")
    print("1. Warrior")
    print("2. Rogue")
    print("3. Wizard")

    while True:
        choice = input("Enter the number corresponding to your choice: ")
        if choice == '1':
            return Warrior()
        elif choice == '2':
            return Rogue()
        elif choice == '3':
            return Wizard()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

calendar = Calendar()
magic_system = MagicSystem()

hero = choose_hero_class()
print(f"You've chosen {hero.__class__.__name__}")
print("Base Stats: \nHealth = {} \nAttack = {} \nDefense = {} \nMagic Power = {}".format(hero.health, hero.attack, hero.defense, hero.magic_power))

while True:
    command = input("Press Enter to generate a new cycle or type 'Stop' to end: ")
    if command.lower() == 'stop':
        break
    cycle = calendar.generate_cycle()
    for season, length, day in cycle:
        weather_today = WeatherToday(season=season)
        magic_system.apply_weather_effects(weather_today.weather)
        fire_magic_bonus = magic_system.magic_effects['fire']
        ice_magic_bonus = magic_system.magic_effects['ice']
        
        print(f'Day {day} of {season}, the weather is {weather_today.weather}')
        # print(f'The fire bonus today is {fire_magic_bonus}\nThe ice bonus today is {ice_magic_bonus}')
    
    # Test fight at the end of the year
    enemy = Goblin()
    fight_command = input("Enter command to fight: ")
    if fight_command == 'attack':
        hero.attack_enemy(enemy)
    elif fight_command == 'cast spell':
        hero.cast_spell(enemy)
        print(enemy.current_health)
    if enemy.current_health <= 0:
        print('You killed the enemy. The game ends.')
        break

print("End of program")
