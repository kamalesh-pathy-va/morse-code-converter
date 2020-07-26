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

morseCodeInverse = {val:key for key, val in morseCode.items()}

invalidCharacter = "?"
options = ['-f', '-t', '-r']
chosenOptions = []
textStartIndex = 1
for option in options:
	if option in sys.argv:
		chosenOptions.append(option)
if len(chosenOptions) != 0:
	textStartIndex = sys.argv.index(chosenOptions[len(chosenOptions) - 1]) + 1

text = ' '.join(sys.argv[textStartIndex:])
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