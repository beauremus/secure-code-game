#!/usr/bin/env python3

"""Provide structure for Tax Payer with helper methods."""

import os
from pathlib import Path

from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    """Standard test inputs."""
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

def valid_path(path):
    """Defends against path traversal attacks."""
    root_dir = Path('.')
    try:
        Path(root_dir).joinpath(path).resolve().relative_to(root_dir.resolve())
        return True
    except ValueError:
        return False

class TaxPayer:
    """Structure for Tax Payer with helper methods."""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    def get_prof_picture(self, path=None):
        """Return the path of an optional profile picture that users can set"""
        # setting a profile picture is optional
        if not path:
            pass

        if not valid_path(path):
            return None

        # builds path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        prof_picture_path = os.path.normpath(os.path.join(base_dir, path))

        # assume that image is returned on screen after this
        return prof_picture_path

    def get_tax_form_attachment(self, path=None):
        """Return the path of an attached tax form that every user should submit"""
        if path is None:
            raise ValueError("Error: Tax form is required for all users")

        if not valid_path(path):
            return None

        with open(path, 'rb') as form:
            self.tax_form_attachment = bytearray(form.read())

        # assume that tax data is returned on screen after this
        return path
