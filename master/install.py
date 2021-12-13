# Copyright 2021-2022 Jacob Bodell.

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

# This system requires access to the internet
# for proper function.

import os
import time
print("loading, please wait ...")
os.system("pip install requests -q")
import requests
import getpass

os.system("cls")

print("KEENEYED-4 ARTIFICIAL INTELLIGENCE AND SIMULATION ENGINE EULA AGREEMENT", 24)
print("Hello, " + getpass.getuser() + ". You will be referred to as 'You'.")
print("This program is designed to allow You to begin proper installation of the System's")
print("software components. By using this program, even if You do not complete the proper")
print("installation of the System's software components, You a) agree to and b) are hence")
print("legally bound by the terms of the EULA which governs System's software components'")
print("use until the EULA's termination.\n")
print("If You agree with all terms and conditions described within the EULA, then You may")
print("proceed with the installation of the Keeneyed-4 engine environment.\n")
print("If You do not agree with any of the terms or conditions described within the EULA,")
print("then You must immediately discontinue your use of this program and cannot continue")
print("with the proper installation of the System's software components.\n")
print("\n Type y to agree to the EULA, and type n to cancel installation.\nType r to display a copy of the EULA to which you are agreeing.\n")
while True:
	usr = input(" (y/n/r) ")
	if usr == "y":
		break
	elif usr == "n":
		exit()
	elif usr == "r":
		eula = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/EULA.md")
		i = 20
		for x in eula.text.split("\n"):
			if i == 20:
				os.system("cls")
			print(x)
			i -= 1
			if i == 0:
				i = 20
				input(" -- [ENTER] to continue reading --")
		eula.close()
	else:
		pass

wd = input("Please enter a directory to install the environment to: ")

<<<<<<< Updated upstream
def begin():
	w_eula.destroy()
	w_inst = Tk()
	w_inst.config(bg="black")

	instructions = Label(w_inst, text="Please enter a valid directory where the environment should be installed.\nAn internet connection is necessary for the installation.", bg="black", fg="white", font=("OCR A Extended", 12))
	instructions.grid(row=1, column=1, columnspan=2)

	dire = Entry(w_inst, bg="black", fg="white", font=("OCR A Extended", 12), width=25)
	dire.grid(row=2, column=1)

	def install_ke4_environment(): # Defined in here to ensure that users must agree to the EULA before using the software
		w_inst.destroy()
		print("Installing non-essentials ...", end="")
		wd = dire["text"]
		f = open(wd + "/keeneyed_4/README.md", "w+"):
		print(" | Installing readme file ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/README.md").text
		f.write(fd)
		fd.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/EULA.md", "w+"):
		print(" | Installing EULA copy ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/EULA.md").text
		f.write(fd)
		fd.close()
		print("complete.")

		print("Non-essential installations complete.\nInstalling environment CLI access program ...", end="")
		f = open(wd + "/keeneyed_4/acc.py", "w+"):
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/acc.py").text
		f.write(fd)
		fd.close()

		print("CLI access installation complete.\n\nInstalling drivers...")
		f = open(wd + "/keeneyed_4/master/drivers/dv_master.py",  "w+"):
		print(" | Installing master driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_master.py").text
		f.write(fd)
		fd.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_cacheGeneration.py", "w+"):
			print(" | Installing cache generation driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_cacheGeneration.py").text
		f.write(fd)
		fd.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_languageProcessing.py", "w+"):
		print(" | Installing language processing driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_languageProcessing.py")
		f.write(fd)
		fd.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_neuralNetworking.py", "w+"):
		print(" | Installing neural networking driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_neuralNetworking.py")
		f.write(fd)
		fd.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_preformattingRedprints", "w+"):
		print(" | Installing preformatting driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_preformattingRedprints.py")
		f.write(fd)
		fd.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_simulationEngine", "w+"):
		print(" | Installing simulation engine driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_simulationEngine.py")
		f.write(fd)
		fd.close()
		print("complete.")
		print("Driver installation complete.")
		print("Environment setup complete.")
		print(f"\nTo access your environment, type 'python {wd}/keeneyed_4/acc.py' into your command prompt.")

	go = Button(w_inst, text="Install", bg="black", fg="white", font=("OCR A Extended", 12), command=install_ke4_environment)
	go.grid(row=2, column=2)

	w_inst.mainloop()
=======
print("Installing non-essentials ...", end="")
open(wd + "/keeneyed_4/README.md", "x").close()
f = open(wd + "/keeneyed_4/README.md", "w+")
print(" | Installing readme file ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/README.md").text
f.write(fd)
fd.close()
f.close()
print("complete.")
open(wd + "/keeneyed_4/EULA.md", "x").close()
f = open(wd + "/keeneyed_4/EULA.md", "w+")
print(" | Installing EULA copy ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/EULA.md").text
f.write(fd)
fd.close()
f.close()
print("complete.")
>>>>>>> Stashed changes

print("Non-essential installations complete.\nInstalling environment CLI access program ...", end="")
open(wd + "/keeneyed_4/acc.py", "x").close()
f = open(wd + "/keeneyed_4/acc.py", "w+")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/acc.py").text
f.write(fd)
fd.close()
f.close()

print("CLI access installation complete.\n\nInstalling drivers...")
open(wd + "/keeneyed_4/master/drivers/dv_master.py", "x").close()
f = open(wd + "/keeneyed_4/master/drivers/dv_master.py",  "w+")
print(" | Installing master driver ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_master.py").text
f.write(fd)
fd.close()
f.close()
print("complete.")
open(wd + "/keeneyed_4/master/drivers/dv_cacheGeneration.py", "x").close()
f = open(wd + "/keeneyed_4/master/drivers/dv_cacheGeneration.py", "w+")
print(" | Installing cache generation driver ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_cacheGeneration.py").text
f.write(fd)
fd.close()
f.close()
print("complete.")
open(wd + "/keeneyed_4/master/drivers/dv_languageProcessing.py", "x").close()
f = open(wd + "/keeneyed_4/master/drivers/dv_languageProcessing.py", "w+")
print(" | Installing language processing driver ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_languageProcessing.py")
f.write(fd)
fd.close()
f.close()
print("complete.")
open(wd + "/keeneyed_4/master/drivers/dv_neuralNetworking.py", "x").close()
f = open(wd + "/keeneyed_4/master/drivers/dv_neuralNetworking.py", "w+")
print(" | Installing neural networking driver ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_neuralNetworking.py")
f.write(fd)
fd.close()
f.close()
print("complete.")
open(wd + "/keeneyed_4/master/drivers/dv_preformattingRedprints.py", "x").close()
f = open(wd + "/keeneyed_4/master/drivers/dv_preformattingRedprints", "w+")
print(" | Installing preformatting driver ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_preformattingRedprints.py")
f.write(fd)
fd.close()
f.close()
print("complete.")
open(wd + "/keeneyed_4/master/drivers/dv_simulationEngine.py", "x").close()
f = open(wd + "/keeneyed_4/master/drivers/dv_simulationEngine", "w+")
print(" | Installing simulation engine driver ...", end="")
fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_simulationEngine.py")
f.write(fd)
fd.close()
f.close()
print("complete.")
print("Driver installation complete.")
print("Environment setup complete.")
print(f"\nTo access your environment, type 'python {wd}/keeneyed_4/acc.py' into your command prompt.")
