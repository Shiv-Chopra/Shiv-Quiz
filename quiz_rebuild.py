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
    "INTERMEDIATE": [
        ("Which factor can affect wave quality at a surf break?", ["Wind direction and swell", "The colour of the surfboard", "The surfer's shoes", "The time shown on a phone"],
          "Wind direction and swell", "Swell and wind strongly affect wave size, shape and cleanliness."),
        ("Why is it important to avoid dropping in on another surfer?", ["It can cause a collision and breaks surf etiquette", "It makes the board heavier", "It stops the tide", "It changes the weather"],
          "It can cause a collision and breaks surf etiquette", "The surfer closest to the breaking part of the wave has priority."),
        ("What is a surf break?", ["A place where waves break and can be surfed", "A type of wetsuit", "A competition prize", "A piece of surfboard equipment"],
          "A place where waves break and can be surfed", "A surf break is a location where waves form in a surfable way."),
        ("Which action shows good surf etiquette?", ["Waiting your turn for a wave", "Taking every wave from others", "Paddling into another surfer", "Ignoring surfers with priority"],
          "Waiting your turn for a wave", "Taking turns makes the lineup safer and fairer."),
        ("What should you do if caught in a rip current?", ["Stay calm and signal for help", "Fight it by swimming straight in", "Dive under it", "Take off your leash"],
          "Stay calm and signal for help", "Stay calm, float, and raise an arm to signal for help."),
    ],

    "ADVANCED": [
        ("What does 'swell' refer to in surfing?", ["A series of waves travelling across the ocean", "The colour of the ocean", "The length of a surfboard", "The temperature of the sand"],
          "A series of waves travelling across the ocean", "Swell is organised wave energy travelling through the ocean."),
        ("Why can wind direction be important to surfers?", ["It can change the shape and quality of waves", "It determines surfboard colour", "It changes a surfer's height", "It controls wetsuit cost"],
          "It can change the shape and quality of waves", "Offshore winds can make waves cleaner; onshore winds often make surf choppy."),
        ("Which behaviour is most responsible in a crowded lineup?", ["Observe and wait for a safe opportunity", "Paddle straight through everyone", "Take every available wave", "Ignore other surfers"],
          "Observe and wait for a safe opportunity", "Watch the pattern first so you do not interfere with surfers riding waves."),
         ("Why understand local conditions at an unfamiliar break?", ["Different breaks have different hazards and wave behaviour", "All surf breaks are exactly the same", "It guarantees perfect waves", "It removes the need for safety equipment"],
           "Different breaks have different hazards and wave behaviour", "Local conditions may include rips, rocks, currents and changing weather."),
        ("Why is learning Southland surfing history useful?", ["It builds understanding of local surf culture", "It changes the tides", "It makes waves larger", "It replaces safety knowledge"], "It builds understanding of local surf culture", "History gives context about the people and places that shape a surfing community."),
    ],
}

class SurfQuiz:
    """Application controller for the quiz screens and timer."""

NAVY, DEEP_BLUE, OCEAN = "#073B4C", "#055A7A", "#0B9CB5"
FOAM, CORAL, INK = "#F4FBFA", "#E9674A", "#12343B"

def __init__(self, root):
    self.root = root
    root.title("Southland Surfing Quiz")
    root.geometry("900x680")
    root.minsize(760, 600)
    root.configure(bg=self.NAVY)
    self.level = ""
    self.questions = []
    self.index = self.score = 0
    self.time_left = TIME_LIMIT
    self.timer_id = None
    self.answered = False
    self.selected_answer = None
    self.choice_buttons = []
    self.setup_styles()
    self.show_welcome()

def setup_styles(self):
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Page.TFrame", background=self.FOAM)
    style.configure("Card.TFrame", background="white")
    style.configure("Title.TLabel", background=self.FOAM, foreground=self.NAVY, font=("Segoe UI", 28, "bold"))
    style.configure("Sub.TLabel", background=self.FOAM, foreground="#39717D", font=("Segoe UI", 11))
    style.configure("Question.TLabel", background="white", foreground=self.INK, font=("Segoe UI", 18, "bold"))
    style.configure("Body.TLabel", background="white", foreground="#41636B", font=("Segoe UI", 11))
    style.configure("Level.TButton", font=("Segoe UI", 13, "bold"), padding=(22, 13), foreground="white", background=self.DEEP_BLUE, borderwidth=0)
    style.map("Level.TButton", background=[("active", self.OCEAN)])
    style.configure("Answer.TButton", font=("Segoe UI", 12), padding=(16, 14), foreground=self.INK, background="#EDF7F6", borderwidth=0)
    style.map("Answer.TButton", background=[("active", "#D6F0EC")])
    style.configure("Selected.Answer.TButton", font=("Segoe UI", 12, "bold"), padding=(16, 14), foreground="white", background=self.OCEAN, borderwidth=0)
    style.configure("Next.TButton", font=("Segoe UI", 12, "bold"), padding=(20, 11), foreground="white", background=self.DEEP_BLUE, borderwidth=0)
    style.map("Next.TButton", background=[("active", self.OCEAN)])
    style.configure("Correct.Answer.TButton", font=("Segoe UI", 12, "bold"), padding=(16, 14), foreground="white", background="#2A9D8F", borderwidth=0)
    style.configure("Wrong.Answer.TButton", font=("Segoe UI", 12), padding=(16, 14), foreground="white", background=self.CORAL, borderwidth=0)

def cancel_timer(self):
    if self.timer_id is not None:
        self.root.after_cancel(self.timer_id)
        self.timer_id = None

def clear(self):
    self.cancel_timer()
    for widget in self.root.winfo_children():
        widget.destroy()

def page(self):
    page = ttk.Frame(self.root, style="Page.TFrame", padding=(52, 32))
    page.pack(fill="both", expand=True)
    return page

def brand(self, parent):
     tk.Label(parent, text="SOUTHLAND  /  AOTEAROA", bg=self.FOAM, fg=self.OCEAN, font=("Segoe UI", 10, "bold")).pack(anchor="w")
     tk.Label(parent, text="SURF SMART", bg=self.FOAM, fg=self.NAVY, font=("Segoe UI", 28, "bold")).pack(anchor="w", pady=(2, 0))

