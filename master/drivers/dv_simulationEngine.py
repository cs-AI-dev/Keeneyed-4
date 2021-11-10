# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os

class universal:
	class Item:
		def __init__(item, parentSimulation, *functions, **properties): # Input functions need a parent arg
			item.functions = []
			for function in functions:
				item.functions.append(function)
				
			item.properties = {}
			for propertyName in properties.keys():
				item.properties[propertyName] = properties[propertyName]
				
		def call(item, targetFunction, argsList=None):
			if targetFunction in item.functions:
				targetFunction(item, argsList)

class axonometric:
	class Block:
		def __init__(block, 
	class Layer:
		def __init__(layer, *blockStrings):
			
