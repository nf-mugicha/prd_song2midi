#!/usr/bin/env python
# -*- coding: utf-8 -*-

# コードに対応する単音を定義する
chords_list = [
    {"C:maj": ["C4", "E4", "G4"]},
    {"C:min": ["C4", "E!4", "G4"]},
    {"C:dim": ["C4", "E!4", "G!4"]},
    {"C:aug": ["C4", "E4", "G#4"]},
    {"C:maj7": ["C4", "E4", "G4", "B4"]},
    {"C:min7": ["C4", "E!4", "G4", "B!4"]},
    {"C:7": ["C4", "E4", "G4", "B!4"]},
    {"C:dim7": ["C4", "E!4", "G!4", "A4"]},
    {"C:hdim7": ["C4", "E!4", "G!4", "B!4"]},
    {"C:maj6": ["C4", "E4", "G4", "A4"]},
    {"C:min6": ["C4", "E!4", "G4", "A4"]},

    {"C#:maj": ["C#4", "F4", "A!4"]},
    {"C#:min": ["C#4", "E4", "A!4"]},
    {"C#:dim": ["C#4", "E4", "G4"]},
    {"C#:aug": ["C#4", "F4", "A4"]},
    {"C#:maj7": ["C#4", "F4", "A!4", "C5"]},
    {"C#:min7": ["C#4", "E4", "A!4", "B5"]},
    {"C#:7": ["C#4", "F4", "A!4", "B4"]},
    {"C#:dim7": ["C#4", "E4", "G4", "B!4"]},
    {"C#:hdim7": ["C#4", "E4", "A4", "C5"]},
    {"C#:maj6": ["C#4", "F4", "A!4", "B!5"]},
    {"C#:min6": ["C#4", "E4", "A!4", "B!5"]},

    {"D:maj": ["D4", "F#4", "A4"]},
    {"D:min": ["D4", "F4", "A4"]},
    {"D:dim": ["D4", "F4", "G#4"]},
    {"D:aug": ["D4", "F#4", "A#4"]},
    {"D:maj7": ["D4", "F#4", "A4", "C#5"]},
    {"D:min7": ["D4", "F4", "A4", "C5"]},
    {"D:7": ["D4", "F#4", "A4", "C5"]},
    {"D:dim7": ["D4", "F4", "A!4", "C!5"]},
    {"D:hdim7": ["D4", "F4", "A!4", "C5"]},
    {"D:maj6": ["D4", "F#4", "A4", "B4"]},
    {"D:min6": ["D4", "F4", "A4", "B4"]},

    {"D#:maj": ["E!4", "G4", "B!4"]},
    {"D#:min": ["E!4", "G!4", "B!4"]},
    {"D#:dim": ["E!4", "G!4", "A4"]},
    {"D#:aug": ["E!4", "G4", "B4"]},
    {"D#:maj7": ["E!4", "G4", "B!4", "D5"]},
    {"D#:min7": ["E!4", "G!4", "B!4", "D!5"]},
    {"D#:7": ["E!4", "G4", "B!4", "D!5"]},
    {"D#:dim7": ["E!4", "G!4", "A4", "C5"]},
    {"D#:hdim7": ["E!4", "G!4", "A4", "D!5"]},
    {"D#:maj6": ["E!4", "G4", "B!4", "C5"]},
    {"D#:min6": ["E!4", "G!4", "B!4", "C5"]},

    {"E:maj": ["E4", "G#4", "B4"]},
    {"E:min": ["E4", "G4", "B4"]},
    {"E:dim": ["E4", "G4", "A#4"]},
    {"E:aug": ["E4", "G#4", "B#4"]},
    {"E:maj7": ["E4", "G#4", "B4", "D#5"]},
    {"E:min7": ["E4", "G4", "B4", "D5"]},
    {"E:7": ["E4", "G#4", "B4", "D5"]},
    {"E:dim7": ["E4", "G4", "B!4", "D!5"]},
    {"E:hdim7": ["E4", "G4", "B!4", "D5"]},
    {"E:maj6": ["E4", "G#4", "A4", "C#5"]},
    {"E:min6": ["E4", "G4", "A4", "C#5"]},

    {"F:maj": ["F4", "A4", "C5"]},
    {"F:min": ["F4", "A!4", "C5"]},
    {"F:dim": ["F4", "A!4", "B4"]},
    {"F:aug": ["F4", "A4", "C#5"]},
    {"F:maj7": ["F4", "A4", "C5", "E5"]},
    {"F:min7": ["F4", "A!4", "C5", "E!5"]},
    {"F:7": ["F4", "A4", "C5", "E!5"]},
    {"F:dim7": ["F4", "A!4", "B5", "D5"]},
    {"F:hdim7": ["F4", "A!4", "C!5", "E!5"]},
    {"F:maj6": ["F4", "A4", "C5", "D5"]},
    {"F:min6": ["F4", "A!4", "C5", "D5"]},

    {"F#:maj": ["F#4", "A#4", "C#5"]},
    {"F#:min": ["F#4", "A4", "C#5"]},
    {"F#:dim": ["F#4", "A4", "C5"]},
    {"F#:aug": ["F#4", "A#4", "D5"]},
    {"F#:maj7": ["F#4", "A#4", "C#5", "E#5"]},
    {"F#:min7": ["F#4", "A4", "C#5", "E5"]},
    {"F#:7": ["F#4", "A#4", "C#5", "E5"]},
    {"F#:dim7": ["F#4", "A4", "C5", "E!5"]},
    {"F#:hdim7": ["F#4", "A4", "C5", "E5"]},
    {"F#:maj6": ["F#4", "A#4", "C#5", "D#5"]},
    {"F#:min6": ["F#4", "A4", "C#5", "D#5"]},

    {"G:maj": ["G3", "B3", "D4"]},
    {"G:min": ["G3", "B!3", "D4"]},
    {"G:dim": ["G3", "B!3", "D!4"]},
    {"G:aug": ["G3", "B3", "D#4"]},
    {"G:maj7": ["G3", "B3", "D4", "F#4"]},
    {"G:min7": ["G3", "B!3", "D4", "F4"]},
    {"G:7": ["G3", "B3", "D4", "F4"]},
    {"G:dim7": ["G3", "B!3", "D!4", "F!4"]},
    {"G:hdim7": ["G3", "B!3", "D!4", "F4"]},
    {"G:maj6": ["G3", "B3", "D4", "E4"]},
    {"G:min6": ["G3", "B!3", "D4", "E4"]},

    {"G#:maj": ["G#3", "C4", "E!4"]},
    {"G#:min": ["G#3", "C!4", "E!4"]},
    {"G#:dim": ["G#3", "C!4", "D4"]},
    {"G#:aug": ["G#3", "C4", "E4"]},
    {"G#:maj7": ["G#3", "C4", "E!4", "G4"]},
    {"G#:min7": ["G#3", "C!4", "E!4", "G!4"]},
    {"G#:7": ["G#3", "C4", "E!4", "G!4"]},
    {"G#:dim7": ["G#3", "C!4", "D4", "F4"]},
    {"G#:hdim7": ["G#3", "C!4", "D4", "G!4"]},
    {"G#:maj6": ["G#3", "C4", "E!4", "F4"]},
    {"G#:min6": ["G#3", "C!4", "E!4", "F4"]},

    {"A:maj": ["A3", "C#4", "E4"]},
    {"A:min": ["A3", "C4", "E4"]},
    {"A:dim": ["A3", "C4", "D#4"]},
    {"A:aug": ["A3", "C#4", "E#4"]},
    {"A:maj7": ["A3", "C#4", "E4", "G#4"]},
    {"A:min7": ["A3", "C4", "E4", "G4"]},
    {"A:7": ["A3", "C#4", "E4", "G4"]},
    {"A:dim7": ["A3", "C4", "E!4", "G!4"]},
    {"A:hdim7": ["A3", "C4", "E!4", "G4"]},
    {"A:maj6": ["A3", "C#4", "E4", "F#4"]},
    {"A:min6": ["A3", "C4", "E4", "F#4"]},

    {"A#:maj": ["A#3", "D4", "F4"]},
    {"A#:min": ["A#3", "D!4", "F4"]},
    {"A#:dim": ["A#3", "D!4", "E4"]},
    {"A#:aug": ["A#3", "D4", "F#4"]},
    {"A#:maj7": ["A#3", "D4", "F4", "A4"]},
    {"A#:min7": ["A#3", "D!4", "F4", "A!4"]},
    {"A#:7": ["A#3", "D4", "F4", "A!4"]},
    {"A#:dim7": ["A#3", "D!4", "F!4", "G4"]},
    {"A#:hdim7": ["A#3", "D!4", "F!4", "A!4"]},
    {"A#:maj6": ["A#3", "D4", "F4", "A4"]},
    {"A#:min6": ["A#3", "D!4", "F4", "G4"]},

    {"B:maj": ["B3", "D#4", "F#4"]},
    {"B:min": ["B3", "D4", "F#4"]},
    {"B:dim": ["B3", "D4", "F4"]},
    {"B:aug": ["B3", "D#4", "G4"]},
    {"B:maj7": ["B3", "D#4", "F#4", "A#4"]},
    {"B:min7": ["B3", "D4", "F#4", "A4"]},
    {"B:7": ["B3", "D#4", "F#4", "A4"]},
    {"B:dim7": ["B3", "D4", "F4", "A!4"]},
    {"B:hdim7": ["B3", "D4", "F4", "A4"]},
    {"B:maj6": ["B3", "D#4", "F#4", "G4"]},
    {"B:min6": ["B3", "D4", "F#4", "G#4"]}
]


def key2chord(analyzed_chord_name):
    """
    解析結果のコードを単音のリストにバラす関数
    param:
        analyzed_chord_name:  コードのdict
    return:
        result: コードを単音にバラしたリスト
    """
    chord_name = analyzed_chord_name["chord"]
    chords_note_list = [d.get(chord_name)
                        for d in chords_list if d.get(chord_name)]
    print(chords_note_list)
    return chords_note_list[0]


if __name__ == "__main__":
    analyzed_chord_name = {"index": 30,
                           "time": 85.0711898803711, "chord": "F#:min"}
    print(key2chord(analyzed_chord_name))
