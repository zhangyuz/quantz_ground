uwsgi --socket=0.0.0.0:5000 --protocol=http -w quantz_ground.wsgi:app
