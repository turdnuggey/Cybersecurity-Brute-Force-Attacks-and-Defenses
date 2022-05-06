# terminal_bot_controller_wireless_your_turn.py

from microbit import *
import radio

#def caesar(key, word):
 #   alpha = "vLR{}:,’01234 56789"
  #  result = ""

#    for letter in word:
        
        #letter = letter.upper()
 #       index = ( alpha.find(letter) + key ) % 26
  #      result = result + alpha[index]
    
   # return result

def scramble(word):
    alphabet = "vLR{}:,’01234 56789"
    key = "r:5v 19{4l}’,783062"
    
    result = ""
    for letter in word:
        if letter in alphabet:
            result += key[alphabet.find(letter)]
        else:
            result += letter
    
    print(result)
    return result

radio.on()
radio.config(channel=10,length=64)

sleep(1000)

print("\nSpeeds are -100 to 100\n")

while True:
    try:
        vL = int(input("Enter left speed: "))
        vR = int(input("Enter right speed: "))
        ms = int(input("Enter ms to run: "))

        dictionary = {  }
        dictionary['vL'] = vL
        dictionary['vR'] = vR
        dictionary['ms'] = ms
        
        packet = str(dictionary)
        print("Unencrypted packet: ", packet)
        newPacket = scramble(packet)
    
        print("Send: ", newPacket)
        radio.send(newPacket)
    
        print()

    except:
        print("Error in value entered.")
        print("Please try again. \n")
        