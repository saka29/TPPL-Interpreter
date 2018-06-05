'''TPPL Interpreter
By Saka.
Bad, messy, and terrible because I'm not that good
at Python. But it has a debug option!
Place it in it's own folder along with a file named "code.txt" that contains the code,
because Python does not have multiline inputs.
See https://esolangs.org/wiki/TPPL'''

file = open('code.txt')
code = file.read()
code = code.splitlines()
roll = [0]
trash = []
hold = ''
view = 0
temp = ''
done = False
debug = False # Debug? True or False
if code[0] == 'ENTER BATHROOM' or code[0] == 'ENTER RESTROOM':
    point = 1
    while done == False:
        l = code[point]
        if debug == True:
            print('Roll: ',roll)
            print('HOLD: ',hold)
            print('View Index: ',view)
            print('Point: ',point)
            print('Instruction: ',l)
            print('Trash: ',trash)
        if l=='SET':
            inp = int(input('>>'))
            if inp > 2 or inp < 0:
                print('ERROR: INPUT OUT OF RANGE.')
                done = True
            else:
                roll[view] = inp
            point += 1
        elif l=='ADD':
            roll = [0] + roll
            if len(roll)>1:
                view += 1
            point += 1
        elif l=='EXIT':
            done = True
        elif l=='FLUSH':
            print(chr(int(hold.replace(',',''),3)),end='')
            hold = ''
            point += 1
        elif l=='APPEND':
            if hold != '':
                roll = roll + list(map(int, list(filter(lambda a: a != ',', hold))))
                hold = ''
            else:
                print('ERROR: HOLD IS EMPTY.')
                done = True
            point += 1
        elif 'JUMP' in l:
            n = l.split(' ')
            n = n[1]
            point = int(n)
        elif 'CHECK' in l:
            spl = l.split(' ')
            s = spl[1]
            n = spl[3]
            if hold==s:
                point = int(n)
            else:
                point += 1
        elif l=='WIPE':
            if roll[view]<2:
                roll[view]=roll[view]+1
            else:
                print('ERROR: TOO DIRTY.')
                done = True
            point += 1
        elif l=='CLEAN':
            if roll[view]>0:
                roll[view]=roll[view]-1
            else:
                print('ERROR: TOO WET.')
                done = True
            point += 1
        elif l=='PULL':
            if view != 0:
                view -= 1
            else:
                view = len(roll)-1
            point += 1
        elif l=='RIP':
            if hold == '':
                hold = ','.join(map(str,roll[view:]))
                del roll[view:]
                if view != 0:
                    view -= 1
            else:
                print('ERROR: HOLD IS FULL.')
                done = True
            point += 1
        elif 'TAKE' in l:
            n = l.split(' ')
            n = int(n[1])
            if hold == '':
                hold = trash[n]
                del trash[n]
            else:
                print('ERROR: HOLD IS FULL.')
                done = True
            point += 1
        elif l=='TRASH':
            if hold != '':
                trash.append(hold)
                hold = ''
            else:
                print('ERROR: HOLD IS EMPTY.')
                done = True
            point += 1
        elif l[0]=='#':
            point += 1
        else:
            print('ERROR: UNRECOGNISED COMMAND "',l,'"')
            done = True
else:
    print('ERROR: WHERE ARE WE?')
                
    
