#!/bin/usr/env python 3
'''
Name:
    lex.py
Summary:
    Lexical Analyzer of Compiler (Rough Draft)
    Source Code: C (A simplified version)
    Note that token definition are decoupled from module.
'''
# Import regular expression module to parse definition file
import re
import sys

# Keep track of line number in case of error diagnosis
line_number = 1
# File which contains source code
source = None
# File which contains definition for tokens
definition_text = "definition.txt"
# Dictionary containing tokens
token_dict = {}

########################################
# DEFINITION
########################################
def define(debug=False):
    file = open(definition_text, "r")
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
            # Remove any ' ', or pairing quotation marks
            if(rule.startswith("'") and rule.endswith("'") and rule != "'"):
               rule = rule.replace("'", "")
            # Convert any escape characters to their actual counterpart
            rule = bytes(rule, "utf-8").decode("unicode-escape")
            token_dict[rule] = tokenItem
    if debug:
        print("")
        for key, value in token_dict.items():
            print("{: <10} : {: <10}".format(key, value))
        print("")

########################################
# IDENTITY
########################################
def is_num(characters):
    return str(characters).isdigit()

def is_alpha(characters):
    return str(characters).isalpha()

def is_alnum(characters):
    return str(characters).isalnum()

def is_reserved(characters):
    if character in token_dict:
        return token_dict[character] == "reservedToken"
    else:
        return False

def is_assign(characters):
    if character in token_dict:
        return token_dict[character] == "assignToken"
    else:
        return False

def is_operator(characters):
    if character in token_dict:
        return token_dict[character] == "operatorToken"
    else:
        return False

def is_comparator(characters):
    if character in token_dict:
        return token_dict[character] == "comparisonToken"
    else:
        return False

def is_logical_token(characters):
    if character in token_dict:
        return token_dict[character] == "logicToken"
    else:
        return False

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

########################################
# TOKENISE
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
    '''Tokenise a stream of input'''
    global line_number
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

def analyse(output=False):
    # List of tokens and corresponding type
    source_tokenised = []
    while peek():
        token = tokenise();
        if token is None:
            continue
        source_tokenised.append(token)
    if output:
        for source_token in source_tokenised:
            print(source_token)
    return source_tokenised

def main():
    global source
    # Ensure file to be analysed exist
    source = open(sys.argv[1], "br+")
    define(True)
    analyse(True)

if __name__ == "__main__":
  main()
