#! /bin/fish 
nitrogen --restore &
setxkbmap pl
alacritty &
sleep .1
alacritty -e htop &
sleep .1
alacritty &
sleep .1
picom -b
