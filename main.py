import sys
from instagram.client import InstagramAPI
from flask import render_template,Flask, Response


app = Flask(__name__)
app.debug=True

@app.route('/')
def main_feed():
    access_token = "674314654.f490ada.e15ed6b4254b4d81b6f8a4fe648fb4bb"
    client_secret = "afb94a2669b046cf92c9585b56b99eba"
    api = InstagramAPI(access_token=access_token, client_secret=client_secret)
    user = api.user(674314654)

    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run()
