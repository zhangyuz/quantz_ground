QuantZ 的数据后端，提供数据只读功能。

## System Requirements
有一个能够运行的MongoDB

## Run
```bash
git clone git@github.com:zhangyuz/quantz_ground.git
cd quantz_ground/quantz_ground
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
使用浏览器打开 http://127.0.0.1:5000/us_wei_item ，就可以看见你的数据了
