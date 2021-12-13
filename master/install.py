# Copyright 2021-2022 Jacob Bodell.

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

# This system requires access to the internet
# for proper function.

import os
print("loading, please wait ...")
os.system("pip install requests -q")
import requests
os.system("pip install tk -q")
from tkinter import *

w_eula = Tk()
w_eula.config(bg="black")

txt = Frame(w_eula, bg="black")
txt.grid(row=1, column=1)

ui = Frame(w_eula, bg="black")
ui.grid(row=2, column=1)

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

btn_yes = Button(ui, text="Agree", bg="black", fg="white", font=("OCR A Extended", 14), command=begin)

lines = []
rn = 0
def d(text, size=12):
	lines.append(Label(txt, text=text, bg="black", fg="white", font=("OCR A Extended", size), anchor=w))
	lines[-1].grid(row=rn, column=1)
	rn += 1

d("KEENEYED-4 ARTIFICIAL INTELLIGENCE AND SIMULATION ENGINE EULA AGREEMENT", 24)
d("This program is designed to allow You to begin proper installation of the System's")
d("software components. By using this program, even if You do not complete the proper")
d("installation of the System's software components, You a) agree to and b) are hence")
d("legally bound by the terms of the EULA which governs System's software components'")
d("use until the EULA's termination.")
d("If You agree with all terms and conditions described within the EULA, then You may")
d("proceed with the installation of the Keeneyed-4 engine environment.")
d("If You do not agree with any of the terms or conditions described within the EULA,")
d("then You must immediately discontinue your use of this program and cannot continue")
d("with the proper installation of the System's software components.")

w_eula.mainloop()
