export PKG_CONFIG_PATH="/usr/lib/pkgconfig:$PKG_CONFIG_PATH"
#export PKG_CONFIG_PATH="/usr/local/lib:$PKG_CONFIG_PATH"

export PKG_CONFIG_PATH

export LD_LIBRARY_PATH="/usr/lib:$LD_LIBRARY_PATH"

export PATH="/usr/local/bin:$PATH"
export PATH="/usr/bin:$PATH"
export PATH="$PATH:/home/dylan/prog/flutter/bin"

export EDITOR="nvim"
export WEB_BROWSER="firefox"

eval "$(zoxide init zsh)"
