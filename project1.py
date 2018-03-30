alphabet='abcdefghijklmnopqrstuvwxyz'

key=3	
key1=-3

newmessage=""

print "sender"
message=raw_input("please enter your message:")

for character in message:

	if character in alphabet:
	
		position=alphabet.find(character)
		
		#print (position)
		
		newposition = (position + key) % 26
		
		
		#print (newposition) 
		
		newcharacter=alphabet[newposition] 
		
		# print ("the new character is:"),newcharacter	
		

		newmessage+=newcharacter 

	else:
		newmessage+=character

	
print "the the encrypted message is :",newmessage

print "Receiver:"
print "the message is:",newmessage


message=newmessage
newmessage1=''

for character in message:

	if character in alphabet:
	
		position=alphabet.find(character)
		
		#print (position)
		
		newposition = (position + key1) % 26
		
		
		#print (newposition) 
		
		newcharacter=alphabet[newposition] 
		
		# print ("the new character is:"),newcharacter	
		

		newmessage1+=newcharacter 

	else:
		newmessage1+=character
print "the decrypt message is",newmessage1




