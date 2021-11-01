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

class Datalattice:
	def __init__(this, **kwargs): # DL passed as "data=[initial value, modify conditions, modify]
		this.items = {}
		for key, val in kwargs.items():
			this.items[key] = {
				"currentValue": val[0],
				"modifyCondition": val[1],
				"modifyCallback": val[2]
			}
		this.feedback = None

	def SelfModify(this):
		for key in this.items:
			if this.items[key]["modifyCondition"]:
				this.items[key]["modifyCallback"]()

	def FunctionalDatalattice(this):
		this.SelfModify()
		return this.items

class OutputCache:
	def __init__(this, fromName, val, feedToTarget):
		this.timestamp = time.time()
		this.label = fromName
		this.target = feedToTarget
		this.value = val

	def extract(this):
		return (str(this.label + "_ts:" + str(this.timestamp) + ">" + this.target), this.value)

	def expunge(this):
		del this

class Neuron:
	def __init__(this, parent, name, function, feedTo, getFrom, datalattice): # Datalatt
		this.name = name
		this.operation = function
		this.feedTo = feedTo
		this.getFrom = getFrom # as obj
		this.datalattice = datalattice

	def execute(this):
		return OutputCache(this.name, this.operation(regularArgs=this.getFrom.execute(), datalatticeArgs=this.datalattice.FunctionalDatalattice()), this.feedTo)

	def getBackpropagation(this, bp):
		this.datalattice.feedback = bp

class NeuralNetwork
