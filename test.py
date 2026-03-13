import keyboard

def on_key_press(event):
    """Callback function executed when a key is pressed."""
    print(f"Key '{event.name}' was pressed.")

# Register the callback function to be called on any key press
keyboard.on_press(on_key_press)

# Keep the program running to listen for key presses
# You can add a condition to exit, e.g., pressing 'esc'
try:
    keyboard.wait('esc')  # Wait until 'esc' key is pressed to exit
except KeyboardInterrupt:
    print("Program terminated by user.")