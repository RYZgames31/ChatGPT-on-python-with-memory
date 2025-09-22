from g4f.client import Client
from pystyle import Colors, Box, Write, Center, Colorate, Anime
import os

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(Colorate.Horizontal(Colors.red_to_white, (r""" 
. __             __ 
_/  |___  _  __ |__| made by tea with trojan
\   __\ \/ \/ / |  | teawithtrojan.404.mn/discord
 |  |  \     /  |  | fork made by RYZgames31
 |__|   \/\_/\__|  | github.com/RYZgames31
            \______|
    """).strip()))

client = Client()
messages_list = []
while True:
    menu()
    message = input("message: ")
    messages_list.append({"role": "user", "content": message})
    menu()
    print("Loading...")
    response = client.chat.completions.create(
        model="gpt-4.1",  # Try "gpt-4o", "deepseek-v3", etc.
        messages=messages_list,
        web_search=False
    )
    menu()
    messages_list.append({"role": "assistant", "content": response.choices[0].message.content})
    print(response.choices[0].message.content)
    os.system("pause")
