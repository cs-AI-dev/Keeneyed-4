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

import requests

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
				os.system("python " + sys.argv[0].split("acc.py")[0] + "projects/" + args[1] + "/master.py")
			except FileNotFoundError:
				print(f"[ke4_acc] 404: no project at {args[1]}.")
			except Exception as e:
				print(f"[ke4_acc] error occurred in project execution: {e}")
		else:
			print("[ke4_acc] invalid command syntax.")

	elif args[0] == "backup" or args[0] == "bu":
		print("[ke4_acc] starting backup ...")
		try:
			d = sys.argv[0].split("acc.py")[0]
			os.system(f"xcopy /e /i /q {d} {args[1]}")
			print(f"[ke4_acc] backup to {args[1]} complete.")
		except Exception as e:
			print(f"[ke4_acc] error occurred during backup: {e}")

	elif args[0] == "version" or args[0] == "v":
		print("[ke4_acc] Keeneyed Artificial Intelligence and Physics Simulation Engine Version 4.1.0.2")
		print("          Rework number:                 4")
		print("          API Change Number:             1")
		print("          Alteration/Addition Number:    0")
		print("          Patch Number:                  2")
		print("          Version supported:             YES")

	elif args[0] == "pull" or args[0] == "pullbackup" or args[0] == "pullbu" or args[0] == "pbu":
		print("[ke4_acc] attempting backup retrieval ...")
		try:
			d = sys.argv[0].split("acc.py")[0]
			os.system(f"xcopy /e /i /q {args[1]} {d}")
			print("[ke4_acc] data successfully pulled.")
		except Exception as e:
			print(f"[ke4_acc] error occurred during backup: {e}")

	elif args[0] == "load" or args[0] == "l" or args[0] == "loadproj" or args[0] == "loadproject":
		print("[ke4_acc] attempting to load project into environment ...")
		try:
			d = sys.argv[0].split("acc.py")[0]
			os.system(f"xcopy /e /i /q {args[1] + " " + d + "/master/projects/"}")
			print("[ke4_acc] data successfully pulled.")
		except Exception as e:
			print(f"[ke4_acc] error occurred during project loading: {e}")

	elif args[0] == "update" or args[0] == "u" or args["installupdate"]:
		print("[ke4_acc] attempting to update environment...")
		if len(args) > 1:
			print("[ke4_acc] backing up projects before reinstalling ...")
			process(["backup", args[1]])
		else:
			print("[ke4_acc] no backup location noticed in command, continuing...")
		print(" -- KEENEYED-4 ENVIRONMENT UPDATE PROCESS -- ")
		print("reinstalling non-essentials ...")
		f = open(wd + "/keeneyed_4/README.md", "w")
		print(" | reinstalling readme file ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/README.md").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/EULA.md", "w")
		print(" | reinstalling EULA copy ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/EULA.md").text
		f.write(fd)
		f.close()

		print("complete.\n | reinstalling environment CLI access program ...", end="")
		f = open(wd + "/keeneyed_4/acc.py", "w")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/acc.py").text
		f.write(fd)
		f.close()
		print("complete.\nnon-essential installations complete.\n")

		print("\nreinstalling drivers...")
		try:
			os.mkdir(wd + "/keeneyed_4/master/")
		except:
			pass
		try:
			os.mkdir(wd + "/keeneyed_4/master/drivers/")
		except:
			pass
		try:
			os.mkdir(wd + "/keeneyed_4/master/projects/")
		except:
			pass
		f = open(wd + "/keeneyed_4/master/drivers/dv_master.py",  "w")
		print(" | reinstalling master driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_master.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_cacheGeneration.py", "w")
		print(" | reinstalling cache generation driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_cacheGeneration.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_languageProcessing.py", "w")
		print(" | reinstalling language processing driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_languageProcessing.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_neuralNetworking.py", "w")
		print(" | reinstalling neural networking driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_neuralNetworking.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_preformattingRedprints", "w")
		print(" | reinstalling preformatting driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_preformattingRedprints.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_simulationEngine", "w")
		print(" | reinstalling simulation engine driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_simulationEngine.py").text
		f.write(fd)
		f.close()
		print("complete.")
		print("\n[ke4_acc] update successful.")

	elif args[0] == "createproject" or args[0] == "createproj" or args[0] == "create" or args[0] == "c":
		if len(args) == 3:
			print("[ke4_acc] creating project ...")
			try:
				os.mkdir(args[1])
				f = open(args[1] + "/project-info.ke4.dat", "w+")
				f.write("? name " + args[2])
				f.close()
				f = open(args[1] + "/master.py", "w+")
				f.write(f"# {args[2]} master callback")
			except FileExistsError:
				print("[ke4_acc] a directory already exists at that directory.")
			except FileNotFoundError:
				print("[ke4_acc] 404: file not found. see error handling docs on the Keeneyed-4 wiki.")
			except Exception as e:
				print(f"[ke4_acc] error occurred: {e}")
		else:
			print("[ke4_acc] invalid syntax.")


	elif args[0] == "q" or args[0] == "quit" or args[0] == "exit":
		exit()

	else:
		print(f"[ke4_acc] invalid command '{args[0]}'.")


while True:
	print(" ")
	process(input("ke4 @ " + str(argv[0]) + " /").split(" "))
