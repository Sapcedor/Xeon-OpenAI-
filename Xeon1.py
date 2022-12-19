import tkinter as tk
import subprocess

def install_openai():
  subprocess.run(["pip", "install", "openai"])

# Try to import openai
try:
  import openai
except ModuleNotFoundError:
  # If openai is not installed, install it
  install_openai()
  import openai

openai.api_key = "YOU-API-KEY-HERE"

def chat(prompt):
 # Display the "Processing" label
  processing_label.pack()
  root.update()

  completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0,
  )

  message = completions.choices[0].text

  # Hide the "Processing" label
  processing_label.pack_forget()
  root.update()

  return message

# Create a function to handle the user's input
def handle_user_input(event=None):
 # Get the user's input
  user_input = user_input_entry.get()
  if user_input == "exit":
    root.destroy()

  # Clear the user's input field
  user_input_entry.delete(0, tk.END)

  # Get the chatbot response
  response = chat(user_input)

  # Display the chatbot's response
  display_text.config(state=tk.NORMAL)
  display_text.insert(tk.END, f"\nUser: {user_input}\n", 'white')
  display_text.insert(tk.END, f"\nComputer: {response}\n", 'yellow')
  display_text.see(tk.END)  # Scroll down to the end of the text
  display_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Xeon")
root.configure(bg='blue')

# Create the "Processing" label
processing_label = tk.Label(root, text="Processing...", bg='blue', fg='white', font=("Courier New", 16))

# Create the frame for the chat display
display_frame = tk.Frame(root, bg='blue', bd=2, highlightbackground='white', highlightthickness=1)
display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=(0, 4))

# Create the scrollbar
scrollbar = tk.Scrollbar(display_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the chat display text box
display_text = tk.Text(display_frame, bg='blue', fg='white', font=("Courier New", 16), state=tk.DISABLED, yscrollcommand=scrollbar.set)
display_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
display_text.tag_configure('white', foreground='white')
display_text.tag_configure('yellow', foreground='yellow')

# Associate the scrollbar with the chat display text box
scrollbar.config(command=display_text.yview)

# Create the frame for the user input field
user_input_frame = tk.Frame(root, bg='blue', bd=2, highlightbackground='white', highlightthickness=1)
user_input_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create the user input field
user_input_entry = tk.Entry(user_input_frame, bg='blue', fg='white', font=("Courier New", 16))
user_input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
user_input_entry.bind("<Return>", handle_user_input)

# Create the submit button
submit_button = tk.Button(user_input_frame, text="Submit", bg='blue', fg='white', font=("Courier New", 16), command=handle_user_input)
submit_button.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()
