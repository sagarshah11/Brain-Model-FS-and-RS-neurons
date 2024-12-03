from neuron import h
import matplotlib.pyplot as plt

#Creating RS cell soma
RS_soma = h.Section(name ='soma')
RS_soma.L = 18.8
RS_soma.diam = 18.8
RS_soma.Ra = 123.0

#Inserting Hodgkin Huxley mechanism and setting its parameters
RS_soma.insert ('hh')
RS_soma.gnabar_hh = 0.12 #Na conductance
RS_soma.gkbar_hh = 0.036 #K conductance
RS_soma.gl_hh = 0.003 #Leak conductance
RS_soma.el_hh = -70 #leak reversal potential

#Creating FS cell soma
FS_soma = h.Section(name ='soma')
FS_soma.L = 18.8
FS_soma.diam = 18.8
FS_soma.Ra = 123.0

#Inserting Hodgkin Huxley mechanism and setting its parameters
FS_soma.insert ('hh')
FS_soma.gnabar_hh = 0.12 #Na conductance
FS_soma.gkbar_hh = 0.036 #K conductance
FS_soma.gl_hh = 0.003 #Leak conductance
FS_soma.el_hh = -70 #leak reversal potential

#Creating RS and FS populations
num_RS_soma = 10
num_FS_soma = 5
RS_soma_population= [RS_soma() for _ in range(num_RS_soma)]
FS_soma_population= [FS_soma() for _ in range(num_FS_soma)]

#Setting up Pre/Post Synaptic Network
def connect(pre_cell, post_cell, weight, delay):
  syn = h.ExpSyn(post_cell(0.5))  # Place synapse at the middle of the post cell
  nc = h.NetCon(pre_cell.cell, post_cell.cell)
  nc.weight[0] = weight
  nc.delay = delay

#synapse list
RS_to_RS = []
RS_to_FS= []
FS_to_FS = []

#Connecting RS to RS
for i in range(num_RS_soma):
    for j in range(num_RS_soma):
        if i != j:  # Avoid self-connection
          RS_to_RS.append(connect(RS_soma_population[i], RS_soma_population[j], weight=0.1, delay=2))

#Connecting RS to FS cells
for i in range(num_RS_soma):
    for j in range(num_FS_soma):
        if j < len(FS_soma_population):  # Ensure j is within bounds of FS population
            RS_to_FS.append(connect(RS_soma_population[i], FS_soma_population[j], weight=0.1, delay=2))
