# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import os
import sys

os.system("py -m pip install bs4 -q")
os.system("py -m pip install requests -q")

import re
import requests
import bs4
from bs4 import BeautifulSoup as bs4_content

class TopLevelDomainError(Exception):
	pass
class InvalidQueryArguments(Exception):
	pass

google = "sentinel_google"
bing = "sentinel_bing"
yahoo = "sentinel_yahoo"

websearchNumber = 0

def getTripleDigit(i):
	if i < 10:
		return "00" + str(i)
	elif i < 100:
		return "0" + str(i)
	else:
		return "99+"

class WebsearchReturn:
	def __init__(wsr, searchEngineName, searchEngineTerms, links):
		wsr.engine = searchEngineName
		wsr.terms = searchEngineTerms
		wsr.urls = {
			"net": [url for url in links if url[0].split("/")[2].split(".")[-1] == "net"],
			"com": [url for url in links if url[0].split("/")[2].split(".")[-1] == "com"],
			"org": [url for url in links if url[0].split("/")[2].split(".")[-1] == "org"],
			"edu": [url for url in links if url[0].split("/")[2].split(".")[-1] == "edu"],
			"int": [url for url in links if url[0].split("/")[2].split(".")[-1] == "int"],
			"gov": [url for url in links if url[0].split("/")[2].split(".")[-1] == "gov"],
		}
		wsr.tlds = [tld for tld in wsr.urls.keys() if tld != []]
		wsr.allXMLContent = [requests.get(url).content for url in wsr.urls["net"] + wsr.urls["com"] + wsr.urls["org"] + wsr.urls["edu"] + wsr.urls["int"] + wsr.urls["gov"]]

	def getByTopLevelDomains(wsr, tld):
		if tld in wsr.tlds:
			return wsr.urls[tld]
		else:
			raise TopLevelDomainError(str(tld) + " is not a TLD recognized by the webpage parsing driver.")

	def getByTLD(wsr, tld):
		if tld in wsr.tlds:
			return wsr.urls[tld]
		else:
			raise TopLevelDomainError(str(tld) + " is not a TLD recognized by the webpage parsing driver.")

	def getByReputableTopLevelDomain(wsr):
		return wsr.urls["gov"].append(wsr.urls["int"].append(wsr.urls["edu"].append(wsr.urls["org"])))

	def getByReputable(wsr):
		return wsr.urls["gov"].append(wsr.urls["int"].append(wsr.urls["edu"].append(wsr.urls["org"])))

	def getNumberOfLinksByTld(wsr, tld):
		if tld in wsr.tlds:
			return len(wsr.urls[tld])
		else:
			raise TopLevelDomainError(str(tld) + " is not a TLD recognized by the webpage parsing driver.")

	def getDataFromPages(wsr, name=None, tld=None):
		if (name == None and tld == None):
			raise InvalidQueryArguments("No query arguments were defined; search by TLD or a website name.")
		if (name != None and tld != None):
			raise InvalidQueryArguments("Illegal specification of both website name and TLDs.")
		pageData = []
		if name != None:
			for tld in wsr.urls.keys():
				for url in wsr.urls[tld]:
					if name[0:2] == "www":
						if url.split("/")[2] == name:
							currentRequest = requests.get(url)
							pageData.append(currentRequest.content)
						else:
							pass
					else:
						pass

	def getAllContent(wsr):
		return wsr.allXMLContent


def runWebSearch(searchEngineName, searchTerms):
	print(f"[websearch_{str(websearchNumber)}] starting search.")
	resultsPage = None
	returnedLinks = []
	output = None
	if searchEngineName == "sentinel_google":
		print(" | formatting search terms ...", end="")
		st = searchTerms.replace(" ", "+")
		print("done.\n | current search terms: " + str(st))
		print(" | opening URL request ...", end="")
		url = "https://www.google.com/search?q=" + str(st)
		resultsPage = requests.get(url)
		print("done.\n | current URL: " + url)
		print(" | loading DNS soup ...", end="")
		dnsSoup = bs4_content(resultsPage.content)
		print("done.")
		print(" | getting 1st-page URLs ...")
		urls = dnsSoup.find_all("a")
		for link in dnsSoup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
			print(" | | URL retrieved: " + str(re.split(":(?=http)",link["href"].replace("/url?q=",""))) )
			returnedLinks.append( re.split(":(?=http)",link["href"].replace("/url?q=","")) )
		print(" | complete, stored in microdatabase.")
		output = WebsearchReturn(google, searchTerms, returnedLinks)
	else:
		raise NameError(f"search engine {searchEngineName} is not available (currently only Google is supported).")
	print(f"[websearch_{str(websearchNumber)}] search complete.")
	reg_net = getTripleDigit( output.getNumberOfLinksByTld("net") )
	reg_com = getTripleDigit( output.getNumberOfLinksByTld("com") )
	reg_org = getTripleDigit( output.getNumberOfLinksByTld("org") )
	reg_edu = getTripleDigit( output.getNumberOfLinksByTld("edu") )
	reg_int = getTripleDigit( output.getNumberOfLinksByTld("int") )
	reg_gov = getTripleDigit( output.getNumberOfLinksByTld("gov") )
	print(f"[websearch_{str(websearchNumber)}] returned URLs: {str(len(returnedLinks))}")
	print(f" | .net | {reg_net} |")
	print(f" | .com | {reg_com} |")
	print(f" | .org | {reg_org} |")
	print(f" | .edu | {reg_edu} |")
	print(f" | .int | {reg_int} |")
	print(f" | .gov | {reg_gov} |")
	print(f"[websearch_{str(websearchNumber)}] websearch complete, returning.")
	return output

if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        while True:
            exec(input(">>> "))
    if sys.argv[1] == "version":
        print("Webpage Parsing Driver version 4.1.1.0.")
