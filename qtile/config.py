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

from typing import List  # noqa: F401

from libqtile import qtile, bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import os
import subprocess
from libqtile import hook

#----STARTUP----#
@hook.subscribe.startup_once
def start_once():
        home = os.path.expanduser('~')
        subprocess.call([home + '/.config/qtile/autostart.sh'])

# ...
mod = "mod1"
spawn_mod = "mod4"
terminal = "alacritty"

#-----COLORS-----#
def init_colors():
    return [['#282a36', '#282a36'], # Dracula gray
            ['#11BAB5', '#11BAB5'], # ADOBE cyan
            ['#C74CAE', '#C74CAE'], # ADOBE pink
            ['#ff5555', '#ff5555'], # Red
            ['#8a426b', '#8a426b'], # Inactive pink
            ['#414247', '#414247'], # Inactive gray
            
            ['#d666a6', '#d666a6'], # Pink (used)
            ['#74AFAB', '#74AFAB'], # Cyan (used)

            ['#2093bd', '#2093bd'], # Cyan
            ['#ffffff', '#ffffff']] # White

colors=init_colors()

#-----LAYOUT-THEME-----#
def init_layout_theme():
    return {"margin":15,
            "border_width":2,
            "border_focus":colors[2],
            "border_normal":'#b7a7c2'}

#layout_theme=init_layout_theme()


#-----BINDS-----#
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "a", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "d", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "s", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "w", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key(["control"], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Hide bar
    Key([mod], "b", lazy.hide_show_bar("top")),   
]


#-----GROUPS-----#
group_names=[("TER", {'layout':'columns'}),
            ("MAIN", {'layout':'columns'}),
            ("WWW", {'layout':'columns'}),
            ("FILE", {'layout':'columns'}),
            ("COM", {'layout':'columns'}),
            ("MUS", {'layout':'columns'}),
            ("VBOX", {'layout':'columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names] 

for i, (name, kwargs) in enumerate(group_names, 1):     
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group     
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send window to another group


#-----LAYOUTS-----#
layouts = [
    #layout.Columns(layout_theme)
    #layout.Floating(border_focus=colors[6], border_normal=colors[0], margin=5, border_width=1),
    layout.Columns(border_focus=colors[6], border_normal=colors[0], margin=5, border_width=1),
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


#-----WIDGETS-----#
widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

# Separetor widget abstraction
separate = lambda bcolor: widget.Sep (
    linewidth=0,
    padding=10,
    background=bcolor,
    size_percent=0,
)

# Right rounded corner widget
right_corner = lambda fcolor: widget.TextBox(
    text="⬤  ",
    fontsize=40,
    background=colors[0],
    foreground=fcolor,
    max_chars=1,
    padding=-12,
)

# Left rounded corner widget
left_corner = lambda fcolor: widget.TextBox(
    text="  ⬤",
    fontsize=40,
    background=colors[0],
    foreground=fcolor,
    max_chars=1,
    padding=-12,
)

screens = [
    Screen(
        top=bar.Bar(
            [
                separate(colors[0]),
                widget.GroupBox(
                    fontsize=10,
                    highlight_method='line',
                    borderwidth=3,
                    margin=3,
                    padding_x=5,
                    padding_y=5,
                    this_current_screen_border=colors[2],
                    this_screen_border=colors[4],
                    highlight_color=colors[5],
                    background=colors[0],
                    invert_mouse_wheel=False
                    ),
                
                separate(colors[0]),
                separate(colors[0]),
                widget.Prompt(
                    background=colors[0]
                    ),
                separate(colors[0]),
                separate(colors[0]),

                widget.WindowName(
                    max_chars=60,
                    background=colors[0],
                    foreground=colors[7]
                    ),

                left_corner(colors[6]),
                separate(colors[6]),
                widget.Clock(
                    format='%A %d-%m-%Y %H:%M', 
                    background=colors[6],
                    foreground=colors[9],
                    ),
                separate(colors[6]),
                right_corner(colors[6]),

                widget.Spacer(
                    background=colors[0]
                    ),

                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.Systray(
                    padding=10,
                    icon_size=20,
                    background=colors[0]
                    ),
                separate(colors[0]),
                
                left_corner(colors[7]),
                separate(colors[7]),
                widget.TextBox(
                    text='🔈',
                    fontsize=15,
                    background=colors[7],
                    foreground=colors[9]
                    ),
                widget.Volume(
                    background=colors[7],
                    emoji=False,
                    update_interval=0.05,
                    foreground=colors[9],
                    ),
                separate(colors[7]),
                right_corner(colors[7]),

                left_corner(colors[6]),
                separate(colors[6]),
                widget.TextBox(
                    text='⟳',
                    fontsize=20,
                    background=colors[6],
                    foreground=colors[9]
                    ),
                widget.CheckUpdates(
                    background=colors[6],
                    distro='Arch_checkupdates',
                    display_format='{updates} Updates',
                    no_update_string='No Updates',
                    update_interval=1800,
                    colour_have_updates=colors[9],
                    colour_no_updates=colors[9],
                    foreground=colors[9],
                    ),
                separate(colors[6]),
                right_corner(colors[6]),

                left_corner(colors[7]),
                separate(colors[7]),
                widget.TextBox(
                    text='🖬',
                    fontsize=15,
                    background=colors[7],
                    foreground=colors[9]
                    ),
                widget.Memory(
                    measure_mem='M',
                    measure_swap='M', 
                    background=colors[7],
                    foreground=colors[9],
                    format='{MemUsed: .0f} |{MemTotal: .0f}'
                    ),
                separate(colors[7]),
                right_corner(colors[7]),

                left_corner(colors[6]),
                separate(colors[6]),
                widget.Net(
                    interface="enp3s0", 
                    format='{down}↓{up}↑', 
                    background=colors[6],
                    foreground=colors[9],
                    ),
                separate(colors[6]),
                right_corner(colors[6]),

                separate(colors[0]),
                widget.QuickExit(
                    background=colors[0],
                    countdown_format=' ⏻ ',
                    countdown_start=1,
                    default_text=' ⏻ ',
                    fontsize=20,
                    foreground=colors[3],
                    ),
                separate(colors[0]),
            ],
            size=24,
            margin=[5, 5, 0, 5],
        ),
    ),
]

#-----REST-----#
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
