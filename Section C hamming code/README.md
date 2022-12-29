# Hamming Code Take Home Test
This is my attempt at solving a Hamming code problem.
 Hamming code is used in error detection and detection.

# Table of contents
[Introduction](#general-info)
[What the project does](#what-this-project-does) 
- [Hamming Code Take Home Test](#hamming-code-take-home-test)
- [Table of contents](#table-of-contents)
  - [WHAT MY CODE CAN DO](#what-my-code-can-do)
  - [HOW DOES IT WORK?](#how-does-it-work)
  - [DETAILED SUMMARY](#detailed-summary)
    - [How is testing conducted](#how-is-testing-conducted)
    - [How is a hamming block entered](#how-is-a-hamming-block-entered)
    - [How is the hamming-block manipulated?](#how-is-the-hamming-block-manipulated)
    - [How are regions analysed](#how-are-regions-analysed)
    - [What is the expected output](#what-is-the-expected-output)
    - [What is the space complexity](#what-is-the-space-complexity)
- [TECHNOLOGIES](#technologies)
- [SETUP](#setup)

[Technologies](#technologies)
[Setup](#setup)

## WHAT MY CODE CAN DO
* Analyses error in a transmitted message and churns out the original message!
* *In addition to that,a user can*
	* **enter arbitrary data and obtain the original message**
	* **carry out testing using predetermined data**

## HOW DOES IT WORK?
The program works by either:
1. ONLY prompting the user for input.
2. Prompting the user for input and carrying out a set of tests for confirmation.

## DETAILED SUMMARY
### How is testing conducted

    Using an in-built python framework called unittest that has been mainly used for test automation.
    The following actions take place with-in testing:

1. Iterating through 15 sets of input values and expected values.
2. Comparison of the input to the expected values.
3. Finding the corrupted bits or if no bit is corrupt, a corresponding confirmation is given.
4. Evaluation and determination of the accuracy of the inout to the expectations.

### How is a hamming block entered

    Through user intervention.
    The block must be a 16bit binary string.
    The validity of the latter is confirmed by using a set that contains '0' and '1' to compare to the user input.
    If it matches the function that checks the hamming code is prompted to run.
    During testing, the blocks have been predetermined as transmitted values, the original value and the position of the erroneous bit.
    If there is no error, the erronious bit is recognised as an absence of error.

### How is the hamming-block manipulated?
    
    The block is split into 16 individual strings all stored into a list.
    The list is manipulated through comprehension to obtain a list of integers.
    The list is reshaped to a 4x4 array using Python Numpy.
    The 4x4 array is sliced into 4 regions corresponding to the parity bits in the positions
    corresponding to powers of 2 (1,2,4,8... e.t.c..)

### How are regions analysed
    
    Once slicing is done, the slices are stored into new arrays called regions.
    The sum of elements inside these new arrays is obtained.
    The moduli of these sums are calculated and this will determine whether the region has even or odd parity.
    If even parity exists,a 0 bit is stored. If odd parity exists,a 1 bit is stored.
    The order of storage is from region 8 to region 1.
    This value can be read as a decimal digit by converting the bits to a single string then converting it back into a decimal integer.
    This digit shows the postion of the bit that was flipped which we can re-flip to obtain the original message 


### What is the expected output
    The expected output is a corrected message of 16bits.

### What is the space complexity
    Since the input being given is a 16bit string that is mostly being used as a 4x4 array. It is evident that the worst case scenario is a growth that is directly proportional to the size of the input.
    Therefore it has a space complexity of O(n)

# TECHNOLOGIES
1. Python
2. Python unittest
3. VSCode
4. Numpy

# SETUP
Open up a workspace in VSCode and import all the source files for the program.
The source files are 
 1. hamming_code_2.py. This contains the main function.
 2. test_hamming_checker.py. This contains the test cases used in this code.

For Windows users:
Install Python from python.org. You can typically use the Download Python button that appears first on the page to download the latest version.
Note: If you don't have admin access, an additional option for installing Python on Windows is to use the Microsoft Store. The Microsoft Store provides installs of Python 3.7, Python 3.8, Python 3.9, and Python 3.10.

For MacOs users:
The system install of Python on macOS is not supported. Instead, a package management system like Homebrew is recommended. To install Python using Homebrew on macOS use brew install python3 at the Terminal prompt.
Note On macOS, make sure the location of your VS Code installation is included in your PATH environment variable.

For Linux users:
The built-in Python 3 installation on Linux works well, but to install other Python packages you must install pip with get-pip.py.

If Numpy is not installed, use of commandline pip commands can be used as directed below:
1. The easiest way to install NumPy is by using Pip. Pip a package manager for installing and managing Python software packages.
2. The commands below use the apt utility as we are installing on Linux

    a. Install Pip (for Python 2) by running:
        sudo apt install python-pip

    b. If you need Pip for Python 3, use the command:
        sudo apt install python3-pip

    c. Install NumPy with Python 2 by typing:
        pip install numpy

    d. To install NumPy with the package manager for Python 3, run:
        pip3 install numpy

3. Install NumPy on Mac Operating System

    a. Open Terminal.

    b.Check if you have python installed on your system or not. You can check this by typing “Python” on the terminal. It will give you the version of python installed on your system. MAC operating system usually has already installed a python package in it.

    c. Installing the Numpy library, using the following command:
        pip install numpy

4. Install Numpy on Windows Operating System

    a. Open command prompt.

    b. Check if you have python installed on your system or not. You can check this by typing “Python ” on the terminal. It will give you the version of python installed on your system.

    c.Installing the Numpy library, using the following command:
        pip install numpy

The program can be run from either source file by running the code directly within the Interactive Environment.
