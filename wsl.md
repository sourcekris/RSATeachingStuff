# Installing Ubuntu under WSL for Windows Users

## Step 1: Enable WSL

1. Open the Start menu and search for "Turn Windows features on or off" and click on the 
   corresponding result.
2. In the Windows Features dialog, scroll down and locate "Windows Subsystem for Linux".
3. Check the box next to "Windows Subsystem for Linux" and click "OK".
4. Windows will install the necessary components and may require you to restart your computer.

## Step 2: Install Ubuntu from Microsoft Store

1. Open the Microsoft Store on your Windows machine.
2. Search for "Ubuntu" and select "Ubuntu" from the search results.
3. Click on the "Install" button to download and install Ubuntu.
4. Once the installation is complete, click on the "Launch" button to start Ubuntu.
5. Ubuntu will initialize and prompt you to create a new user account with a username and password.

## Step 3: Update Ubuntu

1. After creating your user account, open the Ubuntu terminal.
2. Run the following command to update the package lists and upgrade installed packages:
   ```
   sudo apt update && sudo apt upgrade
   ```
3. Enter your password when prompted.
4. Wait for the update and upgrade process to complete.

## Step 4: Using Ubuntu on WSL

1. With Ubuntu installed and updated, you can now use it as a Linux environment on your Windows
   machine.
2. You can execute Linux commands, install packages, and run Linux applications within the Ubuntu
   terminal.
3. You can access your Windows files from within Ubuntu at the path `/mnt/c/` followed by the path
   to your files. For example, to access files on your C: drive, use `/mnt/c/`.
4. You can also access the Ubuntu file system from Windows File Explorer by navigating to `\\wsl$`
   and selecting the appropriate Ubuntu distribution.

Congratulations! You have successfully installed Ubuntu under WSL on your Windows machine. You can
now start using Ubuntu and enjoy a Linux environment alongside your Windows operating system.

