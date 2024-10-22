from textblob import TextBlob

def correct_grammar(text):
    #Createing obj for TextBlob
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

#User input of the sentence
text = input("Enter your Sentence: ")
corrected_text = correct_grammar(text)
print(f"Corrected: {corrected_text}")
