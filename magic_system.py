class MagicSystem:
    '''
    Class to manage the magic system in the game.
    '''

    def __init__(self):
        '''
        Initialize MagicSystem object.
        '''
        self.magic_effects = {'fire': 0, 'ice': 0}  # Initial magic attributes

    def apply_weather_effects(self, weather):
        '''
        Apply global buffs and debuffs based on the weather.

        Args:
            weather (str): The current weather.
        '''
        self.magic_effects = {'fire': 0, 'ice': 0}
        
        if weather == 'sunny':
            self.magic_effects['fire'] += 1
            self.magic_effects['ice'] -= 1
        elif weather == 'rainy':
            self.magic_effects['fire'] -= 1
        elif weather == 'snowy':
            self.magic_effects['fire'] -= 1
            self.magic_effects['ice'] += 1
        elif weather == 'cloudy':
            pass  # No magic impacts for cloudy weather