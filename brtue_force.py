# terminal_controlled_bot_wireless

from cyberbot import *
import radio

def unScramble(word):
    alphabet = "vLR{}:,’01234 56789"
    key = "r:5v 19{4l}’,783062"
    
    result = ""
    for letter in word:
        if letter in key:
            result += alphabet[key.find(letter)]
        else:
            result += letter
    
    print(result)
    return result

radio.on()
radio.config(channel=10,length=64)

sleep(1000)

print("Ready...\n")

while True:
    packet = radio.receive()
    
    if packet is not None:
        print("Received encryption: ", packet)
        packet = unScramble(packet)
        print("Decrypted packet: ", packet)

        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
        