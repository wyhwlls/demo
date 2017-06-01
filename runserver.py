from demo import app
from demo.view import banner_api

app.register_blueprint(banner_api)

if __name__ == '__main__':
    app.run(debug=True)