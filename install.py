## Script to install all the necessary packages and dotfiles

import os

# Install packages
os.system("sudo apt-get install -y git vim zsh curl polybar rofi i3 feh kitty neofetch fonts-powerline")

os.system("cd")
os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ")
os.system("git clone https://github.com/zsh-users/zsh-autosuggestions.git")
os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git")


os.system('cd "$OLDPWD"')

## move everything to .config and replace the files if they already exist
os.system("cd /dotfiles && cp -f * ~")

