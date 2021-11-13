# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os

infinity = infinite = "sentinel_infinity"

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
        def __init__(bid, name, *function=None, **properties):
            bid.functions = []
            for function in functions:
                bid.functions.append(function)

            bid.properties = {}
            for propertyName in properties.keys():
                bid.properties[propertyName] = properties[propertyName]

        def call(bid, targetFunction, argsList=None):
            if targetFunction in bid.functions:
                targetFunction(item, argsList)

class standard:
    class functions:
        def clearBlock(targetBlock):
            targetBlock.id = standard.bids.elements.air

    class colors:
        white = "FFFFFF"
        gray = "808080"
        black = "000000"

        red = "FF0000"
        blood_red = "800000"
        orange = "FF8000"
        yellow = "FFFF00"
        green = "008000"
        lime = "00FF00"
        blue = "0000FF"
        cyan = "00FFFF"
        indigo = "000080"
        violet = "800080"
        magenta = "FF00FF"

        class chromatic:
			chromaticReflectance = 0

            white = {"rgb"="FFFFFF", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            gray = {"rgb"="808080", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            black = {"rgb"="000000", "reflectance"=standard.colors.chromatic.chromaticReflectance}

            red = {"rgb"="FF0000", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            blood_red = {"rgb"="800000", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            orange = {"rgb"="FF8000", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            yellow = {"rgb"="FFFF00", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            green = {"rgb"="008000", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            lime = {"rgb"="00FF00", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            blue = {"rgb"="0000FF", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            cyan = {"rgb"="00FFFF", "reflectance"=standard.colors.chromatic.chromaticReflectance0}
            indigo = {"rgb"="000080", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            violet = {"rgb"="800080", "reflectance"=standard.colors.chromatic.chromaticReflectance}
            magenta = {"rgb"="FF00FF", "reflectance"=standard.colors.chromatic.chromaticReflectance}

        class metallic:
            metallicReflectance = 50

            mirror = lambda rgbColor : {"rgb"=rgbColor, "reflectance"=100}
			silver = {"rgb"="808080", "reflectance"=standard.colors.metallic.metallicReflectance}
			gold = {"rgb"="F8F800", "reflectance"=standard.colors.metallic.metallicReflectance}
			pink_gold = {"rgb"="FFE800", "reflectance"=standard.colors.metallic.metallicReflectance}

        class gem:
			# Uses classic (popular) colors based on gem
            gemReflectance = 75

			diamond = {"rgb"="EEEEFF", "reflectance"=standard.colors.gem.gemReflectance}
			onyx = {"rgb"="000000", "reflectance"=standard.colors.gem.gemReflectance}

			ruby = {"rgb"="FF0000", "reflectance"=standard.colors.gem.gemReflectance}
			topaz = {"rgb"="FF8000", "reflectance"=standard.colors.gem.gemReflectance}
			emerald = {"rgb"="00FF00", "reflectance"=standard.colors.gem.gemReflectance}
			sapphire = {"rgb"="0000FF", "reflectance"=standard.colors.gem.gemReflectance}
			amethyst

    class bids: # Tensile strength represented in kilonewtons
        class elements:
            air = BlockId("air", standard.functions.clearBlock, physicalTransparency=1, tensileStrength=0, color=None)

        class simulant:
            base_simulant = BlockId("base_simulant", standard.functions.clearBlock, physicalTransparency=0, tensileStrength=1, color=)

class axonometry:
	class Block:
		def __init__(block, blockId):
            this.id = blockId

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
