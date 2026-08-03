## What?
All the components selections and footprint gathering is made over the JLCPCB ecosystem of part sourcing and its prices.
## Easyeda [footprint] to kicad
Install [easyeda2kicad git](https://github.com/uPesy/easyeda2kicad.py) with 
```bash
pipx install easyeda2kicad
```

### Usage
#### Directory (zsh)
``` zsh
export MPROOT="~/workspace/house-urani/music-player/"
```
#### Command
```bash
easyeda2kicad --full --output $(MPROOT)/music-player-PCB/external/ --lcsc_id=C
```