import os
from typing import Optional, Any, Union, Iterator, Generator

from flask import Flask, jsonify, abort, request, Response

from utils import commands

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    data: Optional[Any] = request.json
    if not data:
        abort(404, 'No data')
    cmd1: str = data.get('cmd1')
    value1: str = data.get('value1')
    cmd2: str = data.get('cmd2')
    value2: str = data.get('value2')
    file_name: str = data.get('file_name')
    file_path: str = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(404, 'No such file')
    with open(file_path, 'r', encoding='utf-8') as file:
        result: Union[str, Iterator, Generator] = commands(cmd=cmd1, value=value1, data=file)
        answer: Union[str, Iterator, Generator] = commands(cmd=cmd2, value=value2, data=result)
    return jsonify(list(answer))

