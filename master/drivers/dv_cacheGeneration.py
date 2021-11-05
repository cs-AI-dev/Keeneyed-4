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
	
	def generateCacheFile(this, cacheId="ID_UNKNOWN", directory):
		f = open(directory, "w")
		f.write(this.generateCacheContents(cacheId=cacheId))
		f.close()
