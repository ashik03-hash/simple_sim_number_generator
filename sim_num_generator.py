'''

'''
import random

def generate_sim_number():
    sim=[]
    country_code="+91"
    number=str(random.randint(1000000000,9999999999)) 
    sim_number=country_code + number
    sim.append(sim_number)
    print(sim)
generate_sim_number()