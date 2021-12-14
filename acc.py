# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

print("Keeneyed-4 engine internal access")
print("   Type 'q' or 'quit' to exit")

import os

import sys
from sys import argv

import math
from math import sqrt

import tqdm
from tqdm import tqdm

import time
from time import sleep as wait

drivers = ["cacheGeneration", "master", "neuralNetworking", "preformattingRedprints", "simulationEngine", "languageProcessing"]

def process(args):
	if args[0] == "test":
		if args[1] == "dv":
			if args[2] == "all":
				if not "-q" in args:
					print("[ke4_acc] testing all drivers ...")
					for driver in drivers:
						process(["test", "dv", driver])
				else:
					for driver in tqdm(drivers, desc = "[ke4_acc] testing all drivers ..."): process(["test", "dv", driver, "-q"])
			else:
				if not "-q" in args:
					print("[ke4_acc] testing compilation of driver under " + args[2] + " ...")
					try:
						os.system("python " + sys.argv[0].split("acc.py")[0] + "master/drivers/dv_" + args[2] + ".py -q")
						print("[ke4_acc] testing successful, no errors found in driver.\n")
					except Exception as e:
						print("[ke4_acc] testing failed due to error:")
						print(" > " + str(e))
				else:
					try:
						os.system("python " + sys.argv[0].split("acc.py")[0] + "master/drivers/dv_" + args[2] + ".py -q")
					except Exception as e:
						print("[ke4_acc] testing failed due to error:")
						print(" > " + str(e))
		else:
			print(f"[ke4_acc] invalid command argument '{args[1]}'.")

	elif args[0] == "e" or args[0] == "exec" or args[0] == "execute":
		for dv in [x for x in drivers if x != "master"]:
			with open(sys.argv[0].split("acc.py")[0] + "master/drivers/dv_" + dv + ".py", "r") as f: exec(f.read())
		if len(args) == 2:
			try:
				os.system("python " + sys.argv[0].split("acc.py")[0] + "projects/" + args[1])
			except FileNotFoundError:
				print(f"[ke4_acc] 404: no project at {args[1]}.")
			except Exception as e:
				print(f"[ke4_acc] error occurred in project execution: {e}")
		else:
			print("[ke4_acc] invalid command syntax.")

	elif args[0] == "backup" or args[0] == "bu":
		print("[ke4_acc] starting backup ...")
		try:
			os.system(f"xcopy /e /i /q {sys.argv[0].split("acc.py")[0]} {args[1]}")
		except Exception as e:
			print(f"[ke4_acc] error occurred during backup: {e}")

	elif args[0] == "q" or args[0] == "quit":
		exit()

	else:
		print(f"[ke4_acc] invalid command '{args[0]}'.")


while True:
	print(" ")
	process(input("ke4 @ " + str(argv[0]) + " /").split(" "))
