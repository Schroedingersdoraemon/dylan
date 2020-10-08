autoload -U promptinit
autoload -Uz compinit && compinit -u
autoload -U colors&&colors
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

compinit
promptinit

export ZSH=/usr/share/oh-my-zsh

#ZSH_THEME="cloud"
prompt pure
DISABLE_AUTO_UPDATE="true"

plugins=(git)

ZSH_CACHE_DIR=$HOME/.oh-my-zsh-cache
if [[ ! -d $ZSH_CACHE_DIR ]]; then
  mkdir $ZSH_CACHE_DIR
fi

source $ZSH/oh-my-zsh.sh
