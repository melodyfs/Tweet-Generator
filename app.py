from flask import Flask
from word_frequency import histogram_dict
import sample as s
import sample
import codecs


app = Flask(__name__)

with codecs.open('dorian.txt',encoding='utf-8', errors='ignore') as f:
    original_text = f.read()


@app.route('/')
def hello_world():
    his = histogram_dict(original_text)
    p = s.get_probability(his)
    s_ = s.sample(p, his)

    # print("W: %s" % s)
    return "W: %s" % s_

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
