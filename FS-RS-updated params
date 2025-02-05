!pip install netpyne
!pip install neuron matplotlib

from netpyne import specs, sim
import matplotlib.pyplot as plt
netParams = specs.NetParams()

## Cell parameters
RScell = {'secs': {}}
RScell['secs']['soma'] = {'geom': {}, 'mechs': {}}
RScell['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 150.0}                           #updated axial Ra to 150 per Konstantoudaki (2014) Table 3
RScell['secs']['soma']['mechs']['hh'] = {'gnabar': 0.075, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  #updated gnabar to 0.075 per Konstantoudaki (2014) table 3
netParams.cellParams['RS'] = RScell

FScell = {'secs': {}}
FScell['secs']['soma'] = {'geom': {}, 'mechs': {}}
FScell['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 150.0}                           #updated axial Ra to 150 Konstantoudaki (2014) Table 2 
FScell['secs']['soma']['mechs']['hh'] = {'gnabar': 0.135, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  #updated gnabar to 0.135 Konstantoudaki (2014) Table 2
netParams.cellParams['FS'] = FScell

## Population parameters
netParams.popParams['RS'] = {'cellType': 'RS', 'numCells': 10} #changed ratio RS:FS = 10:1 per Aric's sugggestion. 
netParams.popParams['FS'] = {'cellType': 'FS', 'numCells': 1}  

## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.5, 'tau2': 5.0, 'e': 0} #updated tau1 to 0.5 per Markram et al. (1998)  
netParams.synMechParams ['inh'] = {'mod': 'Exp2Syn','tau1':0.1, 'tau2':2.0, 'e': -70}  #updated tau2 to 2 ms per Wang & Buzsáki (1996)
netParams.stimSourceParams['TCI'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}  #Thalamocortical input 
netParams.stimTargetParams['TCI->RS'] = {'source': 'TCI', 'conds': {'cellType': 'RS'}, 'weight': 0.01, 'delay': 1.3, 'synMech': 'exc'} #updated delay to 1.3 ms per Agmon et al. Fig 6
netParams.stimTargetParams['TCI->FS'] = {'source': 'TCI', 'conds': {'cellType': 'FS'}, 'weight': 0.01, 'delay': 0.4, 'synMech': 'exc'} #updated delay to 0.4 per Agmon et al. Fig 6

## Cell connectivity rules
netParams.connParams['RS->RS'] = { #  RS -> RS label
        'preConds': {'pop': 'RS'},   # conditions of presyn cells
        'postConds': {'pop': 'RS'},  # conditions of postsyn cells
        'probability': 0.5,         # probability of connection
        'weight': 0.01,             # synaptic weight
        'delay': 2.4,               # transmission delay 2.4 ms per Agmon (2023) Fig 6
        'synMech': 'exc'}           # synaptic mechanism

netParams.connParams['RS->FS'] = { #  RS -> FS label
        'preConds': {'pop': 'RS'},   # conditions of presyn cells
        'postConds': {'pop': 'FS'},  # conditions of postsyn cells
        'probability': 0.5,         # probability of connection
        'weight': 0.01,             # synaptic weight
        'delay': 1.5,                # transmission delay 1.5 ms per Agmon (2023) Fig 6 
        'synMech': 'exc'}           # synaptic mechanism

netParams.connParams['FS->RS'] = { #  FS -> RS label
        'preConds': {'pop': 'FS'},   # conditions of presyn cells
        'postConds': {'pop': 'RS'},  # conditions of postsyn cells
        'probability': 0.5,         # probability of connection
        'weight': 0.01,             # synaptic weight
        'delay': 0.8,                 # transmission delay 0.8 ms per Agmon (2023) Fig 6
        'synMech': 'inh'}           # inhibitory synaptic mechanism

# Simulation options
simConfig = specs.SimConfig()       # object of class SimConfig to store simulation configuration

simConfig.duration = 1*1e3          # Duration of the simulation, in ms
simConfig.dt = 0.025                # Internal integration timestep to use
simConfig.verbose = False           # Show detailed messages
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.1          # Step size in ms to save data (e.g. V traces, LFP, etc)
simConfig.filename = 'tut2'         # Set file output name
simConfig.savePickle = False        # Save params, network and sim output to pickle file

simConfig.analysis['plotRaster'] = {'saveFig': True, 'showFig': True}                  # Plot a raster
simConfig.analysis['plotTraces'] = {'include': [i for i in range (1,16)], 'saveFig': True, 'showFig' : True}  # Plot recorded traces for this list of cells
simConfig.analysis['plot2Dnet'] = {'saveFig': True, 'showFig' : True}                   # plot 2D cell positions and connections

#Create Network and simulation
sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)
plt.show()

