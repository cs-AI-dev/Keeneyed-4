# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

print("Keeneyed-4 engine internal access")
print("   Type 'q' or 'quit' to exit")

import sys
from sys import argv

import math
from math import sqrt

import tqdm
from tqdm import tqdm

import time
from time import sleep as wait

drivers = ["cacheGeneration", "master", "neuralNetworking", "preformattingRedprints", "simulationEngine"]

def process(args):
	if args[0] == "test":
		if args[1] == "dv":
			if args[2] == "all":
				print("[ke4_acc] testing all drivers ...")
				for driver in drivers:
					process(["test", "dv", driver])
			else:
				print("[ke4_acc] testing compilation of driver under " + args[2] + " ...")
				try:
					exec(open(sys.argv[0].split("acc.py")[0] + "master/drivers/dv_" + args[2] + ".py", "r").read())
					print("[ke4_acc] testing successful, no errors found in driver.")
				except Exception as e:
					print("[ke4_acc] testing failed due to error:")
					print(" > " + str(e))
		else:
			print(f"[ke4_acc] invalid command argument '{args[1]}'.")

	elif args[0] == "load":
		pass

	elif args[0] == "q" or args[0] == "quit":
		exit()
	else:
		print(f"[ke4_acc] invalid command '{args[0]}'.")


while True:
	print(" ")
	process(input("@" + str(argv[0]) + " ").split(" "))
