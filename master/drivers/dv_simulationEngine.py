# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os

infinity = infinite = "sentinel_infinity"

class ItemError(Exception):
	pass

class ItemCallbackError(Exception):
	pass

class BlockError(Exception):
	pass

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
			try:
				targetFunction(item, argsList)
			except Exception as e:
				raise ItemCallbackError("Exception occurred in item callback: " + str(e))
		else:
			raise ItemError("Target function not registered in item functions.")

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
			targetFunction(bid, argsList)

class standard:
	class functions:
		def clearBlock(targetBlock):
			targetBlock.id = standard.bids.elements.air

		def displaceFluid(targetBlock):
			# Deletes block, but then replaces a nearby air block with a fluid block
			pass

		class door: # BUG: This doesn't do anything yet
			def toggleState(targetBlock):
				targetBlock.id = None

	class colors: # BUG: Colors sometimes misbehave (sometimes). Fix RGB codes.
		generate = lambda rgbHash, reflectancePercentage, transparencyPercentage : {"rgb": rgbHash, "reflectance": reflectancePercentage}

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
			chromaticTransparency = 0

			white = {"rgb": "FFFFFF", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			gray = {"rgb": "808080", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			black = {"rgb": "000000", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}

			red = {"rgb": "FF0000", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			blood_red = {"rgb": "800000", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			orange = {"rgb": "FF8000", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			yellow = {"rgb": "FFFF00", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			green = {"rgb": "008000", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			lime = {"rgb": "00FF00", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			blue = {"rgb": "0000FF", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			cyan = {"rgb": "00FFFF", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			indigo = {"rgb": "000080", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			violet = {"rgb": "800080", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}
			magenta = {"rgb": "FF00FF", "reflectance": standard.colors.chromatic.chromaticReflectance, "transparency": standard.colors.chromatic.chromaticTransparency}

		class metallic:
			metallicReflectance = 50
			metallicTransparency = 0

			mirror = lambda rgbColor : {"rgb": "rgbColor", "reflectance": 100, "transparency": standard.colors.metallic.metallicTransparency}
			silver = {"rgb": "808080", "reflectance": standard.colors.metallic.metallicReflectance, "transparency": standard.colors.metallic.metallicTransparency}
			gold = {"rgb": "F8F800", "reflectance": standard.colors.metallic.metallicReflectance, "transparency": standard.colors.metallic.metallicTransparency}
			pink_gold = {"rgb": "FFE800", "reflectance": standard.colors.metallic.metallicReflectance, "transparency": standard.colors.metallic.metallicTransparency}

		class gem:
			# Uses classic (popular) colors based on gem
			gemReflectance = 75
			gemTransparency = 20

			diamond = {"rgb": "EEEEFF", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}
			onyx = {"rgb": "000000", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}

			ruby = {"rgb": "FF0000", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}
			topaz = {"rgb": "FF8000", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}
			emerald = {"rgb": "00FF00", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}
			sapphire = {"rgb": "0000FF", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}
			amethyst = {"rgb": "800080", "reflectance": standard.colors.gem.gemReflectance, "transparency": standard.colors.gem.gemTransparency}

	class bids: # Tensile strength represented in kilonewtons
		class elements:
			air = universal.BlockId("air", standard.functions.clearBlock, physicalTransparency=1, tensileStrength=0, color=None)

		class simulant:
			standard_simulant = universal.BlockId("standard_simulant", standard.functions.clearBlock, physicalTransparency=0, tensileStrength=1, color=standard.colors.chromatic.white)
			reinforced_simulant = universal.BlockId("standard_simulant", standard.functions.clearBlock, physicalTransparency=0, tensileStrength=10, color=standard.colors.chromatic.gray)
			indestructible_simulant = universal.BlockId("indestructible_simulant", standard.functions.clearBlock, physicalTransparency=0, tensileStrength=infinite, color=standard.colors.chromatic.black)
			liquid_simulant = universal.BlockId("liquid_simulant", standard.functions.clearBlock, standard.functions.displaceFluid, physicalTransparency=0.40, tensileStrength=0, color=standard)

class axonometry:
	class Block:
		def __init__(block, blockId):
			this.id = blockId
			this.blockType = blockId.name
			this.bl
			this.functions = blockId.

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
