from eve import Eve

from .db_domains import db_domains

SETTINGS = {
    'DOMAIN': db_domains,
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    # MONGO_USERNAME': os.environ.get(...),
    # MONGO_PASSWORD': os.environ.get(...),
    'MONGO_DBNAME': 'quantz',
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
    # 'ITEMS': 'items',
    # 'META': 'meta',
    # 'DATE_CREATED': 'created',
    # 'ID_FIELD': 'id',  # FIXME: not working, Y?
    # 'LAST_UPDATED': 'updated',
    # 'ETAG': 'etag',
    'PAGINATION_DEFAULT': 10000,
    'PAGINATION_LIMIT': 99999999,
    # 'OPTIMIZE_PAGINATION_FOR_SPEED': True,
}


def exclude_fields(resource, response):
    excluded_fields = ['_id', '_created', '_updated', '_etag']
    for doc in response['_items']:
        for field in excluded_fields:
            # Better ask forgiveness than permission
            try:
                del doc[field]
            except KeyError as e:
                pass


def on_fetched_resource(resource_name, response):
    print('on_fetched_resource:%s' % resource_name)
    exclude_fields(resource_name, response)


app = Eve(settings=SETTINGS)

app.on_fetched_resource += on_fetched_resource


@app.route('/mnt')
def mnt():
    return 'This is Maintanance Page'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
