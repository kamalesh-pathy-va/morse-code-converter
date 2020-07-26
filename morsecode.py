import sys
morseCode = {
	'a' :'•—',
	'b' :'—•••',
	'c' :'—•—•',
	'd' :'—••',
	'e' :'•',
	'f' :'••—•',
	'g' :'——•',
	'h' :'••••',
	'i' :'••',
	'j' :'•———',
	'k' :'—•—',
	'l' :'•—••',
	'm' :'——',
	'n' :'—•',
	'o' :'———',
	'p' :'•——•',
	'q' :'——•—',
	'r' :'•—•',
	's' :'•••',
	't' :'—',
	'u' :'••—',
	'v' :'•••—',
	'w' :'•——',
	'x' :'—••—',
	'y' :'—•——',
	'z' :'——••',
	'1' :'•————',
	'2' :'••———',
	'3' :'•••——',
	'4' :'••••—',
	'5' :'•••••',
	'6' :'—••••',
	'7' :'——•••',
	'8' :'———••',
	'9' :'————•',
	'0' :'—————',
	' ' :'  '
}

invalidCharacter = "?"
text = ' '.join(sys.argv[1:])
text = text.lower()
transformedText = ""
for i in text:
	if i in morseCode.keys():
		transformedText += i
	else:
		transformedText += invalidCharacter


output = ""
for i in transformedText:
	if i != invalidCharacter:
		output += morseCode[i] + ' '
	else:
		output += invalidCharacter

print(transformedText)
print(output.strip())