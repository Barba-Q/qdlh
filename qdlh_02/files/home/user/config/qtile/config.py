##This config was created by qdlh##
#edit as you please, qdlh related stuff is marked#


##Imports

from typing import List  # noqa: F401

from libqtile import bar, extension, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from os.path import expanduser
import os, subprocess


## Variables ##
from qdlh_conf import * #qdlh related
home = expanduser("~") #needed for autostart

mod = "mod4"
terminal 	= guess_terminal()

## Key bindings ##
keys = [
    # Window focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

   # Window order
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

	# Window sizes
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

	# Layout
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "q", lazy.spawn("qdlh_menu"), desc="blah"),

]

## Groups ##
#(This solution is ugly for now and should change in the future)
icon_gr1 = "1"
icon_gr2 = "2"
icon_gr3 = "3"
icon_gr4 = "4"
icon_gr5 = "5"


# Definitions
groups = [Group(icon_gr1),#variable is qdlh related
          Group(icon_gr2),#variable is qdlh related
          Group(icon_gr3),#variable is qdlh related
          Group(icon_gr4),#variable is qdlh related
          Group(icon_gr5)]#variable is qdlh related

# Keybindings to change groups       
keys.extend([
    Key([mod], "1", lazy.group[icon_gr1].toscreen()),
    Key([mod, "shift"], "1", lazy.window.togroup(icon_gr1, switch_group=True)),
    
    Key([mod], "2", lazy.group[icon_gr2].toscreen()),
    Key([mod, "shift"], "2", lazy.window.togroup(icon_gr2, switch_group=True)),  

    Key([mod], "3", lazy.group[icon_gr3].toscreen()),
    Key([mod, "shift"], "3", lazy.window.togroup(icon_gr3, switch_group=True)),  
	
    Key([mod], "4", lazy.group[icon_gr4].toscreen()),
    Key([mod, "shift"], "4", lazy.window.togroup(icon_gr4, switch_group=True)),  
	
    Key([mod], "5", lazy.group[icon_gr5].toscreen()),
    Key([mod, "shift"], "5", lazy.window.togroup(icon_gr5, switch_group=True))  
	])


layouts = [
    layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=2, margin = margin),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font		= "sans",
    fontsize	= textsize,#variable is qdlh related
    padding		= 3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        wallpaper = wallpaper_img,#variable is qdlh related
        wallpaper_mode = wallpaper_set,#variable is qdlh related
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(active = fgcolor, inactive = "#ffffff"),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("Vol:", foreground = fgcolor),
                widget.Volume(),
                
                widget.TextBox("Tray:", foreground = fgcolor),
                widget.Systray(),
                
                widget.TextBox("Time:", foreground = fgcolor),
                widget.Clock(format ='%H:%M %p'),
                
                widget.TextBox("CPU:", foreground = fgcolor),
                widget.CPU(format = '{load_percent}%'),
                                
                widget.TextBox("Exit:", foreground = fgcolor),
                widget.QuickExit(),
            ],
            panelsize,#variable is qdlh related
        background=[bgcolor]),#variable is qdlh related
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder 	= None
dgroups_app_rules 	= []  # type: List
follow_mouse_focus 	= True
bring_front_click 	= False
cursor_warp 		= False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='>qdlh_menu<'), # This is QDLH related and makes the menu floating
])
auto_fullscreen 			= True
focus_on_window_activation 	= "smart"
reconfigure_screens 		= True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"

#variable is qdlh related
## Autostart 
@hook.subscribe.startup_once
def autostart():
    subprocess.run(home+"/.config/qtile/autostart.sh")
