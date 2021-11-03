# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read the EULA in its entirety
# before using this system.

import sys
import time

OUTPUT = "sentinel_output"
INPUT = "sentinel_input"
HIDDEN = "sentinel_hidden"
NEXT_LAYER = "sentinel_next_layer"

class neuron:
	# Input layer neuron has GetInput function
	# Necessarily feeds into hidden neuron
	class input:
		def __init__(this, name, feedto=NEXT_LAYER, evolvingArgumentsDictionary, function, layer=None):
			this.type = INPUT
			this.name = name
			this.target = feedto
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			
		def GetInitialData(this, inputValuesDictionary=None): # For FNNs
			if inputValuesDictionary == None:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=inputValuesDictionary)
			else:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
			
		def SendInitialData(this, inputValuesDictionary=None): # For ANNs
			if inputValuesDictionary == None:
				this.target.standardInputs = this.function(evolvingArguments=this.evolvingArguments, standardArguments=inputValuesDictionary)
			else:
				this.target.standardInputs = this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
		
	class hidden:
		def __init__(this, name, feedto=NEXT_LAYER, evolvingArgumentsDictionary, function, layer=None):
			this.type = HIDDEN
			this.name = name
			this.target = feedto
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			
		def GetInitialData(this, inputValuesDictionary=None): # For FNNs
			if inputValuesDictionary == None:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=inputValuesDictionary)
			else:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
			
		def SendData(this): # For ANNs
			this.target.standardInputs = this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
			
	class output:
		def __init__(this, name, evolvingArgumentsDictionary, function, layer=None):
			this.type = OUTPUT
			this.name = name
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			
		def GetFinalData(this): # For any NN type
			return this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
		
class FeedforwardNeuralNetwork:
	def __init__(this, neuronObjectList):
		this.neurons = {}
		this.availableLayers = []
		for neuron in neuronObjectsList:
			assert type(neuron.layer) == type(1), "Layer number must be an integer"
			if not (neuron.layer in this.neurons.keys()):
				this.neurons[neuron.layer] = []
			this.neurons[neuron.layer].append(neuron)
			pal = []
			if not (neuron.layer in pal):
				pal.append(neuron.layer)
			[this.availableLayers.append(x) for x in pal if x not in this.availableLayers]
			
	def SetInputs(this, stdin):
		for neuron in this.neurons[this.availableLayers[0]]:
			neuron.
