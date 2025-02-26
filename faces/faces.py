def main():
    text = input()
    text = convert(text)
    print(text)

def convert(sentence):
    sentence = sentence.replace(':)', '🙂')
    sentence = sentence.replace(':(', '🙁')
    return sentence

   
main()