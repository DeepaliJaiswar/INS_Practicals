AlphabeticSet = {
    'a':'q' ,'b':'w' ,
    'c':'e' ,'d':'r' ,
    'e':'t' ,'f':'y',
    'g':'u' ,'h': 'i',
    'i':'o' ,'j': 'p',
    'k':'a' ,'l': 's',
    'm':'d' ,'n':'f',
    'o':'g' ,'p':'h' ,
    'q':'j' ,'r':'k' ,
    's':'l' ,'t':'z' ,
    'u':'x' ,'v':'c' ,
    'w':'v' ,'x':'b' ,
    'y':'n' ,'z':'m',
}
def monoalphabetic(text) :
    result = ""

    input = text.lower()
    for i in input:
        result += AlphabeticSet[i]
    return result

string = input("Enter a string : ")
print("Plain Text : ",string)
output_string = monoalphabetic(string)
print("Cipher Text : ",output_string)

