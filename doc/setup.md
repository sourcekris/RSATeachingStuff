# RSA Excercises - Python

## Python Setup for Ubuntu Linux

Before we start coding, let's set up a basic Python coding environment on Linux. These
steps cover Ubuntu Linux but might work on any Debian based Linux. It includes the installation of Python 
and PyCryptodome, an open source library that provides many useful methods for cryptography
with Python.

If Python (specifically Python3) is already installed on your system, feel free to skip to
step 3 or 4 depending on if `pip` is also already installed.

### Step 1: Update the package list

First, open a terminal and run the following command to update the package list:

```
sudo apt update
```

### Step 2: Install Python

Next, run the following command to install Python 3 (if it is not already installed):

```
sudo apt install python3
```

This will install Python 3 along with its dependencies.

### Step 3: Install pip

Pip is a package manager for Python. If It is used to install and manage Python packages. 
To install pip, run the following command:

```
sudo apt install python3-pip
```

### Step 4: Install PyCryptodome

Finally, to install PyCryptodome, run the following command:

```
pip3 install pycryptodome
```

This will install the PyCryptodome package along with its dependencies.

And that's it! You now have a basic Python coding environment set up on Ubuntu Linux, with 
PyCryptodome installed and ready to use.