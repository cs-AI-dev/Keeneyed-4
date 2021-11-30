# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os
import dv_neuralNetworking as nns

import nltk
from nltk.corpus import wordnet as wn

class InvalidPreformat(Exception):
	pass

class InvalidVersionNumber(Exception):
	pass

class FormattingError(Exception):
	pass

preformats = ["keeneyed", "sharpclawed", "ozymandias"]
maximum = "sentinel_maximum"

class implicit_return_type:
	method = "sentinel_irt_method"
	time = "sentinel_irt_time"
	reason = "sentinel_irt_reason"
	boolean = "sentinel_irt_bool"
	opinion = "sentinel_irt_opinion"
	obj = "sentinel_irt_object"

class function:
	class keeneyed_4:
		def PassFunction(evolvingArguments, standardArguments, activationFunction, parent):
			return standardArguments

		def SubjectPredicateDetection(evolvingArguments, standardArguments, activationFunction, parent):
			return {
				"subj": [x for x in nltk.pos_tag(standardArguments["inputText"]) if x[1] == "NN" or x[1] == "NNP" or x[1] == "NNS" or x[1] == "PRP"], 
				"pred": [x for x in nltk.pos_tag(standardArguments["inputText"]) if x[1] == "VBD" or x[1] == "VBG" or x[1] == "VBP" or x[1] == "VBZ"]
			}

		def TokenizeByNLTK(evolvingArguments, standardArguments, activationFunction, parent):
			return {
				"raw": standardArguments,
				"pos_tag": nltk.pos_tag(standardArguments),
				"word_tk": nltk.word_tokenize(standardArguments),
				"sent_tk": nltk.sent_tokenize(standardArguments),
				"sub_pre": function.keeneyed_4.SubjectPredicateDetection({}, standardArguments, SCALAR, parent)
			}

		def EmphasisLevelDetection(evolvingArguments, standardArguments, activationFunction, parent):
			o = 0
			o -= 7 * len(standardArguments["subject_predicate_detection"]["subj"])
			for word in standardArguments["nltk_tokenization"]["pos_tag"]:
				if word[1] == "RBS":
					o += 20
				if word[1] == "RBR":
					o += 10
				if word[1] == "RB":
					o += 5
				if word[1]
			return o

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
				print("[ke4_install] beginning preformatted installation of the Keeneyed-4 AGI system ...")
				print(" > beginning neural network instantiation ...")
				
				print("        text input neural network ...", end="")
				
				try: 
					
					parent.TextInputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList  = [
						# I
						nns.neuron.input(
							name = "text",
							evolvingArgumentsDictionary = {}, # Nothing, since this is an input neuron
							function = function.keeneyed_4.PassFunction,
							layer = 0,
						),

						# H1
						nns.neuron.hidden(
							name = "subject_predicate_detection",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.SubjectPredicateDetection,
							layer = 1,
						),

						nns.neuron.hidden(
							name = "nltk_tokenization",
							evolvingArgumentsDictionary = {}, # Nothing, since NLTK has linear tokenization
							function = function.keeneyed_4.TokenizeByNLTK,
							layer = 1
						),

						# H2
						nns.neuron.hidden(
							name = "emphasis_level_detection",
							evolvingArgumentsDictionary = { # Threshold values for emphasis lv detection
								"emphasis_threshold_l2": 20,
								"emphasis_threshold_l1": 40,
								"emphasis_threshold_l0": 60,
								"emphasis_threshold_h1": 80,
								"emphasis_threshold_h2": 100
							},
							function = function.keeneyed_4.EmphasisLevelDetection,
							layer = 2
						),

						nns.neuron.hidden(
							name = "start_finish_token_detection",
							evolvingArgumentsDictionary = {
								"start": {
									"when": [implicit_return_type.time],
									"what": [implicit_return_type.reason, implicit_return_type.method, implicit_return_type.opinion, implicit_return_type.obj],
									"how": [implicit_return_type.method],
									"why": [implicit_return_type.reason],
									"who": [implicit_return_type.obj]
								},
								"end": {
									".": None,
									"!": None
								}
							},
							function = function.keeneyed_4.StartFinishTokenDetection,
							layer = 2
						),

						nns.neuron.hidden(
							name = "keeneyed_4_forward_tokenization",
							evolvingArgumentsDictionary = {
								"rigidity": 50 # Range between 1 and 100
							},
							function = function.keeneyed_4.Keeneyed4Tokenization,
							layer = 2
						),

						nns.neuron.hidden(
							name = "tone_analysis",
							evolvingArgumentsDictionary = {
								"rigidity": 50 # Range between 1 and 100
							},
							function = function.keeneyed_4.ToneDetection,
							layer = 3
						),

						nns.neuron.hidden(
							name = "sentence_construction_analysis",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.SentenceConstruction,
							layer = 3
						),

						nns.neuron.hidden(
							name = "syntactic_analysis",
							evolvingArgumentsDictionary = {
								"specificity": 50 # Range between 1 and 100
							},
							function = function.keeneyed_4.SyntacticLanguageConstruction,
							layer = 4
						),

						nns.neuron.hidden(
							name = "implicit_return_type_analysis",
							evolvingArgumentsDictionary = {
								"when": [implicit_return_type.time],
								"what": [implicit_return_type.reason, implicit_return_type.method, implicit_return_type.opinion, implicit_return_type.obj],
								"how": [implicit_return_type.method],
								"why": [implicit_return_type.reason],
								"who": [implicit_return_type.obj]
							},
							function = function.keeneyed_4.ImplicitReturnTypeDetection,
							layer = 4
						),

						nns.neuron.output(
							name = "output",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.PassFunction,
							layer = 5
						),
						])
				
				except Exception as e:
					raise FormattingError(f"[ERROR CODE 53] Error occurred during Keeneyed-4 AGI setup: {e}")
				
				print("complete.\n        omni-output neural network ...", end="")
				
				try:
				
					parent.TextOutputNeuralNetwork = nns.FeedforwardNeuralNetwork(neuronObjectsList = [
						nns.neuron.input(
							name = "syntactic_nlp",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.PassFunction,
							layer = 0
						),

						nns.neuron.hidden(
							name = "reverse_keeneyed_4_tokenization",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.ReverseKeeneyed4Tokenization,
							layer = 1
						),

						nns.neuron.hidden(
							name = "reverse_nltk_tokenization",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.ReverseNLTKTokenization,
							layer = 1
						),

						nns.neuron.hidden(
							name = "reverse_implicit_return_type",
							evolvingArgumentsDictionary = {
								"when": [implicit_return_type.time],
								"what": [implicit_return_type.reason, implicit_return_type.method, implicit_return_type.opinion, implicit_return_type.obj],
								"how": [implicit_return_type.method],
								"why": [implicit_return_type.reason],
								"who": [implicit_return_type.obj]
							},
							function = function.keeneyed_4.ReverseImplicitReturnType,
							layer = 1
						),

						nns.neuron.hidden(
							name = "punctuation_synthesis",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.PunctuationSynthesis,
							layer = 2
						),

						nns.neuron.hidden(
							name = "start_end_synthesis",
							evolvingArgumentsDictionary = {
								"when": [implicit_return_type.time],
								"what": [implicit_return_type.reason, implicit_return_type.method, implicit_return_type.opinion, implicit_return_type.obj],
								"how": [implicit_return_type.method],
								"why": [implicit_return_type.reason],
								"who": [implicit_return_type.obj]
							},
							function = function.keeneyed_4.StartEndTokenSynthesis,
							layer = 2
						),

						nns.neuron.hidden(
							name = "list_sentence_synthesis",
							evolvingArgumentsDictionary = {
								"grammattical_harshness": 50,
							},
							function = function.keeneyed_4.WordListingSynthesis,
							layer = 3
						),

						nns.neuron.hidden(
							name = "associated_outputs_synthesis",
							evolvingArgumentsDictionary = {
								"enable_hardware_output": False,
								"enable_audible_outputs": False
							},
							function = function.keeneyed_4.AssociatedOutputsSynthesis,
							layer = 3
						),

						nns.neuron.hidden(
							name = "textual_output_synthesis",
							evolvingArgumentsDictionary = {
								"enable_asterisk_notation": True,
								"enable_visual_notation": False
							},
							function = function.keeneyed_4.TextualOutputsSynthesis,
							layer = 4
						),

						nns.neuron.hidden(
							name = "non_textual_outputs_synthesis",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.NonTextualOutputsSynthesis,
							layer = 4
						),

						nns.neuron.output(
							name = "output",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.PassFunction,
							layer = 5
						),
						])
				
				except Exception as e:
					raise FormattingError(f"[ERROR CODE 54] Error occurred during Keeneyed-4 AGI setup: {e}")
				
				print("complete.")
	class preformattedAGIModules:
		pass
