import pgzrun
from random import randint
from time import time

WIDHT = 800
HEIGHT = 600


TITLE = "Connecting the planets"

#declearing variables
planets = []
lines = []
next_planet = 0

start_time = 0
total_time = 0
end_time = 0

number_of_planets = 8

def create_planets():
    global start_time
    for count in range(0,number_of_planets):
        planet = Actor("planet")
        planet.pos = randint(40, WIDHT - 40), randint(40, HEIGHT - 40)
        planets.append(planet)
    start_time = time()
        
