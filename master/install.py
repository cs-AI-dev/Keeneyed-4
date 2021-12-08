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
		wd = dire["text"]
		with open(wd + "/keeneyed_4/README.md", "w") as f:
			f.write(requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/README.md?token=ATFFVVO2QONUGH3JO3PMWE3BWET72").text)
		with open(wd + "/keeneyed_4/EULA.md", "w") as f:
			f.write(requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/EULA.md?token=ATFFVVKJPPPNDNIY6EJDVO3BWEUD4").text)
		with open(wd + "/keeneyed_4/acc.py", "w") as f:
			f.write(requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/acc.py?token=ATFFVVL3XSKOJGABE5XE2T3BWEUIU").text)
			
	
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
d("Do you agree to the terms described within the System's software components' EULA?")

w_eula.mainloop()
