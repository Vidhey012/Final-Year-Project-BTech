import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Bot import ChatBot as bot

ob = bot.ChatBot.getBot()

i = 0
print("Print exit to leave")
while True:
    text = input("Q : ")
    if text == 'exit':
        break
    print("A : "+ob.response(text))

print("Ended successfully")
