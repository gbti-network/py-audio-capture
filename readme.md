# Py Audio Sourcer

Py Audio Sourcer is a Python utility script designed for easy audio recording from selected input devices. It prioritizes the Windows Sound Mixer, but if unavailable, focuses on utilizing the VB-Audio Virtual Cable.

## Table of Contents

- [About Python](#about-python)
    - [Installing Python on Windows](#installing-python-on-windows)
- [About Windows Sound Mixer](#about-windows-sound-mixer)
    - [Enabling Sound Mixer on Windows](#enabling-sound-mixer-on-windows)
- [About VB-Cable](#about-vb-cable)
    - [Installing VB-Cable on Windows](#installing-vb-cable-on-windows)
- [Setting Up Audio Output on Windows](#setting-up-audio-output-on-windows)
- [Using Py Audio Sourcer](#using-py-audio-sourcer)

## About Python

Python is a widely-used programming language known for its clear syntax and readability, which makes it especially good for beginners. Python is versatile and can be used for web development, data analysis, artificial intelligence, scientific computing, and more.

### Installing Python on Windows

1. Go to the official Python website's download section: [Python Downloads](https://www.python.org/downloads/).
2. Download the latest version for Windows.
3. Run the installer.
    - Ensure the "Add Python to PATH" option is checked.
    - Choose "Customize installation".
    - Ensure all optional features are selected.
    - Ensure "Install for all users" is selected for system-wide installation.
    - Proceed and finish the installation.

## Installing Python Dependencies

After installing Python, you will also need to install some additional Python packages which are dependencies for the Py Audio Sourcer script. These packages can be installed using `pip`, the Python package installer.

1. Open a command prompt or terminal window.
2. Navigate to the directory containing `sourcer.py`.
3. Run the following command:

```pip install sounddevice numpy wavio```

This will install the required Python packages, namely `sounddevice`, `numpy`, and `wavio`, which are required to run this script. 


## About Windows Sound Mixer

Windows Sound Mixer is an integrated feature that allows users to manage audio inputs and outputs. By default, this feature is usually disabled.

### Enabling Sound Mixer on Windows

1. Right-click on the speaker icon in the system tray.
2. Select "Sounds".
3. Navigate to the "Recording" tab.
4. If "Stereo Mix" or "Sound Mixer" is listed but disabled, right-click it and choose "Enable".
5. If it's not listed, right-click in an empty space and check both "Show Disabled Devices" and "Show Disconnected Devices". Then, look for "Stereo Mix" or "Sound Mixer", right-click, and select "Enable".
6. Click "OK" to save your changes.

## About VB-Cable

VB-Cable is a set of virtual audio devices working as virtual audio cables. Any application can send audio to the output, and any other application can pick this sound from the input. If the Windows Sound Mixer is unavailable, using VB-Cable is a reliable alternative.

### Installing VB-Cable on Windows

1. Visit the official VB-Cable download page: [VB-Cable Virtual Audio Device](https://vb-audio.com/Cable/).
2. Download the VB-Cable installer.
3. Extract the ZIP file.
4. Right-click on the `VBCABLE_Setup_x64.exe` (for 64-bit Windows) or `VBCABLE_Setup.exe` (for 32-bit Windows) and select "Run as administrator".
5. Proceed with the installation.
6. Restart your computer after the installation is complete.

## Setting Up Audio Output on Windows

Before running the script, ensure your audio output is set correctly.

1. If using the Windows Sound Mixer:
    - Set your desired application's audio output as default.

2. If using VB-Cable:
    - Right-click the speaker icon in the system tray (bottom right of your screen).
    - Select "Open Sound settings".
    - In the "Output" section, select "CABLE Input (VB-Audio Virtual Cable)" from the dropdown menu.

When using VB-Cable as your output/input device, sound won't play through your speakers. You'll need to switch the Windows sound output back to your usual device to hear it. Thus, during recording, audio won't be audible; start and stop recording based on judgment.

## Using Py Audio Sourcer

1. Navigate to the directory containing `sourcer.py`.
2. In the command line or terminal, run:

```py sourcer.py```

3. Follow the on-screen instructions to record audio.