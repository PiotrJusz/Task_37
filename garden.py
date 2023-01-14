import spacy

gardenpathSentences = ["The cotton clothing is made of grows in Mississippi.", "The man whistling tunes pianos.", "The government of England plans to raise taxes were defeated.", "The complex houses married and single soldiers and their families.", "I know the words to that song about the queen of Spain don’t rhyme."]

nlp = spacy.load('en_core_web_sm')
word_list = []

# examples of garden path


for sentence in gardenpathSentences:
    print("\nSentence: ", sentence)
    words = nlp(sentence)

    # tokenisation
    words_list = words.text.split()
    print("Sentence after split: ", words_list)
    print("Tokenisation:")
    print([(token, token.orth_, token.orth) for token in words])
    #print("gardenpathSentences:", words)

    # entity recognistion
    # input("Entity recognistaion: ")

    # entity = nlp(sentence)
    print("Entity:")
    print([(i, i.label_, i.label) for i in words.ents])
    if sentence != gardenpathSentences[-1]:
        input("Press any to working on next sentence.")
   





#