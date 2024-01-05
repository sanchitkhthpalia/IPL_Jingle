import time
import winsound  # For Windows systems

# Define the notes and their durations
notes = ["C", "D", "E", "F", "G", "A", "B"]
durations = [500, 500, 500, 500, 500, 500, 500]

# Function to play a note
def play_note(note, duration):
    winsound.Beep(int(get_frequency(note)), duration)

# Function to get the frequency of a note
def get_frequency(note):
    note_freqs = {"C": 261.63, "D": 293.66, "E": 329.63, "F": 349.23, "G": 392.00, "A": 440.00, "B": 493.88}
    return note_freqs[note]

# Play the jingle
def play_jingle():
    for i in range(len(notes)):
        play_note(notes[i], durations[i])
        time.sleep(0.1)  # Add a short pause between notes

# Call the function to play the jingle
play_jingle()
