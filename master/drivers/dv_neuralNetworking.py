# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import time

OUTPUT = "sentinel_output"
INPUT = "sentinel_input"
HIDDEN = "sentinel_hidden"
NEXT_LAYER = "sentinel_next_layer"

SIGMOID = "sentinel_sigmoid"
LINEAR = "sentinel_linear"
LIMITING = "sentinel_limiting"
SPIKING = "sentinel_spiking"
SCALAR = "sentinel_scalar"

class NeuralNetworkError(Exception): pass

class NeuronError(Exception): pass

class programs:
	class v1:
		def simpleEdge(evolvingArguments, standardArguments):
			return standardArguments

class neuron:
	# Input layer neuron has GetInput function
	# Necessarily feeds into hidden neuron
	class input:
		def __init__(this, name, evolvingArgumentsDictionary, function, layer=None, feedto=NEXT_LAYER, activationFunction=SCALAR):
			this.type = INPUT
			this.name = name
			this.target = feedto
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			this.activationFunction = activationFunction

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

	# Multi-network type hidden neuron
	# with multi-purpose output functions
	class hidden:
		def __init__(this, name, evolvingArgumentsDictionary, function, layer=None, feedto=NEXT_LAYER, activationFunction=SCALAR):
			this.type = HIDDEN
			this.name = name
			this.target = feedto
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			this.activationFunction = activationFunction

		def GetInitialData(this, inputValuesDictionary=None): # For FNNs
			if inputValuesDictionary == None:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=inputValuesDictionary)
			else:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)

		def SendData(this): # For ANNs
			this.target.standardInputs = this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)

	# Output neuron, also compatible
	# with FNNs, RNNs, and ANNs.
	# Generally universal output function.
	class output:
		def __init__(this, name, evolvingArgumentsDictionary, function, layer=None, activationFunction=SCALAR):
			this.type = OUTPUT
			this.name = name
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			this.activationFunction = activationFunction

		def GetFinalData(this): # For any NN type
			if this.activationFunction == LINEAR or this.activationFunction == SCALAR:
				return this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)

class FeedforwardNeuralNetwork:
	def __init__(this, neuronObjectList):
		this.neurons = {}
		this.availableLayers = []
		for neuron in neuronObjectsList:
			if not type(neuron.layer) == type(1):
				raise NeuronError("Neuron layer must be an integer")
			if not (neuron.layer in this.neurons.keys()):
				this.neurons[neuron.layer] = []
			this.neurons[neuron.layer].append(neuron)
			pal = []
			if not (neuron.layer in pal):
				pal.append(neuron.layer)
			[this.availableLayers.append(x) for x in pal if x not in this.availableLayers]

	def SetInputs(this, stdin):
		for neuron in this.neurons[this.availableLayers[0]]:
			neuron.standardInputs = stdin

	def MasterCallback(this):
		first = True
		for layer in this.availableLayers:
			# Get dict
			ldict = {}
			odict = {}
			for neuron in this.neurons[layer]:
				if neuron.type != OUTPUT:
					if neuron.type == INPUT:
						odict[neuron.name] = neuron.GetInitialData()
					else:
						odict[neuron.name] = neuron.GetInitialData(inputValuesDictionary = ldict)
				else:
					return neuron.GetFinalData()

			# Cleanup & prep for next layer
			ldict = odict
			if first == True:
				first = False

class TheseusLimiter:
	def __init__(this, targetNeuron):
		pass
	
	def log():
		pass
	
	def limit():
		pass
	
class TheseusLimitationModule:
	def __init__(this, theseusLimiters):
		pass
	
	def regulate():
		pass
