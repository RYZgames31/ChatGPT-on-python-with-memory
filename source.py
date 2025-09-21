from g4f.client import Client
from pystyle import Colors, Box, Write, Center, Colorate, Anime
import os

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(Colorate.Horizontal(Colors.red_to_white, (r""" 
. __             __ 
_/  |___  _  __ |__|
\   __\ \/ \/ / |  |
 |  |  \     /  |  | made by tea with trojan
 |__|   \/\_/\__|  |teawithtrojan.404.mn/discord 
            \______|
    """).strip()))

client = Client()
while True:
    menu()
    message = input("message: ")
    menu()
    print("Loading...")
    response = client.chat.completions.create(
        model="gpt-4.1",  # Try "gpt-4o", "deepseek-v3", etc.
        messages=[{"role": "user", "content": message}],
        web_search=False
    )
    menu()
    print(response.choices[0].message.content)
    os.system("pause")
