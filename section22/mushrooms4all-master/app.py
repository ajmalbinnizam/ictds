import pickle
import random
from pprint import pprint

import pandas as pd
from flask import Flask, render_template, jsonify, make_response, request, abort

app = Flask(__name__)
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

# load the model from disk
filenameEnc = 'model/encoder.sav'
attrEnc = pickle.load(open(filenameEnc, 'rb'))
filenameYEnc = 'model/Yencoder.sav'
yEnc = pickle.load(open(filenameYEnc, 'rb'))
filename = 'model/GBC.sav'
loaded_model = pickle.load(open(filename, 'rb'))


def trasform(x):
    x = x.map(lambda i: i if i in attrEnc[x.name].classes_ else random.choice(attrEnc[x.name].classes_))
    return attrEnc[x.name].transform(x)


def encode(json):
    pprint(json)
    df = pd.DataFrame(json, index=[0])
    # Using the dictionary to label future data
    return df.apply(trasform)


def predict(X):
    print(X.shape)
    y_pred = loaded_model.predict(X)
    return yEnc.inverse_transform(y_pred)


@app.route('/')
def landingPage():
    inp = {
        "cap-shape": {"bell": "b", "conical": "c", "convex": "x", "flat": "f", "knobbed": "k", "sunken": "s"},
        "cap-surface": {"fibrous": "f", "grooves": "g", "scaly": "y", "smooth": "s"},
        "cap-color": {"brown": "n", "buff": "b", "cinnamon": "c", "gray": "g", "green": "r", "pink": "p", "purple": "u",
                      "red": "e", "white": "w", "yellow": "y"},
        "bruises": {"yes": "t", "no": "f"},
        "odor": {"almond": "a", "anise": "l", "creosote": "c", "fishy": "y", "foul": "f", "musty": "m", "none": "n",
                 "pungent": "p", "spicy": "s"},
        "gill-attachment": {"attached": "a", "descending": "d", "free": "f", "notched": "n"},
        "gill-spacing": {"close": "c", "crowded": "w", "distant": "d"},
        "gill-size": {"broad": "b", "narrow": "n"},
        "gill-color": {"black": "k", "brown": "n", "buff": "b", "chocolate": "h", "gray": "g", " green": "r",
                       "orange": "o",
                       "pink": "p", "purple": "u", "red": "e", "white": "w", "yellow": "y"},
        "stalk-shape": {"enlarging": "e", "tapering": "t"},
        "stalk-root": {"bulbous": "b", "club": "c", "cup": "u", "equal": "e", "rhizomorphs": "z", "rooted": "r",
                       "missing": "?"},
        "stalk-surface-above-ring": {"fibrous": "f", "scaly": "y", "silky": "k", "smooth": "s"},
        "stalk-surface-below-ring": {"fibrous": "f", "scaly": "y", "silky": "k", "smooth": "s"},
        "stalk-color-above-ring": {"brown": "n", "buff": "b", "cinnamon": "c", "gray": "g", "orange": "o", "pink": "p",
                                   "red": "e", "white": "w", "yellow": "y"},
        "stalk-color-below-ring": {"brown": "n", "buff": "b", "cinnamon": "c", "gray": "g", "orange": "o", "pink": "p",
                                   "red": "e", "white": "w", "yellow": "y"},
        "veil-type": {"partial": "p", "universal": "u"},
        "veil-color": {"brown": "n", "orange": "o", "white": "w", "yellow": "y"},
        "ring-number": {"none": "n", "one": "o", "two": "t"},
        "ring-type": {"cobwebby": "c", "evanescent": "e", "flaring": "f", "large": "l", "none": "n", "pendant": "p",
                      "sheathing": "s", "zone": "z"},
        "spore-print-color": {"black": "k", "brown": "n", "buff": "b", "chocolate": "h", "green": "r", "orange": "o",
                              "purple": "u", "white": "w", "yellow": "y"},
        "population": {"abundant": "a", "clustered": "c", "numerous": "n", "scattered": "s", "several": "v",
                       "solitary": "y"},
        "habitat": {"grasses": "g", "leaves": "l", "meadows": "m", "paths": "p", "urban": "u", "waste": "w",
                    "woods": "d"}
    }
    return render_template("index.html", inputs=inp)


@app.route('/mush/api/predict', methods=['POST'])
def APIpredict():
    if not request.json:
        abort(400)
    X = encode(request.json)
    res = predict(X)
    return jsonify(res.tolist())


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
