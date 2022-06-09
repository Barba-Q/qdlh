# qdlh alpha
Qtile dirty litte helper - graphical settings-tool for qtile. -
Since 02 it comes along with an graphical applicationlauncher. It can be launched by pressing Meta + Q (default)

![qdlh 0.2](https://github.com/Barba-Q/qdlh/blob/main/qdlh_menu.png)

The Reboot and Shutdown button may not work at this point.

![qdlh 0.1](https://github.com/Barba-Q/qdlh/blob/main/qdlh01.png)


# Description
Qdlh comes along with an "installer" wich moves some files around to access a small python tool to set up qtile the graphical way.
It can be spawned as every other software with `MOD+R qdlh` once it's installed. 
The installer will backup any existing config file.

Qdlh can:
- set bar size
- set font size
- set margin (Gapsize between windows)
- set wallpaper and it's mode
- set barcolor
- set foreground color
- set background color
- set text color

- set up to five (for now) apps to autostart



## Requirements
- xterm
- python 3.9
- tkinter for python3.9 (e.g. python39-tk)
- qtile



## Install
- Download the folder with the latest version
- Install by typing: 
				```sh /path/to/your/download/qdlh_installer.sh```


## Usage
-	Spawn qdlh-menu by pressing `Meta / Super Key + Q`
-	The code behind the menu will lookup for _common_ installed Software and shows a clickable button 


-	Spawn qdlh by pressing `Meta / Super Key + R and type`:
				```qdlh```

-	Set up the stuff you want to change and press apply to save your settings.

-	Changes will take effect when qtile is restarted with `Meta / Super Key + Ctrl + R`, changes in the autostart section 
will take effect after completely restarting qtile (relogin / restart)

## Notes

- 	qdlh is made to be 'not so invasive' on the qtile config so you still be able to fiddle 
	around as you please
  
- this is alpha software for a reason, a lot of features I want to implement are missing, it's ugly and I need a lot more experience with python to 
make this some kind of appealing, but I'm working hard on that :-)
	

## Road to 1.0
Following features will be added:
- Give the installer some intelligence (check for distro, install missing stuff.. things like that)
- Detect invalid options (e.g. wrong filetype for wallpaper)
- Set bar position
- Set up multiple bars
- Select layouts to be used
- Multimonitor settings
- Some kind of widget selector
- Load backup config option
- Restart qtile automatically (almost done)
- Make it look good in a tiling environment


## The files

There are a lot of files for now, to clear up some confusion heres what every one of them is supposed to do and where it goes.

- autostart.sh
	- will be executed once whenever qtile boots up (not on qtile restarts)
	- this file goes to ~/.config/qtile/
	
- config.py
	- replaces the original qtile configuration
	- contains some variables related to qdlh wich are necessary to have an effect on qtile
	- this file goes to ~/.config/qtile/

- qdlh.py
	- this the core, the graphical interface with all its functions to change things in qtile
	- this file goes to ~/.config/qtile/
	
- qdlh_conf.py
	- this is the interface wich is written by qdlh.py the config will fetch those things
	- this file goes to ~/.config/qtile/
	
- qtile(sh)
	- this file goes to /usr/bin/ on your system so qdlh is spawnable from the desktop
	- this file executes qdlh.py

- wallpaper.png
	- this is just a default wallpaper, I think it's cool to see a wallpaper when you're new to qtile
  
  
## Is this necesarry

Of course it's not, this tool exists, if at all, to make it easier for beginners to get started with qtile and not at least to test my premature skills in python.
Bare with me and feel free to take it to the next level.

Oh btw I've tested this on opensuse only. It _should_ work everywhere else though.

