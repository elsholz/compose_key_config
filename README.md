# Compose Key Config
This git repository contains my compose key file and will later contain a small Python script for generating this file dynamically.

#### To use the compose key configuration do the following:
1. Configure the compose key on your system (requires X)
2. Run the following command: <br>
`user@device:~$ cp <path>/<to>/<repo>/.XCompose ~/`<br>
This will copy the default config file to your home directory. If you made a config file earlier, be sure to back it up, as it will be overwritten. See the options below for
<br>You might need to run `pip install -r requirements.txt`.
3. Log off and log in again, have fun!

#### Options
`user@device:~$ python make_config.py [options]`

- `-s` or `--stdout`: emits output to stdout (e.g. terminal)
- `-nr` or `--no-readme`: Skips creation of README.md
- `-sl` or `--save-locally`: Config is saved locally (instead of in home directory)

#### List of Key Combinations
In the following, key combinations and their result will be presented. The symbols are separated into categories that roughly match their use cases.


### Marks
|Combination|Result|
|---|---|
| \<c\> \<h\> \<e\> \<c\> \<k\> | ✓ | 
| \<c\> \<r\> \<s\> | × | 

### Arrows
|Combination|Result|
|---|---|
| \<a\> \<u\> \<p\> | ↑ | 
| \<a\> \<d\> \<o\> \<w\> \<n\> | ↓ | 

### Number Symbols
|Combination|Result|
|---|---|
| \<n\> \<n\> | ℕ | 
| \<w\> \<n\> | ℤ | 
| \<r\> \<e\> \<a\> \<l\> | ℝ | 
| \<c\> \<n\> | ℂ | 
| \<r\> \<a\> \<t\> | ℚ | 
| \<q\> \<u\> \<a\> \<t\> | ℍ | 
| \<c\> \<a\> \<r\> \<d\> | ℵ | 

### Greek Letters
|Combination|Result|
|---|---|
| \<a\> \<l\> | α | 
| \<b\> \<e\> \<t\> | β | 
| \<g\> \<a\> \<m\> | γ | 
| \<G\> \<A\> \<M\> | Γ | 
| \<l\> \<a\> \<m\> | λ | 
| \<L\> \<A\> \<M\> | Λ | 
| \<g\> \<t\> \<h\> | θ | 
| \<G\> \<T\> \<H\> | Θ | 
| \<o\> \<m\> | ω | 
| \<O\> \<M\> | Ω | 
| \<d\> \<e\> \<l\> | δ | 
| \<D\> \<E\> \<L\> | Δ | 
| \<s\> \<i\> \<g\> | σ | 
| \<S\> \<I\> \<G\> | Σ | 
| \<p\> \<i\> | π | 
| \<P\> \<I\> | Π | 
| \<e\> \<p\> \<s\> | Ɛ | 
| \<p\> \<h\> \<i\> | φ | 
| \<P\> \<H\> \<I\> | Φ | 

### Symbols for Logic Class
|Combination|Result|
|---|---|
| \<p\> \<m\> | ± | 
| \<s\> \<q\> \<r\> \<t\> | √ | 
| \<e\> \<x\> \<q\> | ∃ | 
| \<v\> \<m\> | ⊤ | 
| \<s\> \<u\> \<b\> | ⊆ | 
| \<i\> \<e\> | ∈ | 
| \<f\> \<a\> | ∀ | 
| \<u\> \<n\> | ∪ | 
| \<n\> \<o\> \<t\> | ¬ | 
| \<i\> \<m\> \<p\> | → | 
| \<o\> \<r\> | ∨ | 
| \<e\> \<q\> \<v\> | ↔ | 
| \<a\> \<n\> \<d\> | ∧ | 
| \<s\> \<p\> \<r\> | ⊇ | 
| \<t\> \<s\> \<p\> \<r\> | ⊃ | 
| \<e\> \<s\> | ∅ | 
| \<f\> \<m\> | ⊥ | 
| \<i\> \<n\> \<t\> | ∩ | 
| \<i\> \<n\> \<e\> | ∉ | 
| \<t\> \<s\> \<u\> \<b\> | ⊂ | 
| \<p\> \<r\> \<o\> \<p\> | φ | 

### Emojis
|Combination|Result|
|---|---|
| \<f\> \<i\> \<r\> \<e\> | 🔥 | 
| \<j\> \<o\> \<y\> | 😂 | 
| \<g\> \<l\> \<a\> \<d\> | 😊 | 
| \<c\> \<o\> \<o\> \<l\> | 😎 | 
| \<h\> \<m\> \<m\> \<m\> | 🤔 | 
| \<c\> \<o\> \<f\> \<f\> | ☕️﻿ | 
| \<h\> \<a\> \<p\> \<p\> | 😊 | 
| \<s\> \<a\> \<d\> | 😞 | 
| \<t\> \<u\> \<x\> | 🐧 | 
| \<m\> \<o\> \<n\> \<k\> | 🙈 | 
| \<k\> \<i\> \<t\> | 🐈 | 
| \<d\> \<o\> \<g\> | 🐕 | 
| \<p\> \<y\> | 🐍 | 
| \<s\> \<u\> \<r\> \<p\> | 😲 | 
| \<f\> \<p\> \<a\> \<l\> \<m\> | 🤦 | 
| \<w\> \<i\> \<n\> \<k\> | 😉 | 
| \<t\> \<r\> \<e\> \<a\> \<s\> | 💰 | 
| \<t\> \<u\> \<p\> | 👍 | 
| \<c\> \<a\> \<k\> \<e\> | 🎂 | 

### Math Symbols
|Combination|Result|
|---|---|
| \<l\> \<e\> \<q\> | ≤ | 
| \<m\> \<e\> \<q\> | ≥ | 
| \<i\> \<n\> \<f\> | ∞ | 
| \<n\> \<e\> \<q\> | ≠ | 
| \<a\> \<e\> \<q\> | ≈ | 
| \<f\> \<t\> | ℱ | 
| \<i\> \<d\> | ≡ | 
| \<n\> \<i\> \<d\> | ≢ | 

### Characters in Math Font
|Combination|Result|
|---|---|
| \<m\> \<a\> \<A\> | 𝔸 | 
| \<m\> \<a\> \<B\> | 𝔹 | 
| \<m\> \<a\> \<C\> | ℂ | 
| \<m\> \<a\> \<D\> | 𝔻 | 
| \<m\> \<a\> \<E\> | 𝔼 | 
| \<m\> \<a\> \<F\> | 𝔽 | 
| \<m\> \<a\> \<G\> | 𝔾 | 
| \<m\> \<a\> \<H\> | ℍ | 
| \<m\> \<a\> \<I\> | 𝕀 | 
| \<m\> \<a\> \<J\> | 𝕁 | 
| \<m\> \<a\> \<K\> | 𝕂 | 
| \<m\> \<a\> \<L\> | 𝕃 | 
| \<m\> \<a\> \<M\> | 𝕄 | 
| \<m\> \<a\> \<N\> | ℕ | 
| \<m\> \<a\> \<O\> | 𝕆 | 
| \<m\> \<a\> \<P\> | ℙ | 
| \<m\> \<a\> \<Q\> | ℚ | 
| \<m\> \<a\> \<R\> | ℝ | 
| \<m\> \<a\> \<S\> | 𝕊 | 
| \<m\> \<a\> \<T\> | 𝕋 | 
| \<m\> \<a\> \<U\> | 𝕌 | 
| \<m\> \<a\> \<V\> | 𝕍 | 
| \<m\> \<a\> \<W\> | 𝕎 | 
| \<m\> \<a\> \<X\> | 𝕏 | 
| \<m\> \<a\> \<Y\> | 𝕐 | 
| \<m\> \<a\> \<Z\> | ℤ | 
| \<m\> \<a\> \<a\> | 𝕒 | 
| \<m\> \<a\> \<b\> | 𝕓 | 
| \<m\> \<a\> \<c\> | 𝕔 | 
| \<m\> \<a\> \<d\> | 𝕕 | 
| \<m\> \<a\> \<e\> | 𝕖 | 
| \<m\> \<a\> \<f\> | 𝕗 | 
| \<m\> \<a\> \<g\> | 𝕘 | 
| \<m\> \<a\> \<h\> | 𝕙 | 
| \<m\> \<a\> \<i\> | 𝕚 | 
| \<m\> \<a\> \<j\> | 𝕛 | 
| \<m\> \<a\> \<k\> | 𝕜 | 
| \<m\> \<a\> \<l\> | 𝕝 | 
| \<m\> \<a\> \<m\> | 𝕞 | 
| \<m\> \<a\> \<n\> | 𝕟 | 
| \<m\> \<a\> \<o\> | 𝕠 | 
| \<m\> \<a\> \<p\> | 𝕡 | 
| \<m\> \<a\> \<q\> | 𝕢 | 
| \<m\> \<a\> \<r\> | 𝕣 | 
| \<m\> \<a\> \<s\> | 𝕤 | 
| \<m\> \<a\> \<t\> | 𝕥 | 
| \<m\> \<a\> \<u\> | 𝕦 | 
| \<m\> \<a\> \<v\> | 𝕧 | 
| \<m\> \<a\> \<w\> | 𝕨 | 
| \<m\> \<a\> \<x\> | 𝕩 | 
| \<m\> \<a\> \<y\> | 𝕪 | 
| \<m\> \<a\> \<z\> | 𝕫 | 
| \<m\> \<a\> \<0\> | 𝟘 | 
| \<m\> \<a\> \<1\> | 𝟙 | 
| \<m\> \<a\> \<2\> | 𝟚 | 
| \<m\> \<a\> \<3\> | 𝟛 | 
| \<m\> \<a\> \<4\> | 𝟜 | 
| \<m\> \<a\> \<5\> | 𝟝 | 
| \<m\> \<a\> \<6\> | 𝟞 | 
| \<m\> \<a\> \<7\> | 𝟟 | 
| \<m\> \<a\> \<8\> | 𝟠 | 
| \<m\> \<a\> \<9\> | 𝟡 | 


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
 
 #### Help with this project
-If you want to commit to this repo, just run ```bash prepare_for_commit.sh``` to generate the new .XCompose file and the new README.md.
