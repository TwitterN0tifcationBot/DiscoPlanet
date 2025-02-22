from flask import Blueprint, request, jsonify
from models.bot_model import create_bot

bot_blueprint = Blueprint('bot', __name__)

@bot_blueprint.route('/create-bot', methods=['POST'])
def create_bot_route():
    data = request.json
    bot_code = create_bot(data)
    return jsonify({"bot_code": bot_code})
