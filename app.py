from flask import Flask, render_template
from routes.bot_routes import bot_blueprint

app = Flask(__name__)
app.register_blueprint(bot_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
