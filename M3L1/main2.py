import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Merhaba hos geldiniz asagıdaki linke tıklayarak teknoloji ile rastgele bir bilgi öğrene bilir misin!</h1>'
#    return <a href="/rastgele_gercek">!</a>

