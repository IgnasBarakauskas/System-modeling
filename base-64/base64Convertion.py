import base64
from PIL import Image


def main():
    printImg()
    printText()
    saveAsImage()


def saveAsImage():
    html = getTextFromFile('base-64/base64.txt')
    textBase64 = geBase64FromHtml(html)
    base64_bytes = textBase64.encode('ascii')
    with open("base-64/decodedAnswer.png", "wb") as fh:
        fh.write(base64.decodebytes(base64_bytes))


def geBase64FromHtml(html):
    for line in html:
        if line.startswith("<img"):
            startIndex = line.index("base64")+7
            endOfText = line[startIndex:]
            endIndex = endOfText.index('"')
            return endOfText[:endIndex]


def printText():
    text = getTextFromFile("base-64/inputText.txt")[0]
    text64 = encodeTo64String(text)
    textDecoded = decodeFrom64String(text64)
    print("String encoding to base 64")
    print("____________________________________")
    print("Default value: ", text)
    print("Encoded value: ", text64)
    print("Decoded value: ", textDecoded)
    print("____________________________________")


def printImg():
    img64 = imgToBase64("base-64/image.png")
    print("Image in base64:\n", img64)
    print("____________________________________")


def encodeTo64String(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')


def decodeFrom64String(text):
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')


def getTextFromFile(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return(lines)


def imgToBase64(path):
    with open(path, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        encodedMyString = my_string.decode("utf-8")
    return(encodedMyString)


if __name__ == "__main__":
    main()
