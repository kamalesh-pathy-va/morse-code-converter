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

#Don't change
morseCodeInverse = {val:key for key, val in morseCode.items()}

#Can be changed
invalidCharacter = "?"


def help():
	pass

def convert(text):
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

	return output


#Don't change
options = ['-f', '-t', '-r']
selectedOptions = []
textStartIndex = 1

for option in options:
	if option in sys.argv:
		selectedOptions.append(option)
if len(selectedOptions) != 0:
	textStartIndex = sys.argv.index(selectedOptions[len(selectedOptions) - 1]) + 1

text = ' '.join(sys.argv[textStartIndex:])
text = text.lower()

if '-f' in selectedOptions:
	if '-t' in selectedOptions:
		print("'-f' option and '-t' cannot be used at once.")
		help()
	elif '-r' in selectedOptions:
		print(invert(text))


print(transformedText)
print(output.strip())
