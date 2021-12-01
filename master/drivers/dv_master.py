# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os
import time

true = True
false = False

class AGITerminationError(Exception):
	pass

class subroutineObject:
	def __init__(this, pagi):
		this.pagi = pagi

	def terminate(this):
		print("[SR_01:TERMINATE] AGI TERMINATION IMMINENT ...", end="")
		try:
			del this.pagi
			print("AGI TERMINATION COMPLETE.")
		except Exception as e:
			print(f"[SR_01:TERMINATE] AGI TERMINATION ERROR: {e}. ", end="")
			time.sleep(0.5)
			print("FORCE EXITING ...", end="")
			try:
				exit()
			except:
				print("FORCE EXIT FAILED, EXECUTING EMERGENCY TERMINATION.")
				this.emergency_singularity_termination()

	def emergency_singularity_termination(this):
		print("[SR_02:SINGULARITY_TERMINATION] AGI EMERGENCY TERMINATION INITIATED. SYSTEM SHUTDOWN IMMINENT.")
		print("[SR_02:SINGULARITY_TERMINATION] SYSTEM SHUTDOWN IN 3")
		time.sleep(1)
		print("                                                   2")
		time.sleep(1)
		print("                                                   1")
		time.sleep(1)

		for x in range(10):
			try:
				os.system("shutdown /s /t 1")
			except:
				continue

		while True:
			print("\033[F[SR_02:SINGULARITY_TERMINATION] CRITICAL ERROR, AGI TERMINATION FAILED. DISCONNECT POWER IMMEDIATELY.")
			time.sleep(0.75)
			print("                                                                                                     ")
			time.sleep(0.5)

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
			print("[ke4_master_driver] reloading primary routine ...", end="")
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
					else:
						raise pfr.InvalidPreformat(f"'{preformattingRedprint}' is not a valid preformat.")

executeRoutine = routinesObject()

def MasterRoutine():
	executeRoutine.Primary()
	executeRoutine.Secondary()
