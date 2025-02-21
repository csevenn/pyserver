from flask import Flask, render_template
import json
import webbrowser
import os

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""


                                           
  _ __  _   _ ___  ___ _ ____   _____ _ __ 
 | '_ \| | | / __|/ _ \ '__\ \ / / _ \ '__|
 | |_) | |_| \__ \  __/ |   \ V /  __/ |   
 | .__/ \__, |___/\___|_|    \_/ \___|_|   
 |_|    |___/                              

            [ made by c7 ]
          
          
          
          """)


with open('../config.json', 'r') as f:
    config = json.load(f)

PORT = config.get("port", 8000)

app = Flask(__name__, static_folder='../website', template_folder='../website')

@app.route('/')
def home():
    return render_template('index.html')

webbrowser.open(f'http://localhost:{PORT}')

if __name__ == '__main__':
    banner()
    app.run(host='localhost', port=PORT)
