#!/bin/bash
apwd="$(pwd | sed 's/ /\ /g')"

echo "uninstalling qdlh - please provide root password"
xterm -e	"rm ~/.config/qtile/qdlh.py;
            rm ~/.config/qtile/qdlh_conf.py;
			sudo rm /usr/bin/qdlh;
			sleep 3;
            read -s -n1 -p 'qdlh is no more. - Press any key to close...'"
fi
