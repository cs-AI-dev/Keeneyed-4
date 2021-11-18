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

class function:
	class keeneyed_4:
		def PassFunction(evolvingArguments, standardArguments, activationFunction, parent):
			return standardArguments

		def SubjectPredicateDetection(evolvingArguments, standardArguments, activationFunction, parent):
			pass

		def TokenizeByNLTK(evolvingArguments, standardArguments, activationFunction, parent):
			pass

		def EmphasisLevelDetection(evolvingArguments, standardArguments, activationFunction, parent):
			pass

		def StartFinishTokenDetection(evolvingArguments, standardArguments, activationFunction, parent):
			pass

		def Keeneyed4Tokenization(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def ToneDetection(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def SentenceConstruction(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def SyntacticLanguageConstruction(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def ImplicitReturnTypeDetection(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def ReverseKeeneyed4Tokenization(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def ReverseNLTKTokenization(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def ReverseImplicitReturnType(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def PunctuationSynthesis(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def StartEndTokenSynthesis(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def WordListingSynthesis(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def AssociatedOutputsSynthesis(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def TextualOutputsSynthesis(evolvingArguments, standardArguments, activationFunction, parent):
			pass
		
		def NonTextualOutputsSynthesis(evolvingArguments, standardArguments, activationFunction, parent):
			pass

class install:
	class preformattedAGIs:
		class versions:
			keeneyed = [4]
		def keeneyed(parent, version):
			
			# The namesake of this entire engine, the Keeneyed-4 general intelligence is
			# designed to support several neural nets, each leading into a central cortex which
			# controls the thought of the system. For a text-only interface, only 4 neural
			# nets are functional, the input and output nets for the text interface and the
			# simulacrum's memory drive.
			
			if not version in install.preformattedAGIs.versions.keeneyed:
				raise InvalidVersionNumber(f"'{version}' is not a valid version for the Keeneyed AGI system.")
			
			if version == 4:
				print("[ke4_install] beginning preformatted installation of the Keeneyed-4 AGI system ...", end="")
				print(" > beginning neural network instantiation ...")
				parent.TextInputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList  = [
					nns.neuron.input("text",
							 evolvingArgumentsDictionary = {},
							 function = function.keeneyed_4.PassFunction,
							 layer = 0,
					])
				parent.TextOutputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					])
				parent.MemoryGenerationNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					])
				parent.MemoryRetrievalNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
					])
	class preformattedAGIModules:
		pass
