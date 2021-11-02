# Copyright 2021-2022 Jacob Bodell

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# or at the "LICENSE" file stored at the root directory in this
# repository (Keeneyed-4/LICENSE).

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
		def __init__(this, name, feedto, evolvingArgumentsDictionary, function, layer=None):
			this.type = INPUT
			this.name = name
			this.target = feedto
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.layer = layer
			
		def SendInitialData(this, inputValuesDictionary):
			this.target.standardInputs = this.function(evolvingArguments=this.evolvingArguments, standardArguments=inputValuesDictionary)
		
	class hidden:
		def __init__(this, name, feedto, evolvingArgumentsDictionary, function, layer=None):
			this.type = HIDDEN
			this.name = name
			this.target = feedto
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			
		def SendData(this):
			this.target.standardInputs = this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
			
	class output:
		def __init__(this, name, evolvingArgumentsDictionary, function, layer=None):
			this.type = OUTPUT
			this.name = name
			this.evolvingArguments = evolvingArgumentsDictionary
			this.function = function
			this.standardInputs = None
			this.layer = layer
			
		def GetFinalData(this):
			return this.function(evolvingArguments=this.evolvingArguments, standardArguments=this.standardInputs)
		
class FeedforwardNeuralNetwork:
	def __init__(this, neuronObjectList):
		this.neurons = {}
		for neuron in neuronObjectsList:
			assert type(neuron.layer) == type(1), "[ERROR] LAYER NUMBER MUST BE INTEGER OR SIMILAR"
			if not (neuron.layer in this.neurons.keys()):
				this.neurons[neuron.layer] = []
			this.neurons[neuron.layer].append(neuron)
