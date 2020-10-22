from eve import Eve

SETTINGS = {
    'DOMAIN': {'us_wei_item': {}},
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    # MONGO_USERNAME': os.environ.get(...),
    # MONGO_PASSWORD': os.environ.get(...),
    'MONGO_DBNAME': 'quant_test',
    'RENDERERS': [
        'eve.render.JSONRenderer'
        # 'eve.render.XMLRenderer'
    ],
    'ALLOW_UNKNOWN': True,
    'X_DOMAINS_RE': r'.*',
    'IF_MATCH': False,
    'ENFORCE_IF_MATCH': False,
    'HATEOAS': False,
    # 修改数据域名称,从 _items 改为 items，避免前端语法检查严格不能使用_开头的变量
    'ITEMS': 'items',
    'META': 'meta',
    'DATE_CREATED': 'created',
    'ID_FIELD': 'id',  # FIXME: not working, Y?
    'LAST_UPDATED': 'updated',
    'ETAG': 'etag',
}


def on_fetched_resource(resource_name, response):
    print('reousrce_name:%s' % resource_name)
    print('response %s' % type(response))
    # del(response['_links'])
    # del(response['_meta'])


app = Eve(settings=SETTINGS)

app.on_fetched_resource += on_fetched_resource


if __name__ == '__main__':
    app.run(host='0.0.0.0')
