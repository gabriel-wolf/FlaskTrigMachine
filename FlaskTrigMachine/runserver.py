import os
from GabeFlask import app 

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    import random, threading, webbrowser
    threading.Timer(1.25, lambda: webbrowser.open('http://localhost:5555/form-example') ).start()
    app.run(host=HOST, port=5555)

   
    
