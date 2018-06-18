text_file = open("yourfilename.txt", "r")
lines = text_file.readlines()
bits = ''.join(lines).strip()

numBits = len(bits)
numEncBits = 0

print "Decoded as ", bits

#encoding
encodedSequence = ""
currentValue = 'zero'
currentZeroCount = 0
currentOneCount = 0

if bits[0:1] == '1':
    encodedSequence = '0,'
    currentValue = 'one'

if bits[len(bits)-1:] == '0':
    bits = bits + '1'

elif bits[len(bits)-1:] == '1':
    bits = bits + '0'

for bit in list(bits):
    if (currentValue == 'zero') & (int(bit) == 0):
        currentZeroCount = currentZeroCount + 1

    elif (currentValue == 'zero') & (int(bit) == 1):
        if currentZeroCount > 0:
            encodedSequence= encodedSequence + str(currentZeroCount)+ ',';
            currentZeroCount = 0
            currentValue = 'one'
            currentOneCount = currentOneCount + 1


    elif (currentValue == 'one') & (int(bit) == 1):
        currentOneCount = currentOneCount + 1

    elif (currentValue == 'one') & (int(bit) == 0):
        if currentOneCount > 0:
            encodedSequence= encodedSequence + str(currentOneCount)+ ',';
            currentOneCount = 0
            currentValue = 'zero'
            currentZeroCount = currentZeroCount + 1

encodedSequence = encodedSequence[:len(encodedSequence)-1]
countDigits = [c.isdigit() for c in encodedSequence].count(True)
countCommas = encodedSequence.count(",")
countEncodedBits = countDigits*3 + countCommas

ratio = float(numBits) / float(countEncodedBits)

print "Encoded as ", encodedSequence
with open('encoded.rle', 'w+') as f:
    f.write(encodedSequence)


#decoding
decodingString = ''
decodeKey = 'zero'
text_file = open("encoded.rle", "r")
lines = text_file.readlines()
elements = []

if(lines[0].split(',')[0] == '0'):
    decodeKey = 'one'
    elements = lines[0].split(',')[1:]
elif(int(lines[0].split(',')[0]) > 0):
    decodeKey = 'zero'
    elements = lines[0].split(',')

for lengthValue in elements:
    if decodeKey == 'zero':

        for i in range(int(lengthValue)):
            decodingString = decodingString + '0'
        decodeKey = 'one'

    elif decodeKey == 'one':

        for i in range(int(lengthValue)):
            decodingString = decodingString + '1'
        decodeKey = 'zero'

print "Decoded as ",decodingString
print "The number of initialy provided bits is ", numBits
print "The number of encoded bits is ", countEncodedBits
print "The compression ratio is ", ratio
