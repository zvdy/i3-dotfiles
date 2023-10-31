## Script to install all the necessary packages and dotfiles

import os

# Install packages
os.system("sudo apt-get install -y git zsh curl polybar rofi i3 feh kitty neofetch fonts-powerline")

# Get path and assign it to a variable
path = os.getcwd()

os.system("cd")
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ")
os.system("git clone https://github.com/zsh-users/zsh-autosuggestions.git")
os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git")

## Transverse to the path variable path
os.system("cd " + path)


## move everything to .config and replace the files if they already exist
os.system("cd dotfiles/.config && cp -f -r * ~/.config")
os.system("cd dotfiles/ && cp -f .zshrc ~ && cp -f .p10k.zsh ~ && cp -f .xsessionrc ~")

# chmod the .xsessionrc file to make it executable and polybar/launch.sh
os.system("chmod +x ~/.xsessionrc && chmod +x ~/.config/polybar/launch.sh")

# Getting the wallpaper
os.system("cd dotfiles/wallpapers && cp -f -r * ~/Pictures")

# Download Hack Nerd Font
os.system("wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip")

# Create a directory for fonts
os.system("mkdir -p ~/.local/share/fonts")

# Unzip the downloaded font
os.system("unzip Hack.zip -d ~/.local/share/fonts/")

# Remove the downloaded zip file
os.system("rm Hack.zip")

# Refresh the font cache
os.system("fc-cache -f -v")


print("Reboot now!")