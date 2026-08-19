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
    
        "Intermediate": [
            { 
                "text": "Which factor can affect the quality of waves at a surf break?",
                "options": [
                    "Wind direction and swell",
                    "The colour of the surfboard",
                    "The surfer's shoes",
                    "The time shown on a phone"
                ],
                "answer": "Wind direction and swell",
                "explanation": "Swell and wind conditions can strongly affect wave shape and quality."
            },
            {
                "text": "Why is it important to avoid dropping in on another surfer?",
                "options": [
                      "It can cause a collision and breaks surf etiquette",
                      "It makes the board heavier",
                      "It stops the tide",
                      "It changes the weather"
                ],
                "answer": "It can cause a collision and breaks surf etiquette",
                "explanation": "Dropping in means taking a wave when another surfer has priority and can create a dangerous situation."
            },
            {
                "text": "What is a surf break?",
                "options": [
                    "A place where waves break and can be surfed",
                    "A type of wetsuit",
                     "A surfing competition prize",
                     "A piece of surfboard equipment"
                ],
                "answer": "A place where waves break and can be surfed",
                "explanation": "A surf break is a location where waves break in a way that can allow surfing."
            }
            {
                "text": "Why might a surfer wear a wetsuit in Southland?",
                "options": [
                    "To help keep warm in cooler water",
                    "To make the waves bigger",
                    "To improve the tide",
                    "To make the surfboard faster"
                ],
                "answer": "To help keep warm in cooler water",
                "explanation": "A wetsuit helps reduce heat loss when surfing in colder water."
            },
            {
                "text": "Which action shows good surf etiquette?",
                "options": [
                    "Waiting your turn for a wave",
                    "Taking every wave from others",
                    "Paddling directly into another surfer",
                    "Ignoring surfers with priority"
                ],
                            "answer": "Waiting your turn for a wave",
                "explanation": "Taking turns and respecting priority helps keep the lineup safer and fairer."
            }
        ],
    
        "Advanced": [
             {
                "text": "Why is learning about the history of surfing in Southland useful?",
                "options": [
                    "It helps users understand the local surfing culture and its development",
                    "It changes the tides",
                    "It makes waves larger",
                    "It replaces the need for surf safety"
                ],
                  "answer": "It helps users understand the local surfing culture and its development",
                "explanation": "Learning local surfing history gives users more context about the sport and surfing community in Southland."
            },
            {
                  "text": "What does 'swell' refer to in surfing?",
                "options": [
                    "A series of waves travelling across the ocean",
                    "The colour of the ocean",
                    "The length of a surfboard",
                    "The temperature of the sand"
                ],
                "answer": "A series of waves travelling across the ocean",
                "explanation": "Swell is organised wave energy travelling through the ocean."
            },
              {
                "text": "Why can wind direction be important to surfers?",
                "options": [
                    "It can change the shape and quality of waves",
                    "It determines the colour of the surfboard",
                    "It changes a surfer's height",
                    "It controls how much a wetsuit costs"
                ],
                "answer": "It can change the shape and quality of waves",
                "explanation": "Wind can make waves cleaner or more choppy depending on its direction and strength."
            }
             {
                "text": "Which behaviour is most responsible when entering a crowded lineup?",
                "options": [
                    "Observe the lineup and wait for a safe opportunity",
                    "Paddle straight through everyone",
                    "Take every available wave",
                    "Ignore other surfers"
                ],
                "answer": "Observe the lineup and wait for a safe opportunity",
                "explanation": "Watching the lineup helps you understand wave patterns, priority and where other surfers are positioned."
            },
            {
                "text": "Why should surfers understand local conditions before surfing in an unfamiliar break?",
                "options": [
                    "Different breaks can have different hazards and wave behaviour",
                "All surf breaks are exactly the same",
                "it guarantees perfect waves",
                "It removes the need for safety equipment"
                ],
                "answer": "Different breaks can have different hazards and wave behaviour",
                "explanation": "Local knowledge can help surfers recognise hazards, conditions and appropriate places to surf."
            }
        ]
   
]

   


