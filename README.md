# Song Generator

This Python program allows users to generate and play simple songs using a custom notestring format.

## Author

Rodolfo Lopez

## Date

Fall 2019

## Features

- Generate songs from a string of musical notes and modifiers
- Adjust tempo, volume, and octave
- Mix two separate tracks into one song

## Requirements

- Python 3.x
- `sound.py` module (for loading and manipulating sound objects)
- Additional dependencies: numpy, scipy, sounddevice, matplotlib

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install numpy scipy sounddevice matplotlib
```

## Usage

1. Run the `song_generator.py` script
2. Enter a notestring when prompted
3. The program will generate and play the song

## Notestring Format

- Notes: A, B, C, D, E, F, G
- P: Pause
- Numbers (1-9): Note duration
- \> : Increase octave
- <: Decrease octave
- +: Increase volume
- -: Decrease volume
- |: Switch to second track
- [BPM]: Set tempo (e.g., [120] for 120 beats per minute)

## Example

`[120]C2>C<BAG2A2B2>C2`

This notestring sets the tempo to 120 BPM and plays a simple melody.

`>+CCGGAA2GFFEEDD2CGGFFEE2DGGFFEE2DCCGGAA2GFFEEDD2C|+CGEGCA2EBFCGBF2CEGFAEG<2B>EGFAEG<2B>CGEGCA2EBFCGBF2C`

This notestring plays the Twinkle Twinkle Little Star tune.

## Acknowledgements

Dr. Sat Garcia and Dr. Dan Zingaro wrote `sound.py` and I implemented the functions in `song_generator.py`
