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
		p_first = True
		s_first = True

	def Primary(this):
		if this.p_first == True:
			print("[ke4_master_driver] executing primary routine ...", end="")
			this.p_first == False
		else:
			print("[ke4_master_driver] reloading primary routine ...", end="")
		# Primary routine imports all drivers,
		# which includes the APIs for neural
		# networking and memory accessing.

		import dv_neuralNetworking as nns
		import dv_cacheGeneration as cg
		import dv_preformattingRedprints as pfr
		print("primary routine complete.")

	def Secondary(this):
		if this.s_first == True:
			print("[ke4_master_driver] executing secondary routine ...", end="")
			this.s_first = False
		else:
			print("[ke4_master_driver] reloading primary routine ...", end=""
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
				  
			def terminate():
				  

executeRoutine = routinesObject()

def MasterRoutine():
	executeRoutine.Primary()
	executeRoutine.Secondary()
