from weather import Calendar, WeatherToday
from magic_system import MagicSystem

calendar = Calendar()
magic_system = MagicSystem()

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
        print(f'The fire bonus today is {fire_magic_bonus}\nThe ice bonus today is {ice_magic_bonus}')

print("End of program")
