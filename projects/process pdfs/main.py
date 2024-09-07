from flask import Flask
from genai_gemini_app import root_blueprint
from test import test_blueprint
from parallel import parallel_blueprint
import signal, datetime, sys

app = Flask(__name__)
app.register_blueprint (root_blueprint, url_prefix="/")
app.register_blueprint (test_blueprint, url_prefix="/test")
app.register_blueprint (parallel_blueprint, url_prefix="/parallel")


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    # Perform any cleanup or graceful shutdown tasks here
    # ...
    exit(0)  # Exit the application

signal.signal(signal.SIGINT, signal_handler)






if __name__ == '__main__':
    '''
    You need to reorganize content in these markdown files. Goals: 1) most important: information should not be lost; preserve all details; 2) some heading names are wrong. They don't reflect content. Fix them; 3) make it more readable by using adding heading levels, rewriting, adding content/explanation, etc. as deemed necessary; 4) remove garbage text like copyright notices. Replace them if needed;


    You need to reorganize content in these markdown files. Goals: 1) most important: information should not be lost; preserve all details; 2) some heading names are wrong. They don't reflect content. Fix them; 3) remove garbage text like copyright notices. Replace them if needed; 4) Mild effect: make it more readable by using adding heading levels, rewriting, adding content/explanation, etc. as deemed necessary. Avoid excessive bullet points or excessively small paragraphs. Limit doing this;  5) Elaborate and add content where deemed necessary;
    '''

    app.run(debug=True)
    # socketio.run(app, debug=True)