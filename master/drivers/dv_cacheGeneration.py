# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import sys
import os

class Cache:
	def __init__(this, label=None, content=None, target=None, stamps=None):
		this.name = label
		this.content = content.encode("utf-8").hex()
		this.label = target
		this.tags = {}
		for tag in stamps:
			this.tags[tag.split(":")[0]] = tag.split(":")[1]

	def decryptContents(this):
		return this.content.decode("hex")

	def generateCacheContents(this, cacheId="ID_UNKNOWN"):
		return f"//KE4 CC LB>{this.name} ID>{cacheId}//\n//ENCODETYPE ASCII-HEX v1.0.0//\n//BEGINCACHE//\n{this.content}\n//ENDCACHE//\n"

	def generateCacheFile(this, directory, cacheId="ID_UNKNOWN"):
		f = open(directory, "w")
		f.write(this.generateCacheContents(cacheId=cacheId))
		f.close()
