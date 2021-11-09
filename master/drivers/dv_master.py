# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

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
		import dv_preformattingRedprints as pfr

	def Secondary(this):
		# Secondary routine prepares the AGI
		# class. Should be treated with caution!
		# Also instantiates some other tools.

		class ArtificialGeneralIntelligence:
			def __init__(this,
						 debug = false, # Necessarily Boolean statement
						 neuralNetworkingVersion = 1.0, # Necessarily Valid NNing version float
						 selfDestructEnabled = false, # Necessarily Boolean statement
						 simulationInjectTarget = None, # Necessarily any simulation object (TextOnlySimulation, AspacialSimulation, ThreeDimensionalSimulation)
						 preformattingRedprint = None, # Necessarily any valid AGI preformat (i.e. Keeneyed-4, Razorclawed-N, Ozymandias-0, etc.) installed on the preformatting driver
						 preformatKey = pfr.maximum
						):
				print("[AGI_INSTANTIATION] INITIALIZING ARTIFICIAL GENERAL INTELLIGENCE INSTANTIATION PROCESS.")
				if debug == true: 
					print("[AGI_INSTANTIATION] DEBUG MODE ENABLED.")
				
				if preformattingRedprint == None:
					pfr.install.preformattedAGIs.keeneyed_4(this)
				else:
					if preformattingRedprint in pfr.preformats:
						if preformattingRedprint == "keeneyed":
							pfr.install.preformattedAGIs.keeneyed(this, preformatKey)
						elif preformattingRedprint == "sharpclawed":
							pfr.install.preformattedAGIs.sharpclawed(this, preformatKey)
						elif preformattingRedprint == "allknowing":
							pfr.install.
					else:
						raise pfr.InvalidPreformat(f"'{preformattingRedprint}' is not a valid preformat.")
