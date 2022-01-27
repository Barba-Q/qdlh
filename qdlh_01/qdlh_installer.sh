#!/bin/bash
apwd="$(pwd | sed 's/ /\ /g')"
confpath=~/.config/qtile/config.py

echo "checking for qtile"
if which qtile >/dev/null; then
	echo "Qtile is already installed, saving your config.py"
	cp -a ~/.config/qtile/config.py "$confpath-$(date +"%d-%m-%y-%r")"
	echo "config saved as config.py-[current time and date]"
	sleep 3
else   
    echo "Qtile not found. Please install qtile on your system and try again."
    exit
fi

echo "checking for python 3.9"
if which python3.9 >/dev/null; then
	echo "python 3.9 found - commencing setup"
	sleep 3
else
	echo "python3.9 not found, please install and try again"
	exit
fi

echo "installing qdlh - please provide root password"
xterm -e	"cp '$apwd'/files/home/user/config/qtile/config.py ~/.config/qtile/config.py;
            cp '$apwd'/files/home/user/config/qtile/autostart.sh ~/.config/qtile/autostart.sh;
            cp '$apwd'/files/home/user/config/qtile/qdlh.py ~/.config/qtile/qdlh.py;
            cp '$apwd'/files/home/user/config/qtile/qdlh_conf.py ~/.config/qtile/qdlh_conf.py;
            cp '$apwd'/files/home/user/config/qtile/wallpaper.png ~/.config/qtile/wallpaper.png;
            sudo cp '$apwd'/files/usr/bin/qdlh /usr/bin/qdlh;
            sleep 3
            read -s -n1 -p 'All done. Start qtile dirty little helper by spawning 'qdlh' - Press any key to close...'"

