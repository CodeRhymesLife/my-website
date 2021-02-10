from os import environ as env

from app import app

if __name__ == '__main__':
    PORT = int(env.get("HTTP_PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=PORT)