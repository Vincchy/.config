#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Set the color theme for alacritty
cat ~/.cache/wal/sequences

case $(expr $RANDOM % 15) in
	0)
		neofetch
		;;
	1)
		neofetch
		;;
	2)
		pfetch
		;;
	3)
		colorscript -e ghosts
		;;
	4)
		colorscript -e crunch
		;;
	5)
		colorscript -e alpha
		;;
	6)
		colorscript -e tiefighter1row
		;;
	7)
		colorscript -e panes
		;;
	8)
		colorscript -e monster
		;;
	9)
		colorscript -e jangofett
		;;
	10)
		colorscript -e elfman
		;;
	11)
		colorscript -e fade
		;;
	12)
		colorscript -e mouseface
		;;
	13)
		colorscript -e crunchbang-mini
		;;
	14)
		colorscript -e bloks
		;;
esac


PS1='[\u@\h \W]\$ '

alias dwm_config='nvim ~/.local/src/dwm/config.template.h'
alias dwm_compile="cat ~/.local/src/dwm/config.template.h > ~/.local/src/dwm/config.h; sed -i -e '/PLACE-COLORS-HERE/r /home/vinchy/.cache/wal/colors-wal-dwm.h' /home/vinchy/.local/src/dwm/config.h; make -C ~/.local/src/dwm"

alias wallpaper='~/.local/bin/changewallpaper.sh'

alias backup='sudo mount /dev/sdc1 ~/mount/backup'

alias lol='sudo sysctl -w abi.vsyscall32=0'
alias lolmore='rm -rf ~/.local/share/lutris/runtime/dxvk; sudo sysctl -w abi.vsyscall32=0'

alias ls='exa --color=auto'
alias la='exa -alh --color=auto'
alias lh='exa -a | egrep "^\."'
alias ..='cd ..'

alias yt='ytfzf -t --thumbnail-quality=high --pages=2'
alias lofi='$HOME/.local/bin/lofi.sh'

alias lolkill='pkill "League of Legends.exe"'

# Add custom dmenu to the PATH
export PATH="$HOME/.local/src/dmenu:$PATH"
# export PATH="$HOME/.local/bin:$PATH"
