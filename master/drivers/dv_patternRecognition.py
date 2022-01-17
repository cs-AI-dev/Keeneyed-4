# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import random
import os
import math
os.system("py -m pip install tqdm -q")
import tqdm

def stringify(l):
    o = ""
    for x in l:
        o = o + x
    return o

class Cadence:
    def __init__(cadence, *items):
        if len(items) > 1:
            for x in items:
                if type(x) != type(1) and type(x) != type(1.5):
                    raise SyntaxError("Cadence item types must be int or float.")
            cadence.items = items
        else:
            if type(items[0]) != type([1, 2]):
                raise SyntaxError("Cadence 'items' must be ints/floats or list.")
            else:
                cadence.items = items[0]
        cadence.progressiveScalarDifference = [items[i] - items[i - 1] for i in [x + 1 for x in range(len(items))] if i < len(items)]
        cadence.initialScalarDifference = [items[i - 1] - items[0] for i in [x + 1 for x in range(len(items))] if i < len(items)]
        cadence.progressiveGeometricDifference = [items[i] / items[i - 1] for i in [x + 1 for x in range(len(items))] if i < len(items)]
        cadence.initialGeometricDifference = [items[i - 1] / items[0] for i in [x + 1 for x in range(len(items))] if i < len(items)]

    # High -> very different, low -> very similar, 0 -> the same
    def patternDifference(cadence, alternateCadence):
        if type(alternateCadence) != type(cadence):
            raise TypeError("You can only compare the similarity of two Cadences.")

        if len(cadence.initialGeometricDifference) != len(alternateCadence.initialGeometricDifference):
            raise SyntaxError("You can't compare Cadences of different lengths.")

        dset = []

        for i in range(len(cadence.initialGeometricDifference)):
            if cadence.initialGeometricDifference[i] > alternateCadence.initialGeometricDifference[i]:
                dset.append( cadence.initialGeometricDifference[i] - alternateCadence.initialGeometricDifference[i] )
            elif cadence.initialGeometricDifference[i] < alternateCadence.initialGeometricDifference[i]:
                dset.append( alternateCadence.initialGeometricDifference[i] - cadence.initialGeometricDifference[i] )

        return sum(dset) / len(dset)

    def scalarDifference(cadence, alternateCadence):
        if type(alternateCadence) != type(cadence):
            raise TypeError("You can only compare the similarity of two Cadences.")

        if len(cadence.initialGeometricDifference) != len(alternateCadence.initialGeometricDifference):
            raise SyntaxError("You can't compare Cadences of different lengths.")

        dset = []

        for i in range(len(cadence.initialGeometricDifference)):
            dset.append( -1 * (cadence.initialGeometricDifference[i] - alternateCadence.initialGeometricDifference[i]) )

        return sum(dset) / len(dset)

    def literalSimilarity(cadence, alternateCadence):
        identicalities = 0
        for x in range(len(alternateCadence.items)):
            if alternateCadence.items[x] == cadence.items[x]:
                identicalities += 1
        return identicalities / len(alternateCadence.items)

    def generateScalarSimilarities(cadence, difference, newCadencesCount=1000):
        # Generates up to several hundred thousand per second
        newCadences = []
        for x in tqdm.tqdm(range(newCadencesCount), desc="[scalar_similarities_generator] generating new cadences", ascii="_#"):
            newCadences.append(Cadence([item + random.randint((difference * -1), difference) for item in cadence.items]))
        return newCadences

    def generateGeometricSimilarities(cadence, difference, newCadencesCount=1000):
        # Generates up to several hundred thousand per second
        newCadences = []
        for x in tqdm.tqdm(range(newCadencesCount), desc="[scalar_similarities_generator] generating new cadences", ascii="_#"):
            newCadences.append(Cadence([item * random.randint((difference * -1), difference) for item in cadence.items]))
        return newCadences

class Pattern:
    def __init__(pattern, name, dataset):
        pattern.name = name

        for datum in dataset:
            if type(datum) != type(Cadence(1, 2, 3)):
                raise SyntaxError("All data must be Cadences.")
            if len(datum.items) != len(dataset[0].items):
                raise SyntaxError("Cadences in a dataset can't have different item counts.")

        pattern.dataset = dataset
        pattern.averages = []
        for i in range(len(pattern.dataset[0].items)):
            pattern.averages.append(
                sum([x.items[i] for x in pattern.dataset]) / len(pattern.dataset)
            )
        pattern.averageCadence = Cadence(pattern.averages)

    def train(pattern, datasetAddition=None):
        da = datasetAddition
        if datasetAddition == None:
            da = []
        pattern.dataset = pattern.dataset + da
        pattern.averages = []
        for i in range(len(pattern.dataset[0].items)):
            pattern.averages.append(
                sum([x.items[i] for x in pattern.dataset]) / len(pattern.dataset)
            )
        pattern.averageCadence = Cadence(pattern.averages)

    def reloadPattern(pattern):
        pattern.train()

    def clearHistory(pattern, indexMaximum=None):
        if indexMaximum == None:
            pattern.dataset = []
        else:
            pattern.dataset = pattern.dataset[indexMaximum:]

unnamedAis = 0

class ArtificialPatternRecognitionIntelligence:
    def __init__(ai, name=None):
        if name != None:
            ai.name = name
        else:
            ai.name = "unnamed_pattern_recognition_ai_" + str(unnamedAis)
            unnamedAis += 1

        ai.patterns = []

    def addPattern(ai, name, dataset):
        ai.patterns.append(Pattern(name, dataset))

    def trainPattern(ai, name, datasetAddition):
        if type(name) != type("hello world"):
            raise SyntaxError("Pattern name must be a string.")

        for pattern in ai.patterns:
            if pattern.name == name:
                pattern.train(datasetAddition)
                break
            raise NameError(f"No pattern with name '{name}' in this recognizer.")

    def identifyPatterns(ai, dataset, recognitionThreshold, literalSimilarityThreshold=0.9, trainingEnabled=False):
        # if training is enabled, the AI will auto-train
        # itself on matches to better fit the dataset
        patternMatch = []

        for cadence in tqdm(dataset, desc=f"[{ai.name}] identifying patterns", ascii="_#"):
            recognizedPatterns = []
            for pattern in ai.patterns:
                if cadence.geometricDifference(pattern.averageCadence) <= recognitionThreshold or cadence.literalSimilarity(pattern.averageCadence) >= literalSimilarityThreshold:
                    recognizedPatterns.append(pattern.name)
                    if trainingEnabled == True:
                        np = pattern
                        np.train(cadence)
                        ai.patterns = ai.patterns.remove(pattern).append(np)
            patternMatch.append([cadence, recognizedPatterns])

        return patternMatch
        print(f"[{ai.name}] pattern identification complete.\n")

    def identifyMathematicalFunction(ai, patternName): # Currently works on only arithmetic relations
        function = None
        for pattern in ai.patterns:
            if pattern.name == patternName:
                print(f"[{ai.name}] rounding off pattern ...")
                print(f"[{ai.name}] current averaged data: " + str(pattern.averageCadence.items))
                nci = [math.floor(x - 1) for x in pattern.averageCadence.items]
                print(f"[{ai.name}] round-off complete, analyzing ...")
                roundedCadence = Cadence(nci)

                function = "x "

                ft = True

                for x in roundedCadence.items:
                    print(f" | checking differences for {str(x)} between {roundedCadence.items[0]} ...")
                    if x > roundedCadence.items[0] - 1:
                        print(" | greater than detected, adding ...")
                        function = function + "+ " + str((x - roundedCadence.items[0])) + ", x "
                    if x < roundedCadence.items[0] - 1:
                        print(" | greater than detected, adding ...")
                        function = function + "- " + str((roundedCadence.items[0] - x)) + ", x "
                    if x == roundedCadence.items[0] - 1:
                        print(" | equal detected, adding ...")
                        function = function + ", x "

                function = function[:-2]
                function = function.replace(" + 0", "").replace(" - 0", "")

                print(f"[{ai.name}] done.")

                print(f"[{ai.name}] mathematical function generated.")
                print(f"\n{function}\n\n[{ai.name}] returning ... ")
                break
        return function
