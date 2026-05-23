# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:30:26 2026

@author: Nikita Patil
"""

print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")
    
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")
    
    elif user == "what is your name":
        print("Bot: I am a basic chatbot.")
    
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    
    else:
        print("Bot: Sorry, I don't understand.")