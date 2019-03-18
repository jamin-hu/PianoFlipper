import mido
from mido import Message
from mido import MidiFile
import os

filePath = 'MidiRecordings/Chopin/chpn_op10_e12.mid'

mid = MidiFile(filePath)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.type == "note_on" or msg.type == "note_off" or msg.type == "polytouch":
            print("Original note = " + str(msg.note))
            msg.note = 127-msg.note
            #The messages here being modified are still attached to their
            #parent midi file somehow
            print("Flipped note = " + str(msg.note))

folderPath = os.path.dirname(filePath)
composer = os.path.basename(folderPath)
piece = os.path.basename(filePath)

mid.save('FlippedMidiRecordings/' + composer + '/flipped_' + piece)
