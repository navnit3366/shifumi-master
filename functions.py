#!/usr/bin/python3.7
# coding: utf8

import random #import random for computer choice

# choices list for the game
choices = ["PIERRE", "FEUILLE", "CISEAUX"]

def playerName():
    """function for ask player name"""
    name = input("votre nom")
    while controlName(name) is False:
        print("votre nom doit contenir au minimum 2 caractere et maxi 15")
        name = input("votre nom")
    return name

def controlName(name):
    """function control name"""
    try:
        assert len(name) > 1 and len(name) < 15
    except AssertionError as a:
        return False

def user1Choice():
    """function for user1 choice"""
    print("Que choisissez-vous PIERRE, FEUILLE ou CISEAUX ?")
    choice = input("choix : ").upper()
    while controlChoice(choice) is False:
        print("Que choisissez-vous entre PIERRE, FEUILLE ou CISEAUX !")
        choice = input("choix : ").upper()
    return choice

def controlChoice(choice):
    """function for control choice"""
    try:
        assert choice in choices
    except AssertionError as a:
        return False

def computerChoices():
    """function for random computer choices"""
    return choices[random.randint(0,len(choices)-1)]

def calculateScore(score, playerChoice, computerChoice):
    """function for add point """
    if playerChoice != computerChoice:
        if playerChoice == "PIERRE" and computerChoice == "CISEAUX"\
        or playerChoice == "FEUILLE" and computerChoice == "PIERRE"\
        or playerChoice == "CISEAUX" and computerChoice == "FEUILLE":
            score["player"] += 1
        else:
            score["computer"] += 1
    return score







