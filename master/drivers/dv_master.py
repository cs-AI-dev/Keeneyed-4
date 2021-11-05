import sys
import os

true = True
false = False

class routinesObject:
	def __init__(this):
		pass
	
	def Primary(this):
		# Primary routine imports all drivers,
		# which includes the APIs for neural 
		# networking and memory accessing.
		
		import dv_neuralNetworking as nns
		import dv_cacheGeneration as cg
		
	def Secondary(this):
		# Secondary routine prepares the AGI
		# class. Should be treated with caution!
		# Also instantiates some other tools.
		
		class ArtificialGeneralIntelligence:
			def __init__(this,
						 debug = false,
						 neuralNetworkingVersion = 1.0,
						 selfDestructEnabled = false,
						 simulationInjectTarget = None
						):
				print("[AGI_INSTANTIATION] INITIALIZING ARTIFICIAL GENERAL INTELLIGENCE INSTANTIATION PROCESS.")
				if debug == true: print("[AGI_INSTANTIATION] DEBUG MODE ENABLED.")
				print(" > | Initializing neural networking systems ...")
				print("   | > | Initializing input neural network ...", end="")
				
				this.InputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					nns.neuron.input(
						name = "TextualInput",
						evolvingArgumentsDictionary = {},
						function = nns.programs.v1.simpleEdge,
						layer = 0
						),
					nns.neuron.hidden()
				])
