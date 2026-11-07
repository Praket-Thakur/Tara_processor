rom_hex = [0x000040]*2048
pc_notinc = {20, 21, 22, 23}
for i in range(128):
    add = i*16
    rom_hex[add] = 0x8000
    opp = i & 0x1f
    add1 = add + 1
    rom_hex[add1] = 0x06200
    add2 = add + 2
    rom_hex[add2] = 0x081000

#NOP : opcode = 00000
for i in range(4):
    add = (1<<9)
    add = add*i
    add = add + 3
    rom_hex[add] = 0x60040

#HLT : opcode = 00001
for i in range(4):
    add = (1<<9)
    add = add*i
    add = add + 3 + (1<<4)
    rom_hex[add] = 0x20

#MOV : opcode = 00010
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<5)
    add4 = add + 4 + (1<<5)
    rom_hex[add3] = 0x180400
    rom_hex[add4] = 0x60040

#LIL : opcode = 00011
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<5) + (1<<4)
    add4 = add + 4 + (1<<5) + (1<<4)
    rom_hex[add3] = 0x200400
    rom_hex[add4] = 0x60040

#LIH : opcode = 00100
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<6)
    add4 = add + 4 + (1<<6)
    rom_hex[add3] = 0x480400
    rom_hex[add4] = 0x60040


#ADD : opcode = 01001 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7) + (1<<4)
    add4 = add + 4 + (1<<7) + (1<<4)
    rom_hex[add3] = 0x400889
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#SUB : opcode = 01010 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7) + (1<<5)
    add4 = add + 4 + (1<<7) + (1<<5)
    rom_hex[add3] = 0x40088a
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#ADDI : opcode = 01011 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7) + (1<<4) + (1<<5)
    add4 = add + 4 + (1<<7) + (1<<4) + (1<<5)
    rom_hex[add3] = 0x400889
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#AND : opcode = 01101 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7) + (1<<4) + (1<<6)
    add4 = add + 4 + (1<<7) + (1<<4) + (1<<6)
    rom_hex[add3] = 0x40088d
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#OR : opcode = 01110 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7) + (1<<5) + (1<<6)
    add4 = add + 4 + (1<<7) + (1<<5) + (1<<6)
    rom_hex[add3] = 0x40088e
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#XOR : opcode = 01111 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7) + (1<<4) + (1<<6) + (1<<5)
    add4 = add + 4 + (1<<7) + (1<<4) + (1<<6) + (1<<5)
    rom_hex[add3] = 0x40088f
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#NOT : opcode = 10000 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8)
    add4 = add + 4 + (1<<8)
    rom_hex[add3] = 0x400890
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040


####Note - To check
#SHL : opcode = 10001 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<4)
    add4 = add + 4 + (1<<8) + (1<<4)
    rom_hex[add3] = 0x400891
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#SHR : opcode = 10010 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<5)
    add4 = add + 4 + (1<<8) + (1<<5)
    rom_hex[add3] = 0x400892
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#SLT : opcode = 10011 : Status_load = 1
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<5) + (1<<4)
    add4 = add + 4 + (1<<8) + (1<<5) + (1<<4)
    rom_hex[add3] = 0x400893
    rom_hex[add4] = 0x400c00
    rom_hex[add4+1] = 0x60040

#LDW : opcode = 00101
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<4) + (1<<6)
    add4 = add + 4 + (1<<4) + (1<<6)
    rom_hex[add3] = 0x400809 #off5 + rb -> acc
    rom_hex[add4] = 0x408800 #acc -> mar
    rom_hex[add4+1] = 0x086200 #mem[mar] -> mdr
    rom_hex[add4+2] = 0x080400 #mdr -> reg_file
    rom_hex[add4+3] = 0x60040

#STW : opcode = 00110
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<6) + (1<<5)
    add4 = add + 4 + (1<<6) + (1<<5)
    rom_hex[add3] = 0x400809 #off5 + rb -> acc
    rom_hex[add4] = 0x408800 #acc -> mar
    rom_hex[add4+1] = 0x182000 #reg_file -> mdr
    rom_hex[add4+2] = 0x080100 #mdr -> mem[mar]
    rom_hex[add4+3] = 0x60040


#### Note : Even address reads from higher byte of word
#LDB : opcode = 00111
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<6) + (1<<5) + (1<<4)
    add4 = add + 4 + (1<<6) + (1<<5) + (1<<4)
    rom_hex[add3] = 0x400809 #off5 + rb -> acc
    rom_hex[add4] = 0x408800 #acc -> mar
    rom_hex[add4+1] = 0x086200 #mem[mar] -> mdr
    rom_hex[add4+2] = 0x080400 #mdr -> reg_file
    rom_hex[add4+3] = 0x60040


#### Note : Even address writes on higher byte of word
#STB : opcode = 01000
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<7)
    add4 = add + 4 + (1<<7)
    rom_hex[add3] = 0x400809 #off5 + rb -> acc
    rom_hex[add4] = 0x408800 #acc -> mar
    rom_hex[add4+1] = 0x182000 #reg_file -> mdr
    rom_hex[add4+2] = 0x080100 #mdr -> mem[mar]
    rom_hex[add4+3] = 0x60040

#JMP : opcode : 10110
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<6) + (1<<5)
    add4 = add + 4 + (1<<8) + (1<<6) + (1<<5)
    rom_hex[add3] = 0x070000 #add pc
    rom_hex[add4] = 0x060040

#BZ : opcode : 10100
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<6)
    add4 = add + 4 + (1<<8) + (1<<6)
    rom_hex[add3] = 0x400809 #set status reg
    if i < 2 :
        rom_hex[add4] = 0x060000 #pc += 2
        rom_hex[add4+1] = 0x40
    else :
        rom_hex[add4] = 0x070000 #add pc
        rom_hex[add4+1] = 0x060040

#BN : opcode : 10101
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<6) + (1<<4)
    add4 = add + 4 + (1<<8) + (1<<6) + (1<<4)
    rom_hex[add3] = 0x400809 #set status reg
    if i&1 == 0 :
        rom_hex[add4] = 0x060000 #pc += 2
        rom_hex[add4+1] = 0x40
    else :
        rom_hex[add4] = 0x070000 #add pc
        rom_hex[add4+1] = 0x060040

#CALL : opcode : 10111
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<5) + (1<<6) + (1<<4)
    add4 = add + 4 + (1<<8) + (1<<5) + (1<<6) + (1<<4)
    rom_hex[add3] = 0x000400 #write reg_file
    rom_hex[add4] = 0x470809 #r6 + 2 -> acc, pc_add : status_load = 0, Note : pc read is direct and not through the bus, so it's lite
    rom_hex[add4+1] = 0x400c00 #acc -> r6
    rom_hex[add4+2] = 0x060040

#RET : opcode : 11000
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<7)
    add4 = add + 4 + (1<<8) + (1<<7)
    rom_hex[add3] = 0x1c0000 #r6 -> pc
    rom_hex[add4] = 0x40

#PUSH : opcode : 11001
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<7) + (1<<4)
    add4 = add + 4 + (1<<8) + (1<<7) + (1<<4)
    rom_hex[add3] = 0x40080a #r7 decrement
    rom_hex[add4] = 0x400c00 
    rom_hex[add4+1] = 0x188000 #r7 -> mar
    rom_hex[add4+2] = 0x002000 #mdr load. Directly through QB, hardcoded.
    rom_hex[add4+3] = 0x080100 #mdr -> mem[mar]
    rom_hex[add4+4] = 0x60040

#POP : opcode : 11010
for i in range(4):
    add = (1<<9)
    add = add*i
    add3 = add + 3 + (1<<8) + (1<<7) + (1<<5)
    add4 = add + 4 + (1<<8) + (1<<7) + (1<<5)
    rom_hex[add3] = 0x188000 #r7 -> mar
    rom_hex[add4] = 0x086200 #mem[mar] -> mdr
    rom_hex[add4+1] = 0x080400 #mdr -> reg_file
#### Note : On falling edge of the clock cycle and when alu_out is set, the RD is changed to 7 using a flip flop for holding
    rom_hex[add4+2] = 0x400809 #r7 increment
    rom_hex[add4+3] = 0x400c00
    rom_hex[add4+4] = 0x60040
#### Flip flop is reset next time mar is loaded btw. i.e. first step of next fetch cycle

with open("control_rom.hex", "w") as f:
    f.write("v2.0 raw\n")
    for i in rom_hex:
        f.write(f"{i:X}\n")
