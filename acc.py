# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
from sys import argv

import math
from math import sqrt

import tqdm
from tqdm import tqdm

import time
from time import sleep as wait

while True:
    print("enter keeneyed-4 system access code.")
    if input(":") != str(int(sqrt(416119175329))) + "JB":
        print("invalid access code, try again in 120 seconds.")
        for x in tqdm(range(120), desc="please wait two minutes to try again", ascii="_█"): wait(1)
    else:
        break

while True:
    print(" ")
    args = input("@" + str(argv[0]) + " ").split(" ")
    if args[0] == "test":
        if args[1] == "dv":
            print("[ke4_acc] testing compilation of driver under " + args[2] + " ...")
            try:
                exec(open(sys.argv[0].split("acc.py")[0] + "master/drivers/dv_" + args[2] + ".py", "r").read())
                print("[ke4_acc] testing successful, no errors found in driver.")
            except Exception as e:
                print("[ke4_acc] testing failed due to error:")
                print(" > " + str(e))
        else:
            print(f"[ke4_acc] invalid command argument '{args[1]}'.")
    else:
        print(f"[ke4_acc] invalid command '{args[0]}'.")
