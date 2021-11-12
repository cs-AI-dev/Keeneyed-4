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

    class BlockId:
        def __init__(bid, name, *functions, **properties):
            bid.functions = []
            for function in functions:
                bid.functions.append(function)

            bid.properties = {}
            for propertyName in properties.keys():
                bid.properties[propertyName] = properties[propertyName]

        def call(bid, targetFunction, argsList=None):
            if targetFunction in bid.functions:
                targetFunction(item, argsList)

class standardElements:
    class bids:
        air = BlockId("air", )

class axonometric:
	class Block:
		def __init__(block, blockId):
            pass

	class Layer:
		def __init__(layer, *blockStrings, euclideanZCoordinate=None):
            layer.height = euclideanZCoordinate
            xc = -1
            yc = -1
            layer.block = {}
			for blockString in blockStrings:
                xc += 1
                layer.block[xc] = {}
                for block in blockString:
                    yc += 1
                    layer.block[xc][yc]

    class AxonometricSimulation:
