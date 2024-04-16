from numpy.random import choice
import random

class Calendar:
    '''
    Class to generate cycles with alternating Summer and Winter seasons.
    '''

    def __init__(self):
        '''
        Initialize Calendar object.
        '''
        self.cycle_length_range = (2, 10)
        self.day = 0

    def generate_cycle(self):
        '''
        Generate a single cycle with alternating Summer and Winter seasons.

        Returns:
            list: List of tuples containing season, its length, and current day.
        '''
        cycle = []
        seasons = ['Summer', 'Winter']
        for season in seasons:
            length = random.randint(*self.cycle_length_range)
            for day in range(1, length + 1):
                self.day += 1
                cycle.append((season, length, day))
        return cycle

class WeatherToday():
    '''
    Class to generate weather based on season.
    '''
    
    def __init__(self, season):
        '''
        Initialize WeatherToday object.

        Args:
            season (str): The season (either 'Summer' or 'Winter').
        '''
        self.season = season
        self.weather = self.define_weather()

    def define_weather(self):
        '''
        Define the weather based on the season.

        Returns:
            str: The weather for the day.
        '''
        possible_options = {
            'Summer': {'sunny': 0.8, 'cloudy': 0.15, 'rainy': 0.05, 'snowy': 0},
            'Winter': {'sunny': 0.05, 'cloudy': 0.1, 'rainy': 0.1, 'snowy': 0.75}
        }

        if self.season not in possible_options:
            raise ValueError("Invalid season. Please choose either 'Summer' or 'Winter'.")

        weather = choice(list(possible_options[self.season].keys()), 1, p=list(possible_options[self.season].values()))
        return weather[0]
    