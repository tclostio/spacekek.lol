import os
import requests
from app import app
from datetime import datetime
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    chan_err = ""
    time = datetime.now()
    script_dir = os.path.dirname(__file__)
    rel_path = 'static/text/chans.txt'
    abs_file_path = os.path.join(script_dir, rel_path)
    try:
        r = requests.get('https://eldritchdata.neocities.org/IndexTXT/Misc/ChanList.txt')
        chan_list = r.text.splitlines()
        chan_list = chan_list[3:]
    except requests.exceptions.RequestException:
        chan_err = "[!!] Unable to grab chans... pulling from txt backup."
        with open(abs_file_path) as f:
            chan_list = f.readlines()
        chan_list = chan_list[3:]

    return render_template('index.html', title='HOME', cerr=chan_err, chans=chan_list, time=time)
    