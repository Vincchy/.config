#! /bin/fish
setxkbmap pl

# Wallpaper & compositor
nitrogen --restore &
picom -b

# Notification manager
dunst &

# Custom bindings
sxhkd &

# Terminal setup
alacritty &
sleep .1
alacritty -e htop &
sleep .1
alacritty &
sleep .1
