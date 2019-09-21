import mido
from mido import Message
from mido import MidiFile

filePath = 'GsMirroredMidiRecordings/ChopinEtudes/GsMirrorred_chet1012.mid'

#filePath = 'MidiRecordings/ChopinEtudes/chet1012.mid'

outports = mido.get_output_names()
print(outports)
index = [i for i, s in enumerate(outports) if 'MIDISPORT' in s]
outport = mido.open_output(outports[index[0]])

for msg in MidiFile(filePath).play():
    outport.send(msg)
