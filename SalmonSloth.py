''''
Spirit Animal User ID: SalmonSloth
Date the file was last edited: December 6, 2018
Challenge Number: 6

SOURCES OF HELP:
a) https://stackoverflow.com/questions/7115437/how-to-embed-a-small-numpy-array-into-a-predefined-block-of-a-large-numpy-arra  
b) Took help from Lecture 20 slide provided by Dr. Jones
c) Checked some Youtube videos
e) Googled
f)Asked some questions to Paul

'''



from __future__ import division
import neuro
import program
#training inputs and their respective target
inputs=program.outcomes
targets=program.target

#number of repetitions to train the network
reps=1000
network=[] #makes an empty list to contain the neural net
network=neuro.setup_network(inputs)
neuro.train(network, inputs, targets, reps)
neuro.writeNetworkToFile("myNetwork.net", network)
