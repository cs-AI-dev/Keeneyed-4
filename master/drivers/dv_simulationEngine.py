# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os
import time

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
			raise SpaceError("No physics engine callback declared (see howto for a default).")
		else:
			space.physicsEngine = PhysicsEngine(space, physicsEngineCallback)

	def tick(space, **auxiliaryArgsX):
		space.physicsEngine.tick(**auxiliaryArgsX)

class Point:
	def __init__(point, name=None, **coordValues):
		point.name
		point.coordinate = coordValues

	def add(point, coord, value):
		if coord in point.coordinate.keys():
			point.coordinate[coord] += value
			return True
		else:
			raise PointError(f"Selected coordinate '{coord}' not registered on selected point.")

class Surface:
	def __init__(surface, *points):
		if not ( ( len(points) == 3 ) or ( len(points) == 4 ) ):
			raise SurfaceError(f"Invalid number of points ({str(len(points))}) for surface, to render more see howto.")
