"""A beach-themed, multiple-choice quiz about safe surfing in Southland."""

import random
import tkinter as tk
from tkinter import ttk

TIME_LIMIT = 15
POINTS_PER_CORRECT = 10

QUESTION_BANK = {
    "BEGINNER": [
        ("What piece of equipment keeps a surfer attached to their board?", ["Leash", "Wetsuit", "Wax", "Fins"],
         "Leash", "A leash helps keep your board close after a fall."),
        ("What should you check before going surfing?", ["Wave and weather conditions", "The colour of your board", "Your phone battery", "The temperature of your car"],
           "Wave and weather conditions", "Conditions can change quickly, so check them before entering the water."),
        ("What is a wetsuit mainly used for?", ["Keeping a surfer warm", "Making waves bigger", "Making the board faster", "Protecting the surfboard"],
          "Keeping a surfer warm", "A wetsuit slows heat loss in Southland's cooler water."),
        ("Where is the safest place to surf when lifeguards are present?", ["Between the flags", "Where the waves are biggest", "Near rocks", "Far from everyone"],
          "Between the flags", "The flags mark the area that lifeguards are watching."),
        ("What should you do before paddling out?", ["Watch the waves and other surfers", "Rush straight into the lineup", "Leave your board on the sand", "Ignore the conditions"],
          "Watch the waves and other surfers", "A quick observation helps you choose a safer path through the waves."),
    ],
    
}