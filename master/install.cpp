// Copyright 2021-2022 Jacob Bodell

// Licensed with a unique EULA license.
// This system may only be used in accordance
// with its EULA agreement.

// Please read and agree to the EULA in its entirety
// before using this system.

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

// Running this program, once compiled with an official
// C++ compiler, will allow you to install a working
// Keeneyed-4 artificial intelligence and simulation
// engine environment.

int main() {
	cout << "     KEENEYED-4 ARTIFICIAL INTELLIGENCE AND SIMULATION ENGINE ENVIRONMENT SETUP     \n";
	cout << "____________________________________________________________________________________\n";
	cout << "                                                                                    \n";
	cout << " (Step 1 of 4) Agreeing to the Software's EULA.                                     \n";
	cout << "                                                                                    \n";
	cout << " This program is designed to allow You to begin proper installation of the System's \n";
	cout << " software components. By using this program, even if You do not complete the proper \n";
	cout << " installation of the System's software components, You a) agree to and b) are hence \n";
	cout << " legally bound by the terms of the EULA which governs System's software components' \n";
	cout << " use until the EULA's termination.                                                  \n";
	cout << "                                                                                    \n";
	cout << " If You agree with all terms and conditions described within the EULA, then You may \n";
	cout << " proceed with the installation of the Keeneyed-4 engine environment.                \n";
	cout << "                                                                                    \n";
	cout << " If You do not agree with any of the terms or conditions described within the EULA, \n";
	cout << " then You must immediately discontinue your use of this program and cannot continue \n";
	cout << " with the proper installation of the System's software components.                  \n";
	cout << "____________________________________________________________________________________\n";
	cout << "                                                                                    \n";
	cout << " Do you agree to the terms described within the System's software component's EULA? \n";
	cout << " (y/n) ";
	
	string response;
	cin >> response;
	cout << "\n";
	
	while (true) {
		if (response == "y") {
			cout << " Excellent. Beginning installation of Keeneyed-4 engine environment ...\n";
			break;
		} else {
			cout << " Confirmed. Please terminate your use of this software immediately.\n";
		}
	}
	
	cout << "____________________________________________________________________________________\n";
	cout << "                                                                                    \n";
	cout << " (Step 2 of 4) Installation Directory.                                              \n";
	cout << "                                                                                    \n";
	cout << " Please select a directory where You would like to have your copy installed to here \n";
	cout << " on this device.                                                                    \n";
	cout << "                                                                                    \n";
	
	while (true) {
		cout << " C:/";
		cin >> response;
		string targetDirectory = response;
		cout << "\nPlease confirm the directory: " + response + "\n";
		cout << " (y/n) ";
		cin >> response;
		if (response == "y") {
			cout << " Target directory confirmed.\n";
		} else {
			cout << " Retry directory entry: ";
		}
	}
	
	cout << " Constructing environmnet ...";
	ofstream File_README(targetDirectory + "/keeneyed4_env/README.md");
	File_README
}
