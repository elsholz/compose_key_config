
#### Split Compose Key Config into multiple Files for easy editing
To make life easier, the compose keys are now split up into separate files. To enable a file of compose keys, add it to the `include` list in the `keys.yaml` file.

Example:
To remove compose keys for Greek letters, comment out the file for greek letters like so: <br>
```yaml
- include:
    …
    - number_symbols
    # - greek_letters
    - logic_class
    …
 ```
 The next time you run ```python ./make_config.py``` those letters will be excluded