from flask import Flask, request, jsonify
import spacy
from spacy import lang
# you need spaCy version >= 2.2.2
from spacy.lang.lb import Luxembourgish

from tabulate import tabulate

app = Flask(__name__)
# Create the nlp object
nlp = Luxembourgish()
nlp = spacy.load("./lux-tagger-July2023/model-best/")

@app.route('/pos_tag', methods=['POST'])
def pos_tag():
    text = request.json['text']
    doc = nlp(text)
    headers = ["Text", "Tag", "Stopword", "Shape", "Alpha"]
    rows = []
    for token in doc:
        rows.append([token.text, token.tag_, token.is_stop, token.shape_, token.is_alpha])
    return tabulate(rows, headers=headers, tablefmt='html')

if __name__ == '__main__':
    app.run(debug=True)