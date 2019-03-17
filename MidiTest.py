import mido

inports = mido.get_input_names()

index = [i for i, s in enumerate(inports) if 'VirtualMidiPort1' in s]

inport = mido.open_input(inports[index[0]])

print('Inport = ' + inport.name)
