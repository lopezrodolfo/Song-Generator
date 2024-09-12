"""
Module: comp110_psa4

This module provides functionality to manipulate and generate sound objects.

Author: Rodolfo Lopez - rodolfolopez@sandiego.edu
"""

import sound


def scale_volume(original_sound, factor):
    """
    Decreases the volume of a sound object by a specified factor.

    Paramters:
    original_sound (type; Sound): The sound object whose volume is to be decreased.
    factor (type: float): The factor by which the volume is to be decreased.

    Returns:
    scaled_sound (type: Sound) A new sound object that is a copy of original_sound, but with volumes
    scaled by factor.
    """

    scaled_snd = original_sound.copy()
    for smpl in scaled_snd:
        cur_left = smpl.left
        scaled_left = round(factor * cur_left)
        smpl.left = scaled_left

        cur_right = smpl.right
        scaled_right = round(factor * cur_right)
        smpl.right = scaled_right

    return scaled_snd


def mix_sounds(snd1, snd2):
    """
    Mixes together two sounds (snd1 and snd2) into a single sound.
    If the sounds are of different length, the mixed sound will be the length
    of the longer sound.

    This returns a new sound: it does not modify either of the original
    sounds.

    Parameters:
    snd1 (type: Sound) - The first sound to mix
    snd2 (type: Sound) - The second sound to mix

    Returns:
    mixed_sound (type: Sound) A Sound object that combines the two parameter sounds into a
    single, overlapping sound.
    """

    if len(snd1) > len(snd2):
        long_snd = snd1
        short_snd = snd2
    else:
        long_snd = snd2
        short_snd = snd1

    mixed_snd = long_snd.copy()
    for smpl_num, other_smpl in enumerate(short_snd):
        mixed_smpl = mixed_snd[smpl_num]
        new_left = mixed_smpl.left + other_smpl.left
        new_right = mixed_smpl.right + other_smpl.right
        mixed_smpl.left = new_left
        mixed_smpl.right = new_right

    return mixed_snd


def song_generator(notestring):
    """
    Generates a sound object containing a song specified by the notestring.

    Parameter:
    notestring (type: string) - A string of musical notes and characters to
    change the volume and/or octave of the song.

    Returns:
    song (type: Sound) A song generated from the notestring given as a paramter.
    """

    snd1 = sound.create_silent_sound(1)
    snd2 = sound.create_silent_sound(1)

    smpls_per_note = 14700
    note_len = 1
    octave = 0
    volume_mult = 1.0
    on_second_snd = False

    notestring = notestring.upper()
    if notestring[0] == "[":
        end = notestring.find("]")
        bpm = int(notestring[1:end])
        bps = bpm / 60
        smpls_per_note = int(44100 // bps)

    for _, ch in enumerate(notestring):
        actual_len = smpls_per_note * note_len

        if ch in "ABCDEFG":
            new_note = sound.Note(ch, actual_len, octave=octave)
            note_len = 1
            if not on_second_snd:
                snd1 += scale_volume(new_note, volume_mult)
            else:
                snd2 += scale_volume(new_note, volume_mult)

        elif ch == "P":
            note_len = 1
            if not on_second_snd:
                snd1 += sound.create_silent_sound(actual_len)
            else:
                snd2 += sound.create_silent_sound(actual_len)

        elif ch.isdigit():
            note_len = int(ch)

        elif ch == ">":
            octave += 1

        elif ch == "<":
            octave -= 1

        elif ch == "+":
            volume_mult += 0.2

        elif ch == "-":
            volume_mult -= 0.2

        elif ch == "|":
            on_second_snd = True
            volume_mult = 1.0
            octave = 0

    song = mix_sounds(snd1, snd2)

    return song


# Don't modify anything below this point.


def main():
    """
    Asks the user for a notestring, generates the song from that
    notestring, then plays the resulting song.
    """

    print("Enter a notestring (without quotes):")
    ns = input()
    song = song_generator(ns)
    song.play()
    sound.wait_until_played()


if __name__ == "__main__":
    main()
