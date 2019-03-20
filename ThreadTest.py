import _thread, time

def input_thread(L):
    derp = input()
    L.append(derp)

def do_print():
    L = []
    _thread.start_new_thread(input_thread, (L,))
    while True:
        print('hi mom')
        time.sleep(.1)
        if L:
            print(L)
            print(L[0])
            del(L[0])
            break
do_print()
