# Golang Exercises

## Golang Setup for Ubuntu Linux

**Note:** *If you don't have Linux installed, you can download VirtualBox and install it inside a VM. See [instructions here](virtualbox.md). If you're using Windows, you may prefer to use Windows Subsystem for Linux (WSL) instead. You can read [instructions on using that here](wsl.md).*

Before we start coding, let's set up a basic Golang coding environment on Linux. These steps cover Ubuntu Linux but might work on any Debian-based Linux. It includes the installation of Golang.

If Golang is already installed on your system, feel free to skip to step 3 or 4 depending on if `GOPATH` and `GOBIN` are also already configured.

### Step 1: Download Golang

First, open a terminal and run the following command to download Golang:

```bash
sudo apt-get update
sudo apt-get install golang
```

### Step 2: Configure Go Environment

Next, configure the Go environment variables. Open your shell profile file (e.g., .bashrc or .zshrc) using a text editor:

```bash
nano ~/.bashrc
```

Add the following lines at the end of the file:

```bash
export GOPATH=$HOME/go
export GOBIN=$GOPATH/bin
export PATH=$PATH:/usr/local/go/bin:$GOBIN
```

Save the file and exit the text editor. Then, run:

```bash
source ~/.bashrc
```

### Step 3: Verify Golang Installation

Verify that Golang is installed correctly by checking the version:

```bash
go version
```

### Step 4: Install VSCode

While it's possible to use any text editor to write Golang code, using VSCode is recommended as it adds many features that are useful, such as linting and syntax highlighting.

To install it, follow these steps:

1. Open a web browser and visit the official VSCode website: [https://code.visualstudio.com/](https://code.visualstudio.com/).
2. Download the `.deb` package for Ubuntu.
3. Once the download is complete, open a terminal and navigate to the directory where the `.deb` package is located. If you're using the default browser, this is probably `$HOME/Downloads`.
4. Install VSCode using the dpkg command:

   ```bash
   sudo dpkg -i <filename>.deb
   ```

   If any dependencies are missing, you can install them by running:

   ```bash
   sudo apt --fix-broken install
   ```

VSCode should now be installed on your Ubuntu machine.

### Step 5: Set Up Golang Environment in VSCode

1. Open VSCode by searching for it in the applications menu or using the terminal command:

   ```bash
   code
   ```

2. Install the Go extension for VSCode. Go to the Extensions view (Ctrl+Shift+X), search for "Go," and click the "Install" button.

3. Create a new Golang file in VSCode by clicking on the Explorer icon (Ctrl+Shift+E) and then clicking the "New File" button.

4. Start writing your Golang code in the new file. You can also save the file with a .go extension.

5. To run your Golang code, open the integrated terminal in VSCode by selecting View → Terminal (Ctrl+`).

6. In the terminal, navigate to the directory where your Golang file is located using the `cd` command.

7. Run your Golang program using the `go run` command followed by the name of your Golang file:

   ```bash
   go run filename.go
   ```

With these steps, you have successfully installed Golang and VSCode on your Ubuntu machine. You can now start coding Golang programs using VSCode, taking advantage of its powerful features and the Go extension for a seamless development experience.

## Next

* [Exercise 2](exercise2.md)
* [Back to Index](index.md)
