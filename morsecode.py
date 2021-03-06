import sys

morseCode = {
	'a' :'.-',
	'b' :'-...',
	'c' :'-.-.',
	'd' :'-..',
	'e' :'.',
	'f' :'..-.',
	'g' :'--.',
	'h' :'....',
	'i' :'..',
	'j' :'.---',
	'k' :'-.-',
	'l' :'.-..',
	'm' :'--',
	'n' :'-.',
	'o' :'---',
	'p' :'.--.',
	'q' :'--.-',
	'r' :'.-.',
	's' :'...',
	't' :'-',
	'u' :'..-',
	'v' :'...-',
	'w' :'.--',
	'x' :'-..-',
	'y' :'-.--',
	'z' :'--..',
	'1' :'.----',
	'2' :'..---',
	'3' :'...--',
	'4' :'....-',
	'5' :'.....',
	'6' :'-....',
	'7' :'--...',
	'8' :'---..',
	'9' :'----.',
	'0' :'-----',
	' ' :'  '
}

morseCode1 = {
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
	print("Usage: python morsecode.py [options] [text/file]")
	print("\n[options]\n    -t -> represents the input given is normal text\n    -r -> represents the input given should be converted to normal text\n    -f -> represents the input given is a file name (on progress)\n ")

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


def invert(morseText):
	for i in morseText:
		if i not in '.- ':
			return "'-r' option expects morse code to convert text"
	letters = morseText.split(' ')
	output = ""
	for i in letters:
		if i in morseCodeInverse.keys():
			output += morseCodeInverse[i]
		else:
			output += invalidCharacter
	return output

#Don't change
options = ['-f', '-t', '-r', '-h']
selectedOptions = []
textStartIndex = 1

for option in options:
	if option in sys.argv:
		selectedOptions.append(option)
if len(selectedOptions) != 0:
	textStartIndex = sys.argv.index(selectedOptions[len(selectedOptions) - 1]) + 1

text = ' '.join(sys.argv[textStartIndex:])
text = text.lower()

if '-h' in selectedOptions:
	help()
elif '-f' in selectedOptions:
	if '-t' in selectedOptions:
		print("'-f' and '-t' options cannot be used at once.")
		help()
	elif '-r' in selectedOptions:
		print(invert(text))
	elif '-f' in selectedOptions:
		print(convert(text))
elif '-t' in selectedOptions:
	if '-r' in selectedOptions:
		print("'-t' and '-r' options cannot be used at once.")
		help()
	elif '-t' in selectedOptions:
		print(convert(text))
elif '-r' in selectedOptions:
	print(invert(text))
else:
	print(convert(text))


# print(transformedText)
# print(output.strip())
