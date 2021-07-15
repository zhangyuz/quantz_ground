#!/bin/bash
conda activate quant
cd quantz_ground
export FLASK_APP=app.py
export FLASK_ENV=developmen
flask run
# open http://127.0.0.1:5000/us_wei_item
