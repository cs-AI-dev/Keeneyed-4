# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os
import dv_neuralNetworking as nns
import dv_languageProcessing as nlp
import dv_patternRecognition as prai

os.system("py -m pip install nltk -q")
os.system("py -m pip install -U discord -q")

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import words
import discord
import math

class InvalidPreformat(Exception):
	pass

class InvalidVersionNumber(Exception):
	pass

class FormattingError(Exception):
	pass

preformats = ["keeneyed", "sharpclawed", "ozymandias"]
maximum = "sentinel_maximum"
unknown = "sentinel_unknown"

pos = {
	"coordinating_conjunction": "CC",
	"subordinating_conjunction": "IN",

	"cardinal_numeral": "CD",
	"determiner": "DT",
	"wh_determiner": "WDT",
	"predeterminer": "PDT",
	"existential_there": "EX",
	"list_item_marker": "LS",
	"modal_auxiliary": "MD",
	"genitive_marker": "POS",
	"particle": "RP",
	"to": "TO",

	"ordinal_adjective": "JJ",
	"comparative_adjective": "JJR",
	"superlative_adjective": "JJS",

	"common_singular_noun": "NN",
	"common_plural_noun": "NNS",
	"proper_noun": "NNP",
	"wh_pronoun": "WP",

	"personal_pronoun": "PRP",
	"possessive_pronoun": "PRP$",

	"adverb": "RB",
	"comparative_adverb": "RBR",
	"superlative_adverb": "RBS",
	"wh_adverb": "WRB",

	"interjection": "UH",

	"verb": "VB",
	"past_tense_verb": "VBD",
	"present_participle_verb": "VBG",
	"past_participle_verb": "VBN",

	"non_3rd_present_tense_verb": "VBP",
	"3rd_present_tense_verb": "VBZ",
}


class sentence_type:
	imperative = "sentinel_imperative"
	interrogative = "sentinel_interrogative"
	declarative = "sentinel_declarative"
	exclamatory = "sentinel_exclamatory"

	imperative_exclamation = "sentinel_imperative_exclamation"
	interrogative_exclamation = "sentinel_interrogative_exclamation"

class implicit_return_type:
	method = "sentinel_irt_method"
	time = "sentinel_irt_time"
	reason = "sentinel_irt_reason"
	boolean = "sentinel_irt_bool"
	opinion = "sentinel_irt_opinion"
	obj = "sentinel_irt_object"

all_words = words.words()

class function:
	class keeneyed_4:
		def PassFunction(evolvingArguments, standardArguments, activationFunction, parent):
			return standardArguments

		# Input perceptron

		def SubjectPredicateDetection(evolvingArguments, standardArguments, activationFunction, parent): # Input perceptron hidden layer 1
			return {
				"subj": [x for x in nltk.pos_tag(standardArguments["inputText"]) if x[1] == "NN" or x[1] == "NNP" or x[1] == "NNS" or x[1] == "PRP"],
				"pred": [x for x in nltk.pos_tag(standardArguments["inputText"]) if x[1] == "VBD" or x[1] == "VBG" or x[1] == "VBP" or x[1] == "VBZ"]
			}

		def TokenizeByNLTK(evolvingArguments, standardArguments, activationFunction, parent): # Input perceptron hidden layer 1
			return {
				"raw": standardArguments,
				"pos_tag": nltk.pos_tag(standardArguments),
				"word_tk": nltk.word_tokenize(standardArguments),
				"sent_tk": nltk.sent_tokenize(standardArguments),
				"sub_pre": function.keeneyed_4.SubjectPredicateDetection({}, standardArguments, SCALAR, parent)
			}

		def EmphasisLevelDetection(evolvingArguments, standardArguments, activationFunction, parent): # Input perceptron hidden layer 2
			o = 0
			o -= 7 * len(standardArguments["subject_predicate_detection"]["subj"])
			o -= 5 * len(standardArguments["subject_predicate_detection"]["pred"])
			for word in standardArguments["nltk_tokenization"]["pos_tag"]:
				if word[1] == "RBS":
					o += 20
				if word[1] == "RBR":
					o += 10
				if word[1] == "RB":
					o += 5
			for sentence in standardArguments["nltk_tokenization"]["sent_tk"]:
				if list(sentence)[-1] == "!":
					o += 25

			if o < 0:
				o = 0
			elif o > 100:
				o = 100

			if o < evolvingArguments["emphasis_threshold_h2"]:
				if o < evolvingArguments["emphasis_threshold_h1"]:
					if o < evolvingArguments["emphasis_threshold_l0"]:
						if o < evolvingArguments["emphasis_threshold_l1"]:
							if o < evolvingArguments["emphasis_threshold_l2"]:
								parent.evolvingArguments["emphasis_threshold_l2"] += 1
								return "l3"
							else:
								parent.evolvingArguments["emphasis_threshold_l2"] -= 1
								parent.evolvingArguments["emphasis_threshold_l1"] += 1
								return "l2"
						else:
							parent.evolvingArguments["emphasis_threshold_l1"] -= 1
							parent.evolvingArguments["emphasis_threshold_l0"] += 1
							return "l1"
					else:
						parent.evolvingArguments["emphasis_threshold_l0"] -= 1
						parent.evolvingArguments["emphasis_threshold_h1"] += 1
						return "l0"
				else:
					parent.evolvingArguments["emphasis_threshold_h1"] -= 1
					parent.evolvingArguments["emphasis_threshold_h2"] += 1
					return "h1"
			else:
				parent.evolvingArguments["emphasis_threshold_h1"] -= 1
				return "h2"

		def StartFinishTokenDetection(evolvingArguments, standardArguments, activationFunction, parent): # Input perceptron hidden layer 2

			initialToken = []
			it_imperative = ["go", "do", "don't", "stop", "start", "should", "need"]
			it_interrogative = ["who", "what", "when", "where", "why", "how"]

			for sent in standardArguments["nltk_tokenization"]["sent_tk"]:
				sentenceInitial = sent.split(" ")[0:4]

				identified = False
				for tok in it_imperative:
					if tok in sentenceInitial:
						initialToken.append(sentence_type.imperative)
						identified = True
						break

				if identified == False:
					for tok in it_interrogative:
						if tok in sentenceInitial:
							initialToken.append(sentence_type.interrogative)
							break

			sentenceType = []

			for sentence in standardArguments["nltk_tokenization"]["raw"]:
				if list(sentence)[-3:-1] == "...":
					sentenceType.append(sentence_type.declarative)
					continue

				if list(sentence)[-3:-1] == "..?" or list(sentence)[-3:-1] == "?.." or list(sentence)[-1] == "?":
					sentenceType.append(sentence_type.interrogative)
					continue

				if list(sentence)[-2:-1] == "?!" or list(sentence)[-2:-1] == "!?":
					sentenceType.append(sentence_type.interrogative_exclamation)
					continue

				if list(sentence)[-1] == ".":
					if initialToken != unknown:
						sentenceType.append(initialToken)
						continue
					else:
						sentenceType.append(sentence_type.declarative)

			i = -1
			o = []
			for i in range(len(standardArguments["nltk_tokenization"]["sent_tk"])):
				i += 1
				o.append( ( standardArguments["nltk_tokenization"]["sent_tk"][i] , sentenceType[i] , initialToken[i] ) )

			return o

		def Keeneyed4Tokenization(evolvingArguments, standardArguments, activationFunction, parent): # Input perceptron hidden layer 2
			r = evolvingArguments["rigidity"]

			o = [] # List of lists
			so = []

			for sent in standardArguments["nltk_tokenization"]["sent_tk"]:
				for word in sent:
					# Compile a syntactic language data packet
					emphasisInfo = None
					toneInfo = None
					wnSynsetKey = None
					contextInfo = {}

					emphasisInfo = [0, 0]
					emphasisInfo[0] -= 7 * len(standardArguments["subject_predicate_detection"]["subj"])
					emphasisInfo[0] -= 5 * len(standardArguments["subject_predicate_detection"]["pred"])
					if word[1] == "RBS":
						emphasisInfo[0] += 20
					if word[1] == "RBR":
						emphasisInfo[0] += 10
					if word[1] == "RB":
						emphasisInfo[0] += 5
					for sentence in standardArguments["nltk_tokenization"]["sent_tk"]:
						if list(sentence)[-1] == "!":
							emphasisInfo[0] += 25

					if emphasisInfo[0] < 0:
						emphasisInfo[0] = 0
					if emphasisInfo[0] > 100:
						emphasisInfo[0] = 100

					if len(so) == 0:
						emphasisInfo[1] = 0
					else:
						emphasisInfo[1] += int((so[-1].emphasisInfo[1] + emphasisInfo[0]) / 2)

					if list(sent)[-3:-1] == "...":
						toneInfo.append(sentence_type.declarative)

					if list(sent)[-3:-1] == "..?" or list(sentence)[-3:-1] == "?.." or list(sentence)[-1] == "?":
						toneInfo.append(sentence_type.interrogative)

					if list(sent)[-2:-1] == "?!" or list(sentence)[-2:-1] == "!?":
						toneInfo.append(sentence_type.interrogative_exclamation)

					if list(sent)[-1] == ".":
						if initialToken != unknown:
							toneInfo.append(initialToken)
						else:
							toneInfo.append(sentence_type.declarative)

					wnSynsetKey = [x for x in wn.synsets(word)]
					contextInfo["sentenceEmphasis"] = emphasisInfo
					contextInfo["hypernyms"] = []
					for x in wn.synsets(word):
						if x.path_similarity(wn.synsets(word)[1]) < rigidity:
							contextInfo["hypernyms"].append(x.hypernyms())
							parent.evolvingArgumentsDictionary["rigidity"] += 1
						else:
							parent.evolvingArgumentsDictionary["rigidity"] -= 1
					contextInfo["hyponyms"] = []
					for x in wn.synsets(word):
						if x.path_similarity(wn.synsets(word)[1]) < rigidity:
							contextInfo["hyponyms"].append(x.hyponyms())
							parent.evolvingArgumentsDictionary["rigidity"] -= 1
						else:
							parent.evolvingArgumentsDictionary["rigidity"] += 1

					so.append(nlp.SemanticLanguageData(emphasisInfo, toneInfo, wnSynsetKey, **contextInfo))

				o.append(so)
				so = []
			return o

		def ToneDetection(evolvingArguments, standardArguments, activationFunction, parent):
			tok_ke4 = standardArguments["keeneyed_4_forward_tokenization"]

			toneEmphasisLevel = None

			for sent in tok_ke4:
				o = 0

				for word in sent:
					o += word.emphasisInfo[0]
					o += word.emphasisInfo[1]

				if o / len(sent) < evolvingArguments["emphasis_threshold_h2"]:
					if o / len(sent) < evolvingArguments["emphasis_threshold_h1"]:
						if o / len(sent) < evolvingArguments["emphasis_threshold_l0"]:
							if o / len(sent) < evolvingArguments["emphasis_threshold_l1"]:
								if o / len(sent) < evolvingArguments["emphasis_threshold_l2"]:
									if parent.evolvingArguments["emphasis_threshold_l2"] < 100:
										parent.evolvingArguments["emphasis_threshold_l2"] += 1
									toneEmphasisLevel = "l3"
								else:
									if parent.evolvingArguments["emphasis_threshold_l2"] > 0:
										parent.evolvingArguments["emphasis_threshold_l2"] -= 1
									if parent.evolvingArguments["emphasis_threshold_l1"] < 100:
										parent.evolvingArguments["emphasis_threshold_l1"] += 1
									toneEmphasisLevel = "l2"
							else:
								if parent.evolvingArguments["emphasis_threshold_l1"] > 0:
									parent.evolvingArguments["emphasis_threshold_l1"] -= 1
								if parent.evolvingArguments["emphasis_threshold_l0"] < 100:
									parent.evolvingArguments["emphasis_threshold_l0"] += 1
								toneEmphasisLevel = "l1"
						else:
							if parent.evolvingArguments["emphasis_threshold_l0"] > 0:
								parent.evolvingArguments["emphasis_threshold_l0"] -= 1
							if parent.evolvingArguments["emphasis_threshold_h1"] < 100:
								parent.evolvingArguments["emphasis_threshold_h1"] += 1
							toneEmphasisLevel = "l0"
					else:
						if parent.evolvingArguments["emphasis_threshold_h1"] > 0:
							parent.evolvingArguments["emphasis_threshold_h1"] -= 1
						if parent.evolvingArguments["emphasis_threshold_h2"] < 100:
							parent.evolvingArguments["emphasis_threshold_h2"] += 1
						toneEmphasisLevel = "h1"
				else:
					if parent.evolvingArguments["emphasis_threshold_h1"] > 0:
						parent.evolvingArguments["emphasis_threshold_h1"] -= 1
					toneEmphasisLevel = "h2"

				return o

		def SentenceConstruction(evolvingArguments, standardArguments, activationFunction, parent):
			tk = function.keeneyed_4.TokenizeByNLTK({}, parent.currentInput, SCALAR, parent)
			alldata = {}

			for x in tk["pos_tag"]:
				if x[1] in alldata.keys():
					alldata[x[1]] += 1
				else:
					alldata[x[1]] = 1

			# Might look like random garbage but it's standard deviation
			deviation = math.sqrt( (sum([x - (sum(alldata.values()) / len(alldata.values())) for x in alldata.values()]) ^ 2) / len(alldata.values()) )

		def SyntacticLanguageConstruction(evolvingArguments, standardArguments, activationFunction, parent):
			pass

		def ImplicitReturnTypeDetection(evolvingArguments, standardArguments, activationFunction, parent):
			pass

		# Central neocortex (unfinished?)

		# Output perceptron

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
	class preformattedAGI:
		class versions:
			keeneyed = [4]
		def keeneyed(parent, version):

			# The namesake of this entire engine, the Keeneyed-4 general intelligence is
			# designed to support several neural nets, each leading into a central neocortex which
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
						# Input
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
							evolvingArgumentsDictionary = {},
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

						# H3
						nns.neuron.hidden(
							name = "tone_analysis",
							evolvingArgumentsDictionary = { # Threshold values for emphasis lv detection
								"emphasis_threshold_l2": 20,
								"emphasis_threshold_l1": 40,
								"emphasis_threshold_l0": 60,
								"emphasis_threshold_h1": 80,
								"emphasis_threshold_h2": 100
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

						# H4
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

						# Output
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
						# Input
						nns.neuron.input(
							name = "syntactic_nlp",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.PassFunction,
							layer = 0
						),

						# H1
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

						# H2
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

						# H3
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

						# H4
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

						# Output
						nns.neuron.output(
							name = "output",
							evolvingArgumentsDictionary = {},
							function = function.keeneyed_4.PassFunction,
							layer = 5
						),
						])

				except Exception as e:
					raise FormattingError(f"[ERROR CODE 54] Error occurred during Keeneyed-4 AGI setup: {e}")

				print("complete.\n        central neural neocortext ...", end="")

	class AGIModule:
		def DiscordInteraction(agi, authkey):
			pass
