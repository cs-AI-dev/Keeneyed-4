# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import nltk
from nltk.corpus import wordnet as wn

class SemanticLanguageDataError(Exception): pass

class SemanticLanguageData:
	def __init__(sld, emphasisInfo, toneInfo, wnSynsetKey=None, **contextInfo):
		try:
			sld.rawKey = wnSynsetKey.encode("utf-8").hex()
			sld.synsetKey = wn.synsets(bytes.fromhex(sld.rawKey[2:]).decode("ASCII"))
			sld.lemmasKey = wn.lemmas(bytes.fromhex(sld.rawKey[2:]).decode("ASCII").split(".")[0])
		except Exception as e:
			raise SemanticLanguageDataError(f"[ERROR CODE 54] Error constructing semantic language data packet: {e}")
		
		try:
			sld.emphasisLevel = emphasisInfo[0]
			sld.emphasisExtrinsicity = emphasisInfo[1]
		except IndexError:
			raise SemanticLanguageDataError("[ERROR CODE 55] Invalid emphasis data packet construction.")
		except:
			raise SemanticLanguageDataError(f"[ERROR CODE 56] Error constructing semantic language data packet: {e}")
		
		try:
			sld.toneType = toneInfo[0].encode("utf-8").hex()
			sld.toneExtrinsicity = toneInfo[1]
		except IndexError:
			raise SemanticLanguageDataError("[ERROR CODE 57] Invalid tone data packet construction.")
		except:
			raise SemanticLanguageDataError(f"[ERROR CODE 58] Error constructing semantic language data packet: {e}")
			
		sld.context = contextInfo
			
	def packet(sld):
		return {
			"synsetKey": sld.synsetKey,
			"lemmasKey": sld.lemmasKey,
			"emphasisLevel": sld.emphasisLevel,
			"emphasisExtrinsicity": sld.emphasisExtrinsicity,
			"toneType": bytes.fromhex(sld.toneType[2:]).decode("ASCII"),
			"toneExtrinsicity": sld.toneExtrinsicity,
			"context": sld.context
		}
	
	def wn_info(sld):
		return {
			"synsetKey": sld.synsetKey,
			"lemmasKey": sld.lemmasKey
		}
	
	def ke4_info(sld):
		return {
			"emphasisLevel": sld.emphasisLevel,
			"emphasisExtrinsicity": sld.emphasisExtrinsicity,
			"toneType": bytes.fromhex(sld.toneType[2:]).decode("ASCII"),
			"toneExtrinsicity": sld.toneExtrinsicity
		}
	
	def context(sld):
		return sld.context
	
	def unwrap(sld):
		return {
			"packet": sld.packet(),
			"wn_info": sld.wn_info(),
			"context": sld.context(),
			"ke4_info": sld.ke4_info(),
		}
		
def UnwrapSLD(sld):
	return {
		"packet": sld.packet(),
		"wn_info": sld.wn_info(),
		"context": sld.context(),
		"ke4_info": sld.ke4_info(),
	}
