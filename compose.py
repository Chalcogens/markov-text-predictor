import string
from graph import Graph, Vertex
import random

def get_words_from_text(text_path):
    with open(text_path, "rb") as f:
        text = f.read().decode("utf-8")
        text = " ".join(text.split()) #turns whitespaces, tabs, newlines, ... with a single space, so splitting in line 11 works smoothly
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split() #split on spaces
    return words

def make_graph(words):
    g = Graph()
    previous_word = None
    # for each word in text, check if it's in the graph, and if not then add it as an edge
    # otherwise, increment existing edge by 1.
    # set word to previous one and iterate
    # generate probability mappings here
    for word in words:
        word_vertex = g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for i in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main():
    # step 1: get words from text
    words = get_words_from_text(".txt")

    # step 2: make a graph using those words
    g = make_graph(words)

    # step 3: generate x number of subsequent words (x defined by user)
    composition = compose(g, words, 100)
    return " ".join(composition)

if __name__ == "__main__":
    print(main())



