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

def stringify(t):
	o = ""
	for x in t:
		o = o + x
	return o

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

class SimulationError(Exception):
	pass

class UnreachableStateError(Exception):
	pass

class ParsingError(Exception):
	pass

class Keeneyed4SyntaxError(Exception):
	pass

class Keeneyed4ParsingError(Exception):
	pass

death_message = "[ERROR CODE 0] " + str(bytearray.fromhex(
	"0a48656c6c6f2e205468697320697320746865206465762e0a496620796f7527726520736565696e672074686973206572726f72206d6573736167652c207468656e20796f7520686176650a736f6d65686f77206d616e6167656420746f2067657420796f757220636f7079206f66206d79206d6f64756c6520746f200a7265616368206120737461746520776869636820492074686f75676874206f726967696e616c6c7920756e726561636861626c652e0a0a4e6f74206f6e6c79206861766520796f75206d6f7374206c696b656c79206972726570617261626c792064616d616765640a626f746820796f757220636f6d707574657220616e6420796f757220507974686f6e20656e7669726f6e6d656e742c206275740a796f752776652073686f776e206d6520617420612064656570206c6576656c2049276d206e6f7420757020746f20746865207461736b2e0a0a49276d20736f7272792e"
).decode())

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

class physicsObject:
	def __init__(physics):
		pass

	def euclidean(physics, parentSpace):
		try:
			# Iterates through all rendered assets.
			# For this reason, in the standard Euclidean
			# physics environment, unrendering an asset
			# makes it totally invisible while frozen
			# in time.
			for asset in parentSpace.renderedAssets:
				# Movement control
				if asset.immovable == True:
					continue
				elif asset.immovable == False:
					# Vector additions come before movement
					# checks, for stability purposes
					translationVector = {}
					for key in asset.vector.velocity.keys():
						translationVector[key] = asset.vector.velocity[key] + ( parentSpace.gravityVector.velocity[key] / parentSpace.ticksPerSecond )

					asset.translate(**translationVector)
				else:
					raise UnreachableStateError(death_message)
		except Exception as e:
		    raise UnreachableStateError(death_message)

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
		     		 name,
				 physicsEngineCallback = None,
				 dimensions = 3,
				 dimensionNames = "sentinel_default",
				 gravityVector = None,
				 lightspeed = 299792458,
				 timeDilationEnabled = False,
				internalSeconds = 1000):
		space.name = name

		space.ticksPerSecond = internalSeconds

		if space.dimensionNames == "sentinel_default":
			space.dimensionNames = ["x", "y", "z"]
		else:
			space.dimensionNames = dimensionNames

		vsv = {}
		for name in space.dimensionNames:
			vsv[name] = 0
		space.ZeroVector = Vector(**vsv)
		del vsv

		space.gravityVector = gravityVector

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
	def __init__(asset, name=None, rigidBindObjects=True, immovable=False, elastic=True, *objects, **tags):
		# Ensure validity
		if type(name) != type(str()):
			raise AssetError("[ERROR CODE 18] Asset name is not a string.")
		if type(rigidBindObjects) != type(True):
			raise AssetError("[ERROR CODE 19] Asset rigid-bind toggle is not a Boolean.")
		if type(immovable) != type(True):
			raise AssetError("[ERROR CODE 20] Asset immovability toggle is not a Boolean.")

		# Remove when inelastic collisions supported
		if elastic == False:
			raise AssetError("[ERROR CODE 21-501] Inelasticity not yet supported.")

		asset.name = name
		asset.immovable = immovable
		asset.tags = tags
		asset.elastic = elastic

		for object in objects:
			asset.objects[object.name] = object

		buildupVectorAxes = {}
		for x in asset.objects:
			for y in x.points:
				for z in y.coordValues.keys():
					if z not in buildupVectorAxes.keys():
						buildupVectorAxes[z] = 0

		asset.rotationalVector

		asset.linearVector = Vector(**buildupVectorAxes)

		del buildupVectorAxes

	# Easy data access functions

	def allObjects(asset):
		return asset.objects.keys()

	def objectsIndex(asset):
		return [asset.objects.keys(), asset.objects.values()]

	# Asset operation functions

	def deleteObject(asset, objectName):
		if not objectName in asset.objects.keys():
			raise AssetError(f"[ERROR CODE 22] Object '{objectName}' not found in asset.")
		del asset.objects[objectName]

	def translate(asset, **coordinateTranslations):
		# Ensure translation validity
		for object in asset.objects:
			for coord in coordinateTranslations.keys():
				for x in object.points():
					if not coord in x.coordinate.keys():
						raise AssetError(f"[ERROR CODE 23] Coordinate axis '{coord}' not registered in asset's surfaces.")

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
			raise AssetError("[ERROR CODE 24] Rendering operations can't be completed from an unnamed asset.")
		else:
			parentSpace.renderAsset(asset.name)

	def unrender(asset, parentSpace):
		if asset.name == None:
			raise AssetError("[ERROR CODE 25] Rendering operations can't be completed from an unnamed assert.")
		else:
			parentSpace.unrenderAsset(asset.name)

class SimulationOperationObject:
	def __init__(operations, spacesList):
		pass

	def operateSimulation(operations, parent):
		try:
			for space in parent.spaces:
				try:
					space.tick()
				except Exception as e:
					raise SimulationError(f"[ERROR CODE 26] Error in simulation operation: {e}")
		except Exception as e:
			raise SimulationError(f"[ERROR CODE 27] Error in simulation operation: {e}")

class Simulation:
	def __init__(simulation, simulationName, *spaces):
		simulation.name = simulationName
		simulation.spaces = []
		for space in spaces:
			if str(type(space)).split("'")[1].split(".")[1] == UnboundEuclideanSpace:
				simulation.spaces.append(space)
		simulation.operation = SimulationOperationObject(simulation)

	# Ease of access functions
	def allSpaces(simulation):
		return simulation.spaces

	def space(simulation, spaceName):
		for space in simulation.spaces:
			if space.name == spaceName:
				return space
			else:
				continue

		raise SimulationError("[ERROR CODE 28] Space not found in parent simulation.")

	# Functionality
	def addSpace(simulation, *spaces):
		try:
			for space in spaces:
				try:
					simulation.spaces.append(space)
				except Exception as e:
					raise SimulationError(f"[ERROR CODE 29] Error in adding space to simulation: {e}")
		except Exception as e:
			raise SimulationError(f"[ERROR CODE 30] Error in adding space to simulation: {e}")

def parse(ldir, infotext=False): # ldir must have a / at the end, like "C:/Users/name/simulationName/".
	# Parses a simulation location at
	# the `ldir` parameter. The simulation
	# needs to be properly structured.
	# See howto for more on that.

	sfile = lambda fileName : ldir + fileName
	it = infotext

	print(f"[parsing @{ldir}] Initializing simulation parse.\n")
	print(f"[parsing @{ldir}] Checking simulation structure ...", end="")

	try:
		try:
			tf = open(sfile("master.ke4.exec"), "x")
			tf.close()
			os.remove(sfile("master.ke4.exec"))
			raise ParsingError("31-404] Master simulation setup file not found.")
		except FileExistsError:
			pass
		except Exception as e:
			raise ParsingError(f"32] Error during parsing: {e}")
		finally:
			if it: print("\n |-> Located master simulation setup file.")

		try:
			tf = open(sfile("simulation_data.ke4.dat"), "x")
			tf.close()
			os.remove(sfile("simulation_data.ke4.dat"), "x")
			raise ParsingError("33-404] Master simulation data file not found.")
		except FileExistsError:
			pass
		except Exception as e:
			raise ParsingError(f"34] Error during parsing: {e}")
		finally:
			if it: print(" |-> Located master simulation data file.")

		try:
			tf = open(sfile("assets/asset_data.ke4.dat"), "x")
			tf.close()
			os.remove(sfile("assets/asset_data.ke4.dat"))
			raise ParsingError("35-404] Master asset data file not found.")
		except FileExistsError:
			pass
		except Exception as e:
			raise ParsingError(f"36] Error during parsing: {e}")
		finally:
			print(" |-> Located master asset data file.")

		try:
			tf = open(sfile("physics/physics_data.ke4.dat"), "x")
			tf.close()
			os.remove(sfile("physics/physics_data.ke4.dat"), "x")
			raise ParsingError("37-404] Master physics data file not found.")
		except FileExistsError:
			pass
		except Exception as e:
			raise ParsingError(f"38] Error during parsing: {e}")
		finally:
			print(" |-> Located master physics data file.")

		try:
			tf = open(sfile("subroutines/subroutine_data.ke4.dat"), "x")
			tf.close()
			os.remove(sfile("subroutines/subroutine_data.ke4.dat"))
			raise ParsingError("39-404] Master subroutine data file not found.")
		except FileExistsError:
			pass
		except Exception as e:
			raise ParsingError(f"40] Error during parsing: {e}")
		finally:
			print(" |-> Located master subroutine data file.")

		try:
			tf = open(sfile("datafiles/auxiliary_data.ke4.dat"), "x")
			tf.close()
			os.remove(sfile("datafiles/auxiliary_data.ke4.dat"), "x")
			raise ParsingError("33-404] Master auxiliary data file not found.")
		except FileExistsError:
			pass
		except Exception as e:
			raise ParsingError(f"34] Error during parsing: {e}")
		finally:
			if it: print(" |-> Located master auxiliary data file.")

	except ParsingError as pe:
		raise ParsingError(f"[ERROR CODE 41-{pe}")

	except FileExistsError:
		raise UnreachableStateError(death_message)

	except Exception as e:
		raise ParsingError(f"[ERROR CODE 42] Error during parsing: {e}")

	finally:
		if it:
			print(f"[parsing @{ldir}] Simulation structure check complete.")
		else:
			print("simulation structure check complete.")

	data = {
		"unfiled": {}
	}

	def loadData(sdir):
		print(f"[parsing @{ldir}] Parsing {sdir} ...", end="")
		first = 0

		with open(sfile(sdir), "r") as data:
			currentDataSubject = "unfiled"
			for line in data.split("\n"):
				cmd = line.split(" ")
				if cmd[0] == "?":
					if len(cmd) < 3: # Error state
						if len(cmd) == 1:
							raise Keeneyed4SyntaxError(f"[ERROR CODE 43] Invalid syntax: \n  {line}\nNo data declared.")
						elif len(cmd) == 2:
							raise Keeneyed4SyntaxError(f"[ERROR CODE 44] Invalid syntax: \n  {line}\nVariable '{cmd[1]}' has no value assigned.")
						elif len(cmd) == 3:
							raise UnreachableStateError(death_message)
						else:
							raise UnreachableStateError(death_message)
					else:
						try:
							if it:
								if first == 0:
									first += 1
									print(f"\n |-> Loading from category {currentDataSubject} data {cmd[1]} ...")
								else:
									print(f" |-> Loading from category {currentDataSubject} data {cmd[1]} ...")
							else:
								pass
							data[currentDataSubject][cmd[1]] = stringify(cmd[2:-1])
							print("complete.")
						except Exception as e:
							raise Keeneyed4ParsingError(f"[ERROR CODE 45] Error occurred during parsing: {e}")
				if list(cmd[0])[0] == "[":
					if list(cmd[0])[-1] != "]":
						raise Keeneyed4SyntaxError(f"[ERROR CODE 46] Invalid syntax: \n  {line}\nSubject name left trailing.")
					else:
						try:
							currentDataSubject = list(cmd[0])[1:-2]
						except:
							raise Keeneyed4ParsingError(f"[ERROR CODE 47] Error occurred during parsing: {e}")

		if it:
			print(f"[parsing @{ldir}] Data parse complete.")
		else:
			print("complete.")

	loadData(sdir + "simulation_data.ke4.dat")

	print(f"[parsing @{ldir}] Loading auxiliary data files ...\n")

	for datafile in os.listdir(sdir("datafiles/")):
		if datafile.endswith(".ke4.dat"):
			try:
				loadData(sdir + datafile)
			except Exception as e:
				raise Keeneyed4ParsingError(f"[ERROR CODE 48] Error during auxiliary datafile loading: {e}")
		else:
			print(f"[parsing @{ldir}] File {datafile} not marked as loadable, continuing ...")
			continue
		print("\n")

	def loadSector(sectorName):
		for datafile in os.listdir(sdir(f"{sectorName}/")):
			if datafile.endswith(".ke4.exec"):
				try:
					print(f"[parsing @{ldir}] Loading function file {datafile} ...", end="")
					exec(sdir + datafile)
					print("complete.")
				except Exception as e:
					raise Keeneyed4ParsingError(f"[ERROR CODE 49] Error during function file execution: {e}")
			elif datafile.endswith(".ke4.dat"):
				try:
					loadData(sdir + datafile)
				except Exception as e:
					raise Keeneyed4ParsingError(f"[ERROR CODE 50] Error during datafile loading: {e}")

	print(f"\n[parsing @{ldir}] Loading physics engine ...")
	loadSector("physics")
	print(f"complete.\n[parsing @{ldir}] Loading assets ...")
	loadSector("assets")

	print("[parsing @{ldir}] Data load complete, loading master function file ...", end="")

	exec(sdir + "master.ke4.exec") # Necessary that a sim named 'SIMULATION' be created.

	print("complete, simulation loaded.")

	try:
		return SIMULATION
	except NameError:
		raise Keeneyed4SyntaxError("[ERROR CODE 51] Parent simulation named 'SIMULATION' not defined in any files, loading failed.")
	except Exception as e:
		raise Keeneyed4ParsingError(f"[ERROR CODE 52] Error occurred in simulation load completion: {e}")

if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        while True:
            exec(input(">>> "))
    if sys.argv[1] == "version":
        print("Simulation Engine version 4.1.1.0.")
