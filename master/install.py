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
import sys
os.system("pip install tk -q")
from tkinter import *

iw = Tk()
iw.title("Keeneyed-4 Installer")
iw.config(bg="black")

head = Label(iw, text="Keeneyed-4 Installer Wizard", bg="black", fg="white", font=("OCR A Extended", 24))
head.grid(row=1, column=1)

tb = Text(iw, bg="black", fg="white", font=("OCR A Extended", 12), width=120, height=20)
tb.grid(row=2, column=1)

dl = []

dc = 3
def d(txt):
	global dc
	dl.append(Label(iw, text=txt, bg="black", fg="white", font=("OCR A Extended", 12)))
	dl[-1].grid(row=dc, column=1)
	dc += 1

d("KEENEYED-4 ARTIFICIAL INTELLIGENCE AND SIMULATION ENGINE EULA AGREEMENT")
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

c1v = 0
c2v = 0

def c1toggle():
	if c1["text"] == "I am exempt from Section 8.2 of the EULA":
		c1["text"] = "I am not exempt from Section 8.2 of the EULA"
		c1v = 0
	else:
		c1["text"] = "I am exempt from Section 8.2 of the EULA"
		c1v = 1

def c2toggle():
	if c2["text"] == "I am exempt from Section 8.3 of the EULA":
		c2["text"] = "I am not exempt from Section 8.3 of the EULA"
		c2v = 0
	else:
		c2["text"] = "I am exempt from Section 8.3 of the EULA"
		c1v = 1

c1 = Checkbutton(iw, text="I am exempt from Section 8.2 of the EULA", variable=c1v, onvalue=1, offvalue=0, bg="black", fg="white", font=("OCR A Extended", 10), command=c1toggle)
c1.grid(row=14, column=1)
c2 = Checkbutton(iw, text='I am exempt from Section 8.3 of the EULA', variable=c2v, onvalue=1, offvalue=0, bg="black", fg="white", font=("OCR A Extended", 10), command=c2toggle)
c2.grid(row=15, column=1)

def install():
	dirask = Tk()
	dirask.title("Enter a Directory")
	dirask.config(bg="black")

	dirask_label = Label(dirask, text="Please enter a directory to install the environment to:", bg="black", fg="white", font=("OCR A Extended", 12))
	dirask_label.grid(row=1, column=1)

	dirask_entry = Entry(dirask, bg="black", fg="white", font=("OCR A Extended", 12), width=40)
	dirask_entry.grid(row=2, column=1)

	def contin():
		wd = dirask_entry.get()
		dirask.destroy()
		print("Creating directory ...", end="")
		try:
			os.rmdir(os.path.join(wd + "/keeneyed_4/"))
		except:
			try:
				for f in os.listdir(wd + "/keeneyed_4/"):
				    os.remove(os.path.join(wd + "/keeneyed_4/", f))
				os.rmdir(wd + "/keeneyed_4/")
			except:
				pass
		if not os.path.exists(wd + "/keeneyed_4/"):
			os.mkdir(wd + "/keeneyed_4/")
		print("complete.")

		print("Installing non-essentials ...")
		f = open(wd + "/keeneyed_4/README.md", "w")
		print(" | Installing readme file ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/README.md").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/EULA.md", "w")
		print(" | Installing EULA copy ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/EULA.md").text
		f.write(fd)
		f.close()

		print("complete.\n | Installing environment CLI access program ...", end="")
		f = open(wd + "/keeneyed_4/acc.py", "w")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/acc.py").text
		f.write(fd)
		f.close()
		print("complete.\nNon-essential installations complete.\n")

		print("\nInstalling drivers...")
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
		print(" | Installing master driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_master.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_cacheGeneration.py", "w")
		print(" | Installing cache generation driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_cacheGeneration.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_languageProcessing.py", "w")
		print(" | Installing language processing driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_languageProcessing.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_neuralNetworking.py", "w")
		print(" | Installing neural networking driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_neuralNetworking.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_preformattingRedprints", "w")
		print(" | Installing preformatting driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_preformattingRedprints.py").text
		f.write(fd)
		f.close()
		print("complete.")
		f = open(wd + "/keeneyed_4/master/drivers/dv_simulationEngine", "w")
		print(" | Installing simulation engine driver ...", end="")
		fd = requests.get("https://raw.githubusercontent.com/cs-AI-dev/Keeneyed-4/master/master/drivers/dv_simulationEngine.py").text
		f.write(fd)
		f.close()
		print("complete.")
		print("Driver installation complete.")
		print("Environment setup complete.")
		print(f"\nTo access your environment, go to the '{wd}/keeneyed_4/' directory and open the 'acc' application.")

	continueButton = Button(dirask, text="Confirm", bg="black", fg="white", font=("OCR A Extended", 12), command=contin)
	continueButton.grid(row=2, column=2)

	dirask.mainloop()

button_begin = Button(iw, text="Agree", bg="black", fg="white", font=("OCR A Extended", 12), command=install)
button_begin.grid(row=16, column=1)

class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self,string):
        self.text_space.insert('end', string)
        self.text_space.see('end')

sys.stdout = StdoutRedirector(tb)

iw.mainloop()

os.system("cls")
