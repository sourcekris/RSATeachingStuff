# RSA Excercises - Python

## Python Setup for Ubuntu Linux

Note: If you don't have Linux installed, you can download VirualBox and install it inside a
      VM. See [instructions here](virtualbox.md). If you're using Windows you may prefer
      to use Windows Subsystem for Linux (WSL) instead. You can read
      [instructions on using that here](wsl.md).

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

This will install Python 3 along with its dependencies.  Verify that Python is installed
correctly by checking the version:

```
python3 --version
```

### Step 3: Install pip

Pip is a package manager for Python. If It is used to install and manage Python packages. 
To install pip, run the following command:

```
sudo apt install python3-pip
```

Verify that Pip is installed correctly:

```
pip3 --version
```

### Step 4: Install PyCryptodome

Finally, to install PyCryptodome, run the following command:

```
pip3 install pycryptodome
```

### Step 5: Install VSCode

While its possible to use any text editor to write Python code, using VSCode is recommended
as it adds many features that are useful such as linting and syntax highligting.

To install it follow these steps:

1. Open a web browser and visit the official VSCode website: https://code.visualstudio.com/
2. Download the `.deb` package for Ubuntu.
3. Once the download is complete, open a terminal and navigate to the directory where the `.deb` 
   package is located. If you're using the default browser, this is probably `$HOME/Downloads`

4. Install VSCode using the dpkg command:

   ```
   sudo dpkg -i <filename>.deb
   ```

   If any dependencies are missing, you can install them by running:


   ```
   sudo apt --fix-broken install
   ```

VSCode should now be installed on your Ubuntu machine.

### Step 6: Set Up Python Environment in VSCode

1. Open VSCode by searching for it in the applications menu or using the terminal command:

   ```
   code
   ```

2. Install the Python extension for VSCode by Microsoft. Go to the Extensions view (Ctrl+Shift+X),
   search for "Python," and click the "Install" button.
3. Create a new Python file in VSCode by clicking on the Explorer icon (Ctrl+Shift+E) and then
   clicking the "New File" button.
4. Start writing your Python code in the new file. You can also save the file with a .py extension.
5. To run your Python code, open the integrated terminal in VSCode by selecting View → Terminal
   (Ctrl+`).
6. In the terminal, navigate to the directory where your Python file is located using the `cd` 
   command.
7. Run your Python program using the python3 command followed by the name of your Python file:

   ```
   python3 filename.py
   ```

8. This will install the PyCryptodome package along with its dependencies.

With these steps, you have successfully installed Python, Pip, and VSCode on your Ubuntu machine.
You can now start coding Python programs using VSCode, taking advantage of its powerful features
and the Python extension for a seamless development experience.