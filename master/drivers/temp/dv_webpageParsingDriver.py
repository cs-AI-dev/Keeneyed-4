# Copyright 2021-2022 Jacob Bodell

# Licensed with a unique EULA license.
# This system may only be used in accordance
# with its EULA agreement.

# Please read and agree to the EULA in its entirety
# before using this system.

import os

os.system("py -m pip install bs4 -q")
os.system("py -m pip install requests -q")
os.system("py -m pip install re -q")

import re
import requests
import bs4
from bs4 import BeautifulSoup as bs4_content

google = "sentinel_google"
bing = "sentinel_bing"
yahoo = "sentinel_yahoo"

websearch_number = 0

def runWebSearch(searchEngineName, searchTerms):
	print(f"[websearch_{str(websearchNumber)}] starting search.")
	resultsPage = None
	match searchEngineName:
		case google:
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
			print(" | getting 1st-page URLs ...", end="")
			urls = dnsSoup
		case _:
			raise NameError(f"search engine {searchEngineName} is not available (currently only Google is supported).")
