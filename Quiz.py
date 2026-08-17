# -------------------------------------------
# Southland Surfing Quiz
# By: Shiv
# -------------------------------------------

# This program is a multiple-choice surfing quiz
# about surfing in Southland.
#
# Players answer questions about:
# - Surfing equipment
# - Beach safety
# - Southland surf breaks
# - Surf etiquette
# - Wave conditions
# - Surfing terminology
#
# Players receive 10 points for each correct answer.

import tkinter as tk
from tkinter import messagebox

# ------------------------------------------
# Quiz Questions
# ------------------------------------------

# this list has all of the questions that will be used in the quiz.
# each question has:
# level - the difficulty of the question
# question - the question that the player will see
# answers - four possible answers
# correct - the correct answer


questions = [

    # LEVEL 1 - BEGINNER
    {
        "level": "BEGINNER",
        "question": "What piece of equipment keeps a surfer attached to their board?",
        "answers": [
            "Leash",
            "Wetsuit",
            "Wax",
            "Fins"
        ],
        "correct": "Leash"
    },

    {
        "level": "BEGINNER",
        "question": "What should you check before going surfing?",
        "answers": [
            "Wave and weather conditions",
            "The colour of your board",
            "Your phone battery",
            "The temperature of your car"
        ],
        "correct": "Wave and weather conditions"
    }, 

     {
        "level": "BEGINNER",
        "question": "What is a wetsuit mainly used for?",
        "answers": [
            "Keeping a surfer warm",
            "Making waves bigger",
            "Making the board faster",
            "Protecting the surfboard"
        ],
        "correct": "Keeping a surfer warm"
    },

     
