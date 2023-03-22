# markov-text-predictor

Implemented a Markov model for text prediction in Python, which converts a text input into a weighted graph with vertexes used to represent each word. The weight of an edge represents the probability that the two vertices (words) that it connects occur adjacently. Using this graph, the program outputs a string of words, the length of which is decided by the user. The drawback of this model is that it predict grammatically accurate or coherent sentences as it only predicts pairs of words likely to occur together, rather than distinct clauses. 

compose.py: program that accepts .txt file as input and outputs a predicted string in the console
graph.py: contains methods that generate the weighted graph based on input, is used by compose.py

Code adapted and modified from "12 Beginner Python Projects - Coding Course" by freeCodeCamp.org 
