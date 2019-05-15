# Compose Key Config
This git repository contains my compose key file and will later contain a small Python script for generating this file dynamically.

#### To use the compose key configuration do the following:
1. Configure the compose key on your system (requires X)
2. Run the following command: <br>
`user@device:~$ cp <path>/<to>/<repo>/.XCompose ~/`<br>
This will copy the default config file to your home directory. If you made a config file earlier, be sure to back it up, as it will be overwritten. See the options below for

3. Log off and log in again, have fun!

#### Options
`user@device:~$ python make_config.py [options]`

- `-s` or `--stdout`: emits output to stdout (e.g. terminal)
- `-nr` or `--no-readme`: Skips creation of README.md
- `-sl` or `--save-locally`: Config is saved locally (instead of in home directory)

#### List of Key Combinations
In the following, key combinations and their result will be presented. The symbols are separated into categories that roughly match their use cases.

