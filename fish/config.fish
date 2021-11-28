if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -U fish_greeting

shuf -n 3 ~/.local/share/words.txt | lolcat
