import numpy as np
import json
from flask import Flask, request, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

import searching

@app.route('/test', methods=['POST'])
def test():
    lists = request.args['file_name']
    checked = request.args['file_checked']

    print("node.js로부터 받아온 정보 >> ", lists, "?", checked)

    searching_result = searching.backtracking(lists, checked)
    #exec(open('ex.py', 'rt', encoding='UTF8').read())
    print(searching_result)

    return jsonify({
       'result': searching_result
    })




if __name__ == '__main__':
    app.run()