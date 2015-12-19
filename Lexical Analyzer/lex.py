#!/bin/usr/env python 3
'''
Name:
    lex.py
Summary:
    Lexical Analyzer of Compiler (Rough Draft)
    Source Code: C (A simplified version)
    Note that token definition are decoupled from module.
Acknowledgement:
    http://stackoverflow.com/questions/17848207/making-a-lexical-analyzer
    https://github.com/x2adrew/lexical_python
'''
# Import regular expression module to parse definition file
import re

# Permits usage of a dictionary of lists
from collections import defaultdict

# Keep track of line number in case of error diagnosis
line_number = 1
# File which contains source code
# TODO: Ensures that script accept parameter
source = open("file.txt", "r")
# File which contains definition for tokens
# TODO: Set up a minimal version of Definition.txt, for HereDoc, to allow lex.py to be independent
definition_text = "SampleDefinition.txt"
# Dictionary of list containing tokens
token_dict = defaultdict(list)

########################################
# Definition
########################################
def define(self, file):
    file = open(definition_text)
    for line in self.file:
    # Strip trailing newline characters
    line = line.rstrip("\n")
    # Split using regular expression at '::='
    tokenDef = re.split("\s*::=\s*", line, maxsplit=1)
    tokenItem = tokenDef[0]
    # Split using regular expression at '|'
    tokenRules = re.split("\s+\|\s+", tokenDef[1])
        # Generate dictionary of rules for language
        for rule in tokenRules:
            token_dict[rule].append(tokenItem)
            # Use a inverted using list comprehension with
            # dict([[v,k] for k,v in mydict.items()])

def _analyse(self, source):
# Analyse

def output(self):
# _analyse(source)

########################################
# Tokenise
########################################
def read_next():
    '''
    Return the next character in file
    (Also increment file's current position by one)
    '''
    character = source.read(1)
    return character

def peek():
    '''
    Peek at the next character
    (Note that this does not affect file's current position)
    '''
    character = read_next()
    file.seek(-1, 1)
    return character

def tokenise():
    '''Tokenise a stream of tokens (or more accurately, terminals)'''
    # Check if dictionary is available
    if not tokens_dict:
        # instatantiate class lexer, then analyse

