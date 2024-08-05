# ALEXIS
This project involves creating a basic voice-controlled assistant named "Alexis" using Python. The assistant can listen to voice commands, respond with spoken words, and perform simple tasks such as telling the time, searching the web, and finding locations on a map.

Features:

Speech Recognition:

Utilizes the speech_recognition library to capture audio input from the user and convert it into text using Google's speech recognition API.
Text-to-Speech Conversion:

Employs the gTTS (Google Text-to-Speech) library to convert text responses into spoken words. The audio is then played using the pygame library.

Basic Commands:

Personal Information: Responds to questions like "What is your name?" and "How are you?" with predefined answers.

Time Inquiry: Tells the current time when asked.

Web Search: Allows the user to perform a Google search through voice commands, opening the search results in the default web browser.

Location Search: Opens Google Maps to display a specific location based on user input.

Exit: Ends the program when the user says "exit".

User Interaction:

The assistant starts by greeting the user and continues to listen for commands in an infinite loop until the user decides to exit.
