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
		bid.tickCallback = None
		for function in functions:
			if type(function) == type([1, 2]) or type(function) == type((1, 2)):
				bid.tickCallback = function[0]
			else:
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
			standard_simulant = BlockId("standard_simulant", standard.functions.clearBlock, 
												  physicalTransparency=0, 
												  tensileStrength=1, 
												  color=standard.colors.chromatic.white,
												  friction=10)
			reinforced_simulant = BlockId("standard_simulant", standard.functions.clearBlock, 
													physicalTransparency=0,
													tensileStrength=10, 
													color=standard.colors.chromatic.gray,
												    friction=10)
			indestructible_simulant = BlockId("indestructible_simulant", standard.functions.clearBlock, 
														physicalTransparency=0, 
														tensileStrength=infinite, 
														color=standard.colors.chromatic.black,
													    friction=10)
			liquid_simulant = BlockId("liquid_simulant", standard.functions.clearBlock, standard.functions.displaceFluid, 
												physicalTransparency=0.40, 
												tensileStrength=0, 
												color=standard.colors.gem.sapphire,
											    friction=50)

class axonometry:
	class Block:
		def __init__(block, blockId):
			this.id = blockId
			this.blockType = blockId.name
			this.functions = blockId.functions
			this.properties = blockId.properties
			
		def executeTickCallback(block, argsList):
			this.id.tickCallback(parent, argsList)

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
					
	class AxonometricPhysicsEngine:
		def __init__(physics, physicsEngineOverride):
			law = {
				"ambient_gravity": 9.80243, # Gravity (in meters/second squared) defaults to gravity at 45 degrees latitude with elevation 1,220 meters (abt 4,000 feet)
				"ambient_temperature": 20, # Ambient temperature (in Celsius) defaults to room temperature, approximately 68 degrees Fahrenheit.
				"ambient_atmospheric_density": 1.2041, # Ambient atmospheric density (in kilograms/meter) defaults to the normal temp at 20 C and 101.325 kPa.
				"ambient_atmospheric_pressure": 101.325, # Ambient atmospheric density (in Pascals) defaults to the standard 101.325 kilopascals.
				"enable_day_night_cycle": True, # The day/night cycle defaults to be enabled.
				"toggle_always_day": True # Only matters if 'enable_day_night_cycle' is False. If day/night is disabled and this is also disabled, the simulation will resemble space.
				"day_ticks": 45000, # The number of ticks until nighttime from dawn defaults to 45 kiloticks.
				"night_ticks": 45000, # The number of ticks until daytime from dusk defaults to 45 kiloticks.
				"dawn_dusk_transition_ticks": 10000, # The number of ticks for night to transition to day and vice versa defaults to 10 kiloticks.
				"sun_brightness": 10752 # The measure of the simulation's sun's brightness (in lux) defaults to the Earth's sun's average brightness.
				"minimum_tick_length": 10 # The minimum time for a tick to take defaults to 10 milliseconds, making each second max out at 100 ticks/second.
			}

	class AxonometricSimulation:
		def __init__(simulation, *layers, **physicsOverride):
			simulationPhysics = None
			
			if len(physicsOverride.keys()) > 0:
				simulationPhysics = axonometry.AxonometricPhysicsEngine()
				simulationPhysics.law.update(physicsOverride)
			else:
				simulationPhysics = axonometry.AxonometricPhysicsEngine()
			
		
