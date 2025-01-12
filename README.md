# Find what package manager was used to install a given app

Currently checks for 
- dnf
- flatpak
- any file containing that name in $PATH

### Usage

```console
python3 main.py package_name
```

### Requirements

- Python 3.x
- Fedora (That said, you can modify it to add your prefered package manager(s))


