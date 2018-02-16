import re

def sent_tokenize(text):
    """Split text into sentences."""
    
    # TODO: Split text by sentence delimiters (remove delimiters)
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    # TODO: Remove leading and trailing spaces from each sentence
    for sentence in sentences:
        sentence = sentence.Strip()
    return sentences
    pass  # TODO: Return a list of sentences (remove blank strings)


def word_tokenize(sent):
    """Split a sentence into words."""
    
    # TODO: Split sent by word delimiters (remove delimiters)
    words = re.split(r'\w+([.,]\w+)*|\S+', sent)
    # TODO: Remove leading and trailing spaces from each word
    for word in words:
        word = word.Strip()
    return words
    pass  # TODO: Return a list of words (remove blank strings)


def test_run():
    """Called on Test Run."""

    text = "The first time you see The Second Renaissance it may look boring. Look at it at least twice and definitely watch part 2. It will change your view of the matrix. Are the human people the ones who started the war? Is AI a bad thing?"
    print("--- Sample text ---", text, sep="\n")
    
    sentences = sent_tokenize(text)
    print("\n--- Sentences ---")
    print(sentences)
    
    print("\n--- Words ---")
    for sent in sentences:
        print(sent)
        print(word_tokenize(sent))
        print()  # blank line for readability