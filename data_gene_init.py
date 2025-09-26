import cantera as ct
import numpy as np
from read_input import *
from parameter import parameter
import os
import sys
import math
 
def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   
		os.makedirs(path)            
		print("---  new folder...  ---")
		print("---  OK  ---")

	else:
		print("---  There is this folder!  ---")
		
print(ct.__version__)
parameter_dict=parameter.parameter_dict
read_input()

air = parameter_dict['oxidizer_component'] #oxidizer stream component
#print(air)
fuel = parameter_dict['fuel_component'] #fuel stream component
#print(fuel)
reaction_mechanism = parameter_dict['mechanism_file'] #mechanism file
gas_RK = ct.Solution(reaction_mechanism) #instanciate the solution object in order to use the mechanism file data

#gas_RK.transport_model = 'high-pressure'
initial_width=parameter_dict['domain_length']
#print(initial_width)
initial_grid=np.linspace(0,initial_width,100)#set the initial grid

f = ct.CounterflowDiffusionFlame(gas_RK, initial_grid)#create the counter flow diffusion flame problem
f.transport_model = parameter_dict['transport_model']#Multi-component transport model

#set operating pressure and boundary conditions
f.P = parameter_dict['operating_pressure']
f.fuel_inlet.mdot = parameter_dict['fuel_mdot'] #fuel inlet
f.fuel_inlet.X = fuel
f.fuel_inlet.T = parameter_dict['fuel_temperature']
#print(f.density)
f.oxidizer_inlet.mdot = parameter_dict['oxidizer_mdot'] #oxidizer inlet
f.oxidizer_inlet.X = air
f.oxidizer_inlet.T = parameter_dict['oxidizer_temperature']

f.set_refine_criteria(ratio=3.0, slope=0.1, curve=0.2, prune=0.0) #refinement settings

temperature_limit_extinction = 1500 #set extinction temperature

# strain rate loop
strain_factor = 1.5
data_directory = parameter_dict['primitive_data_path']

n = 0
initial_fuel_inlet_mdot = parameter_dict['fuel_mdot']
initial_oxidizer_inlet_mdot = parameter_dict['oxidizer_mdot']
fuel_inlet_mdot = initial_fuel_inlet_mdot
oxidizer_inlet_mdot = initial_oxidizer_inlet_mdot
width =  initial_width

arguments = sys.argv

step = int(arguments[1])
if step == 0:
    print('strain rate iteration', 0)
    initial_guess_file = 'initial_guess.yaml'
    if os.path.exists(initial_guess_file):
        f = ct.CounterflowDiffusionFlame(gas_RK, initial_grid)
        f.restore(initial_guess_file, name='diff1D')
        f.transport_model = parameter_dict['transport_model']
        f.P = parameter_dict['operating_pressure']
        f.fuel_inlet.X = fuel
        f.fuel_inlet.T = parameter_dict['fuel_temperature']
        f.oxidizer_inlet.X = air
        f.oxidizer_inlet.T = parameter_dict['oxidizer_temperature']
        f.fuel_inlet.mdot = fuel_inlet_mdot
        f.oxidizer_inlet.mdot = oxidizer_inlet_mdot
        f.set_refine_criteria(ratio=3.0, slope=0.1, curve=0.2, prune=0.0)
        f.solve(loglevel=1, auto=True)
    else:
        f = ct.CounterflowDiffusionFlame(gas_RK, initial_grid)
        f.transport_model = parameter_dict['transport_model']
        f.P = parameter_dict['operating_pressure']
        f.fuel_inlet.X = fuel
        f.fuel_inlet.T = parameter_dict['fuel_temperature']
        f.oxidizer_inlet.X = air
        f.oxidizer_inlet.T = parameter_dict['oxidizer_temperature']
        f.fuel_inlet.mdot = fuel_inlet_mdot
        f.oxidizer_inlet.mdot = oxidizer_inlet_mdot
        f.set_refine_criteria(ratio=3.0, slope=0.1, curve=0.2, prune=0.0)
        f.solve(loglevel=1, auto=True)
    print((f.velocity[0]-f.velocity[-1])/initial_width) #mean strain rate
    file_name = '/strain_loop_' + format(0, '02d') + '.yaml'
    mkdir(data_directory)
    f.save(data_directory + file_name, name='diff1D', loglevel=1,
        description='Cantera version ' + ct.__version__ +
        ', reaction mechanism ' + reaction_mechanism)
    print("Solved on {:d} points.".format(len(f.T)))
    print("T max {:.0f} K.".format(max(f.T)))
else:
    for i in range(step):
        fuel_inlet_mdot *= strain_factor**(10/(i+9))
        oxidizer_inlet_mdot *= strain_factor**(10/(i+9))
    ratio = math.sqrt(initial_fuel_inlet_mdot/fuel_inlet_mdot)
    fuel_inlet_mdot *= ratio
    oxidizer_inlet_mdot *= ratio
    width *= ratio

    print('strain rate iteration', step)
    initial_grid=np.linspace(0,width,100)
    f = ct.CounterflowDiffusionFlame(gas_RK, initial_grid)
    f.transport_model = parameter_dict['transport_model']
    #f.transport_model = 'high-pressure-Chung'
    f.P = parameter_dict['operating_pressure']
    f.fuel_inlet.X = fuel
    f.fuel_inlet.T = parameter_dict['fuel_temperature']
    f.oxidizer_inlet.X = air
    f.oxidizer_inlet.T = parameter_dict['oxidizer_temperature']
    f.fuel_inlet.mdot = fuel_inlet_mdot
    f.oxidizer_inlet.mdot = oxidizer_inlet_mdot

    f.set_refine_criteria(ratio=3.0, slope=0.1, curve=0.2, prune=0.0)
    f.solve(loglevel=1, auto=True)
    print((f.velocity[0]-f.velocity[-1])/initial_width)
    file_name = '/strain_loop_' + format(step, '02d') + '.yaml'
    f.save(data_directory + file_name, name='diff1D', loglevel=1,
        description='Cantera version ' + ct.__version__ +
        ', reaction mechanism ' + reaction_mechanism)
    print("Solved on {:d} points.".format(len(f.T)))
    print("T max {:.0f} K.".format(max(f.T)))
