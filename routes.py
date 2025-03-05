from flask import request, jsonify
from flask_restx import Resource, Namespace
from database import users, posts
from models import User, Post

api_ns = Namespace("API", description="Основные маршруты")

@api_ns.route("/users")
class Users(Resource):
    def get(self):
        """Получить список пользователей"""
        return jsonify(list(users.values()))

    def post(self):
        """Создать нового пользователя"""
        if not request.is_json:
            return {"error": "Content-Type must be application/json"}, 415
        data = request.get_json()
        if "username" not in data:
            return {"error": "Missing 'username' field"}, 400
        user_id = len(users) + 1
        users[user_id] = User(user_id, data["username"]).__dict__
        return users[user_id], 201

@api_ns.route("/posts")
class Posts(Resource):
    def get(self):
        """Получить список постов"""
        return jsonify(list(posts.values()))

    def post(self):
        """Создать новый пост"""
        if not request.is_json:
            return {"error": "Content-Type must be application/json"}, 415
        data = request.get_json()
        if "user_id" not in data or "title" not in data or "content" not in data:
            return {"error": "Missing required fields"}, 400
        if data["user_id"] not in users:
            return {"error": "User not found"}, 404
        post_id = len(posts) + 1
        posts[post_id] = Post(post_id, data["user_id"], data["title"], data["content"]).__dict__
        return posts[post_id], 201

def init_routes(api):
    api.add_namespace(api_ns, path="/api")
