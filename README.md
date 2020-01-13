# iTerm-pyenv

Shows the current python environment name in iTerm's status bar, saving precious space in the shell prompt area.



## Installation

1. Copy [`pyenv.py`](./pyenv.py) to the iTerm Scripts directory.

```bash
mkdir -p ~/Library/Application\ Support/iTerm2/Scripts/AutoLaunch
cp pyenv.py ~/Library/Application\ Support/iTerm2/Scripts/AutoLaunch
```

2. Add the following lines to `fish_prompt`

```bash
nano ~/.config/fish/functions/fish_prompt.fish
```

```fish
function fish_prompt
    # set python env for iTerm
    set py (pyenv version-name)
    if set -q VIRTUAL_ENV
        set py (basename $VIRTUAL_ENV)
    end
    iterm2_set_user_var py $py
    ##

		....    
end
```



