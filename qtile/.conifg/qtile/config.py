# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess


from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


from gruvbox.gruvbox import *
from theme import *


from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()

keys = [

# Most of our keybindings are in sxhkd file - except these

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),


# SUPER + SHIFT KEYS

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),


# QTILE LAYOUT KEYS
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "n", lazy.layout.normalize()),
    

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

#Applications 

    Key([mod], "space", lazy.spawn('rofi -show drun')),
    Key([mod], "e", lazy.spawn('alacritty -e nvim')),
    Key([mod], "b", lazy.spawn('brave')),
    Key([mod], "h", lazy.spawn('alacritty -e htop')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "Return", lazy.spawn('alacritty')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "x", lazy.spawn('rofi -show power-menu -modi power-menu:rofi-power-menu')),
    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    Key([alt, "shift"], "n", lazy.spawn('feh --bg-scale -z .local/share/backgrounds')),
    Key([alt], "b", lazy.spawn('rofi-bluetooth')),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brillo -A 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brillo -U 10"))




    ]

groups = [Group(name='1', layout='monadtall'),
          Group(name='2', layout='monadtall'),
          Group(name='3', layout='monadtall'),
          Group(name='4', layout='monadtall'),
          Group(name='5', layout='monadtall'),
          Group(name='6', layout='monadtall'),
          ]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            )
])

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod")

layout_theme = {"border_width": 2,
                "margin": 7,
                "border_focus": "#98971a",
                "border_normal": "#458588",
                "font": "JetBrainsMono Nerd Font",
                "grow_amount": 3,
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(**layout_theme, num_stacks=2),
    layout.Floating(**layout_theme)
]





everforest = {
        'bg': '#1e2326',
        'fg': '#d3c6aa',
        'blue': '#7fbbb3',
        'red': '#f85552',
        'black': '#24283b',
        'cyan': '#83c092',
        'green': '#a7c080',
        'yellow': '#dbbc7f',
        'orange': '#e69875',
        'grey': '#7a8478',
        'purple': '#d699b6'
        }

gruvbox_dark ={

        'bg':'#282828',
        'black0':'#7c6f64',
        'red':'#cc241d',
        'red0':'#fb4934',
        'green':'#98971a',
        'green0':'#b8bb26',
        'yellow':'#d79921',
        'yellow0':'#fabd2f',
        'blue':'#458588',
        'blue0':'#83a598',
        'purple':'#b16286',
        'purple0':'#d3869b',
        'aqua':'#689d6a',
        'aqua0':'#8ec07c',
        'white':'#a89984',
        'fg':'#fbf1c7'
}



colors = gruvbox_dark




widget_defaults = dict(
    font="JetBrainsMono",
    fontsize=18,
    background = colors['bg'],
    foreground=colors['black0'],
    padding = 10,
)
extension_defaults = widget_defaults.copy()






screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize = 15,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    highlight_method='text',
                    this_current_screen_border = colors['green'],
                    active = colors['blue0'],
                    ),
               
                widget.WindowName(
                    background = colors['bg'],
                    format = "{name}",
                    foreground = colors['fg'],
                    empty_group_string = 'Desktop',
                    fontsize = 10,
                    ),
                
                

                widget.Systray(
                    
                        ),

                widget.CheckUpdates(
                    # background = colors['fg'],
                    # foreground = colors['bg'],
                    distro='Arch_checkupdates',
                    display_format = ' : {updates}',
                    no_update_string=' : 0',
                    fontsize = 10,

                    ),
                widget.TextBox(
                    text='\uE0B0',
                    foreground=colors['bg'],
                    background=colors['fg'],
                    padding=0,
                    fontsize = 20,
                    ),
                
                widget.CurrentLayout(
                    background = colors['fg'],
                    foreground = colors['bg'],
                    fontsize = 11,
                ),
                # widget.TextBox(
                #     text='\uE0B0',
                #     background=colors['purple'],
                #     foreground=colors['blue'],
                #     padding=0,
                #     fontsize=25,
                #     ),
                widget.TextBox(
                    text='\uE0B0',
                    foreground=colors['fg'],
                    background=colors['bg'],
                    padding=0,
                    fontsize = 20,
                    ),
                widget.Battery(
                        foreground = colors['fg'],
                       background = colors['bg'],
                       charge_char = "Y",
                       discharge_char = "N",
                       full_char = "Full",
                       fontsize = 11,
                       format =": {percent:2.0%} - : {char}",
                       low_percentage = 0.3,
                       notify_below = 0.3,
                       update_interval = 7,
                       ),
              # widget.TextBox(
              #       text='\uE0B0',
              #       background=colors['green'],
              #       foreground=colors['purple'],
              #       padding=0,
              #       fontsize=25,
              #       ),
              widget.TextBox(
                    text='\uE0B0',
                    foreground=colors['bg'],
                    background=colors['fg'],
                    padding=0,
                    fontsize = 20,
                    ),
                widget.TextBox(
                    text='Vol:',
                    background = colors['fg'],
                    foreground = colors['bg'],
                    fontsize = 10,
                    ),
                widget.PulseVolume(
                    background = colors['fg'],
                    foreground = colors['bg'],
                    fontsize = 10,
                    ),
                widget.TextBox(
                    text='\uE0B0',
                    foreground=colors['fg'],
                    background=colors['bg'],
                    padding=0,
                    fontsize = 20,
                    ),

                widget.Clock(
                        format='Date: %d/%m/%y',
                        foreground = colors['fg'],
                        fontsize = 11,
                        font = "JetBrainsMono",
                        ),
                widget.TextBox(
                    text='\uE0B0',
                    foreground=colors['bg'],
                    background=colors['fg'],
                    padding=0,
                    fontsize = 20,
                    ),

                widget.Clock(
                        background = colors['fg'],
                        format='Time:  %I:%M %p',
                        foreground = colors['bg'],
                        fontsize = 11,
                        font = "JetBrainsMono",
                        ),
                 
                widget.TextBox(
                    text='\uE0B0',
                    foreground=colors['fg'],
                    background=colors['bg'],
                    padding=0,
                    fontsize = 20,
                    ),

            ],
            25,
        ),
    ),
]

Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
Click([mod], "Button2", lazy.window.bring_to_front()),


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True




@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
