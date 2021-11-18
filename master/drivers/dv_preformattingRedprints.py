# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os
import dv_neuralNetworking as nns

class InvalidPreformat(Exception):
	pass

class InvalidVersionNumber(Exception):
	pass

class FormattingError(Exception):
	pass

preformats = ["keeneyed", "sharpclawed", "ozymandias"]
maximum = "sentinel_maximum"

class install:
	class preformattedAGIs:
		class versions:
			keeneyed = [4]
		def keeneyed(parent, version):
			
			# The namesake of this entire engine, the Keeneyed-4 general intelligence is
			# designed to support 7 neural nets, each leading into a central cortex which
			# controls the thought of the system. For a text-only interface,  only 2 NNs
			# are functional
			
			if not version in install.preformattedAGIs.versions.keeneyed:
				raise InvalidVersionNumber(f"'{version}' is not a valid version for the Keeneyed AGI system.")
			
			if version == 4:
				print("[ke4_install] beginning preformatted installation of the Keeneyed-4 AGI system ...", end="")
				print(" > beginning neural network instantiation ...")
				parent.TextInputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList  = [
					nns.neuron.input("text", 
					])
				parent.TextOutputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					])
				parent.MemoryGenerationNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					])
				parent.MemoryRetrievalNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					])
	class preformattedAGIModules:
		pass
