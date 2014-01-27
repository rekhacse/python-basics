import os
os.system('color r') #green text
print ('I like green')

def main():
    # Asks which command you want to run.
    word = input("Which command? ").strip().lower()

    # Runs the command/s.

    if word == "info":
        print("Info command.")

    elif word == "replace":
        print("Replace command.")

    elif word == "ping":
        print("Ping command")

    elif word == "quit":
        return False

    else:
        print("Command not found")
    return True

while main():
    pass

    

