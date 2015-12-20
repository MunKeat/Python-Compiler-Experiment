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

# Keep track of line number in case of error diagnosis
line_number = 1
# File which contains source code
# TODO: Ensures that script accept parameter
source = open("file.txt", "br+")
# File which contains definition for tokens
# TODO: Set up a minimal version of Definition.txt, for HereDoc, to allow lex.py to be independent
definition_text = "SampleDefinition.txt"
# Dictionary containing tokens
token_dict = {}

########################################
# Definition
########################################
def define(debug=False):
    file = open(definition_text)
    for line in file:
        # Strip trailing newline characters
        line = line.rstrip("\n")
        # Split using regular expression at '::='
        tokenDef = re.split("\s*::=\s*", line, maxsplit=1)
        tokenItem = tokenDef[0]
        # Split using regular expression at '|'
        tokenRules = re.split("\s+\|\s+", tokenDef[1])
        # Generate dictionary of rules for language
        for rule in tokenRules:
            # The following assumption will hold:
            # separator, whitepace & newline are 1 character
            token_dict[str(rule)] = tokenItem
    if debug:
        for key, value in token_dict.items():
            print("{} : {}".format(key, value))

def is_whitespace(character):
    if character in token_dict:
        return token_dict[character] == "spaceToken"
    else:
        return False

def is_separator(character):
    if character in token_dict:
        return token_dict[character] == "separatorToken"
    else:
        return False

def is_newline(character):
    if character in token_dict:
        return token_dict[character] == "newlineToken"
    else:
        return False

def is_num(character):
    return str(character).isdigit()

def is_alpha(character):
    return str(character).isalpha()

def is_alnum(character):
    return str(character).isalpha() or str(character).isdigit()

########################################
# Tokenise
########################################
def read_next():
    '''
    Return the next character in file
    (Also increment file's current position by one)
    '''
    character = source.read(1)
    return character.decode("ascii")

def peek():
    '''
    Peek at the next character
    (Note that this does not affect file's current position)
    '''
    character = read_next()
    source.seek(-1, 1)
    return character

def tokenise(skip_whitespace=True):
    '''Tokenise a stream of tokens (or more accurately, terminals)'''
    # Check if dictionary is available
    if not token_dict:
        define()
    char = read_next()
    token = []
    # Case: Alphabet
    if is_alpha(char):
        token.append(char)
        while True:
            temp = peek()
            if not is_alnum(temp):
                token = "".join(token)
                return (token, "string")
            else:
                token.append(read_next())
    # Case : Numbers
    elif is_num(char):
        token.append(char)
        while True:
            temp = peek()
            if not is_num(temp):
                token = "".join(token)
                return (token, "number")
            else:
                token.append(read_next())
    # Case: Whitespace
    elif is_whitespace(char):
        if skip_whitespace:
            return
        else:
            return (char, token_dict[char])
    # Case: Separator
    elif is_separator(char):
        return (char, token_dict[char])
    # Case: Newline
    elif is_newline(char):
        line_number += 1
        return (char, token_dict[char])
    # Case: Default
    else:
        if char in token_dict:
            return (char, token_dict[char])
        else:
            return (char, "UNKNOWN")

# For debugging
def analyse(output=False):
    # List of tokens and corresponding type
    source_tokenised = []
    while peek():
        source_tokenised.append(tokenise())
    if output:
        for source_token in source_tokenised:
            print(source_token)
    return source_tokenised

define()
analyse()
