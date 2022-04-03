# !/bin/sh

setxkbmap pl

dunst &
picom -b &
sxhkd &

# For Android Studio to render properly
export _JAVA_AWT_WM_NONREPARENTING=1

$HOME/.local/bin/changewallpaper.sh

# Update dwm bar
while true
do
	DISK=$(echo " $(df -h | grep '/dev/sda2' | awk {'print $3 "/" $2'})")
	DATE=$(echo " $(date '+%a %d %b')")
	TIME=$(echo " $(date '+%H:%M')")
	MEMO=$(echo " $(free -h --si | awk /Mem/ | awk '{ print $3}')")
	VOLU=$(echo " $(awk -F"[][]" '/dB/ { print $2 }' <(amixer sget Master))")

	xsetroot -name "[  $VOLU  ]  [  $MEMO  ]  [  $DISK  ]  [  $DATE  ]  [  $TIME  ]  "
	sleep 1s
done &

# Water drinking reminder
while true; do notify-send "Drink Water"; sleep 15m; done &

# Main dwm loop
while :
do
	$HOME/.local/src/dwm/dwm
done
