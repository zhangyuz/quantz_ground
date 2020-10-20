from eve import Eve

SETTINGS = {
    'DOMAIN': {'us_wei_item': {}},
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    # MONGO_USERNAME': os.environ.get(...),
    # MONGO_PASSWORD': os.environ.get(...),
    'MONGO_DBNAME': 'quant_test',
    'RENDERERS' : [
        'eve.render.JSONRenderer'
        # 'eve.render.XMLRenderer'
    ],
    'ALLOW_UNKNOWN': True
}

app = Eve(settings=SETTINGS)

if __name__ == '__main__':
    app.run(host='0.0.0.0')