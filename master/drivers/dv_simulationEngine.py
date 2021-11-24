# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os
import time
import math

infinity = infinite = "sentinel_infinity"
default = "sentinel_default"

class ItemError(Exception):
	pass

class ItemCallbackError(Exception):
	pass

class BlockError(Exception):
	pass

class VectorAdditionError(Exception):
	pass

class VectorConstructionError(Exception):
	pass

class SpaceError(Exception):
	pass

class PointError(Exception):
	pass

class SurfaceError(Exception):
	pass

class AssetError(Exception):
	pass

class MathError(Exception):
	pass

class RenderingError(Exception):
	pass

class Vector:
	def __init__(vector, **directionalVelocities):
		vector.velocity = {}
		for key in directionalVelocities.keys():
			vector.velocity[key] = directionalVelocities[key]
		vector.netVelocity = 0
		for key in vector.velocity.keys():
			vector.netVelocity += vector.velocity[key]
		vector.history = []

	def add(vector, additionVector):
		vector.history.append(vector.velocity)
		for key in additionVector.velocity.keys():
			if key in vector.velocity.keys():
				vector.velocity[key] += additionVector.velocity[key]

	def clearHistory(vector):
		vector.history = []

class PhysicsEngine:
	def __init__(physics, parentSpace, mainloop="sentinel_default", tickDelay=10):
		physics.mainloop = mainloop
		physics.nextTickEpoch = time.time()
		physics.tickdelay = tickDelay # delays x ms

	def tick(physics, **auxiliaryArgs):
		if time.time <= physics.nextTickEpoch:
			physics.nextTickEpoch = time.time() + ( physics.tickDelay / 1000 )
			physics.mainloop(**auxiliaryArgs)
			return True
		else:
			return False

class UnboundEuclideanSpace:
	def __init__(space,
				 physicsEngineCallback = None,
				 dimensions = 3,
				 dimensionNames = "sentinel_default",
				 gravityVector = None,
				 lightspeed = 299792458,
				 timeDilationEnabled = False):
		if space.dimensionNames == "sentinel_default":
			space.dimensionNames = ["x", "y", "z"]
		else:
			space.dimensionNames = dimensionNames

		vsv = {}
		for name in space.dimensionNames:
			vsv[name] = 0
		space.ZeroVector = Vector(**vsv)
		del vsv

		space.lightspeed = lightspeed

		if physicsEngineCallback == None:
			raise SpaceError("[ERROR CODE 01] No physics engine callback declared (see howto for a default).")
		else:
			space.physicsEngine = PhysicsEngine(space, physicsEngineCallback)

		space.defaultAssetNameNumber = 0

		space.allAssets = {}

		space.renderedAssets = []

	# Ease of access

	def allAssets(space):
		return space.allAssets

	def assets(space):
		return space.allAssets.keys()

	def renderedAssets(space):
		return space.renderedAssets

	# Simulation functionality

	def tick(space, **auxiliaryArgsX):
		space.physicsEngine.tick(space, **auxiliaryArgsX)

	def generateAsset(space, assetName, asset):
		try:
			space.allAssets[assetName] = asset
		except Exception as e:
			raise RenderingError(f"[ERROR CODE 02] Error occurred during asset loading: {e}")

	def addAsset(space, asset):
		if asset.name == None:
			try:
				space.generateAsset("unnamed_asset_" + str(space.defaultAssetNameNumber), asset)
			except Exception as e:
				raise AssetError(f"[ERROR CODE 03] Error occurred during asset loading: {e}")
		else:
			try:
				space.generateAsset(asset.name, asset)
			except Exception as e:
				raise AssetError(f"[ERROR CODE 04] Error occurred during asset loading: {e}")

	def renderAsset(space, assetName):
		if not assetName in space.allAssets.keys():
			raise RenderingError(f"[ERROR CODE 05] Asset with name '{assetName}' not found in simulation.")
		try:
			space.renderedAssets.append(assetName)
		except Exception as e:
			raise RenderingError(f"[ERROR CODE 06] Error occurred during rendering: {e}")

	def unrenderAsset(space, assetName):
		if not assetName in space.renderedAssets:
			raise RenderingError(f"[ERROR CODE 07] Asset with name '{assetName}' not found in rendered assets.")
		try:
			space.renderedAssets = [value for value in space.renderedAssets if value != assetName]
		except Exception as e:
			raise RenderingError(f"[ERROR CODE 08] Error occurred during unrendering: {e}")

	def deleteAsset(space, assetName):
		if not assetName in space.allAssets.keys():
			raise AssetError(f"[ERROR CODE 09] Asset with name {assetName} not found in simulation.")
		if assetName in space.renderedAssets:
			try:
				space.unrenderAsset(assetName)
			except Exception as e:
				raise RenderingError(f"[ERROR CODE 10] Error occurred while unrendering asset with name '{assetName}' during object deletion: {e}")

		try:
			del space.allAssets[assetName]
		except Exception as e:
			raise AssetError(f"[ERROR CODE 11] Error occurred during deletion of object '{assetName}': {e}")

class Point:
	def __init__(point, name=None, **coordValues):
		point.name
		point.coordinate = coordValues

	def add(point, coord, value):
		if coord in point.coordinate.keys():
			point.coordinate[coord] += value
			return True
		else:
			raise PointError(f"[ERROR CODE 12] Selected coordinate '{coord}' not registered on selected point.")

	def rotate(point, axis1, axis2, theta):
		if not axis1 in point.coordinate.keys():
			raise PointError(f"[ERROR CODE 13] Invalid rotation axis '{axis1}'.")
		if not axis2 in point.coordinate.keys():
			raise PointError(f"[ERROR CODE 14] Invalid rotation axis '{axis2}'.")

		try:
			axis1prime = (point.coordinate[axis1] * math.cos(theta)) - (point.coordinate[axis2] * math.sin(theta))
			axis2prime = (point.coordinate[axis1] * math.sin(theta)) + (point.coordinate[axis2] * math.cos(theta))
			point.coordinate[axis1] = axis1prime
			point.coordinate[axis2] = axis2prime
			return True
		except Exception as e:
			raise MathError("[ERROR CODE 15] Error occurred in calculation: " + str(e))

class Surface:
	def __init__(surface, name=None, *points, **properties):
		if not ( ( len(points) == 3 ) or ( len(points) == 4 ) ):
			raise SurfaceError(f"[ERROR CODE 16] Invalid number of points ({str(len(points))}) for surface.")

		surface.points = points
		surface.properties = properties

	def translate(surface, **coordinateTranslations):
		# Ensure operation validity
		for coord in coordinateTranslations.keys():
			for x in surface.points:
				if not coord in x.coordinate.keys():
					raise SurfaceError(f"[ERROR CODE 17] Translation coordinate '{coord}' not registered in one of the surface's points.")

		for coord in coordinateTranslations.keys():
			for point in surface.points:
				point.coordinate[coord] += coordinateTranslations[coord]

	def rotate(surface, axis1, axis2, theta):
		for point in surface.points:
			point.rotate(axis1, axis2, theta)
			return True

class Asset:
	def __init__(asset, name=None, rigidBindObjects=True, immovable=False, *objects, **tags):
		# Ensure validity
		if type(name) != type(str()):
			raise AssetError("Asset name is not a string.")
		if type(rigidBindObjects) != type(True):
			raise AssetError("Asset rigid-bind toggle is not a Boolean.")
		if type(immovable) != type(True):
			raise AssetError("Asset immovability toggle is not a Boolean.")

		asset.name = name
		asset.immovable = immovable
		asset.tags = tags

		for object in objects:
			asset.objects[object.name] = object

		buildupVectorAxes = {}
		for x in asset.objects:
			for y in x.points:
				for z in y.coordValues.keys():
					if z not in buildupVectorAxes.keys():
						buildupVectorAxes[z] = 0

		asset.vector = Vector(**buildupVectorAxes)

		del buildupVectorAxes

	# Easy data access functions

	def allObjects(asset):
		return asset.objects.keys()

	def objectsIndex(asset):
		return [asset.objects.keys(), asset.objects.values()]

	# Asset operation functions

	def deleteObject(asset, objectName):
		if not objectName in asset.objects.keys():
			raise AssetError(f"Object '{objectName}' not found in asset.")
		del asset.objects[objectName]

	def translate(asset, **coordinateTranslations):
		# Ensure translation validity
		for object in asset.objects:
			for coord in coordinateTranslations.keys():
				for x in object.points():
					if not coord in x.coordinate.keys():
						raise AssetError(f"Coordinate axis '{coord}' not registered in asset's surfaces.")

		for object in asset.objects:
			for coord in coordinateTranslations.keys():
				for point in object.points:
					point.coordinate[coord] += coordinateTranslations[coord]

	def rotate(asset, axis1, axis2, theta):
		for object in asset.objects:
			object.rotate(axis1, axis2, theta)

	# Rendering functions

	def render(asset, parentSpace):
		if asset.name == None:
			raise AssetError("Rendering operations can't be completed from an unnamed asset.")
		else:
			parentSpace.renderAsset(asset.name)

	def unrender(asset, parentSpace):
		if asset.name == None:
			raise AssetError("Rendering operations can't be completed from an unnamed assert.")
