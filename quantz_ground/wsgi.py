# import sys
# import os

# sys.path.append(os.path.basename( os.path.abspath(__file__)))

from .app import app


if __name__ == '__main__':
    app.run()
