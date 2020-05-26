from flask import Flask, render_template, request, url_for, redirect
import socket
import os
import random
import string

app = Flask(__name__)
json = {} # {long_url: hash}

def random_string(length):
    """Generate an alphanumeric string that contains a random combination of letters and numbers."""
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for i in range(length))

def generate_hash(long_url=None): 
    """Generate a hash for the specified URL. Takes care of hash collisions."""
    global json
    generate = random_string(5)
    while generate in json.values(): # Checking for hash collisions
        generate = generate_hash(long_url)
    json[long_url] = generate
    return generate

def dehash(short_url): 
    """Dehashes the shortened hashes."""
    for i in json.keys(): 
        if json[i] == short_url: 
            return i

long_url=""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST": 
        global long_url
        long_url = request.form["longurl"]
        return render_template("test.html", final_hash=generate_hash(long_url), long_url=long_url, curr=request.host)
    return render_template("index.html")

# Basically useless
@app.route('/test', methods=['GET', 'POST'])
def test():
    return "Hello world"

@app.route('/<shortened>')
def user(shortened): 
    shorty=str([dehash(i) for i in json.values()][-1])
    return redirect("%s" %shorty) 
    # render_template("redirect.html", shorty=str([dehash(i) for i in json.values()][-1]))

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=port)
 