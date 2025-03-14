# app.py
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# база данных
fake_db = {
    "users": [],  # Список пользователей
    "posts": []   # Список постов
}

# Создание пользователя
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    
    
    if any(user['username'] == data['username'] for user in fake_db['users']):
        return jsonify({'error': 'Username already exists'}), 400
    
    user_id = len(fake_db['users']) + 1
    user = {'id': user_id, 'username': data['username']}
    fake_db['users'].append(user)
    return jsonify(user), 201


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not all(key in data for key in ['title', 'content', 'user_id']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    
    if not any(user['id'] == data['user_id'] for user in fake_db['users']):
        return jsonify({'error': 'User not found'}), 404
    
    post_id = len(fake_db['posts']) + 1
    post = {
        'id': post_id,
        'title': data['title'],
        'content': data['content'],
        'user_id': data['user_id'],
        'created_at': datetime.utcnow().isoformat()
    }
    fake_db['posts'].append(post)
    return jsonify(post), 201


@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(fake_db['posts'])


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in fake_db['posts'] if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post)


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((p for p in fake_db['posts'] if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    
    data = request.get_json()
    post['title'] = data.get('title', post['title'])
    post['content'] = data.get('content', post['content'])
    return jsonify(post)


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((p for p in fake_db['posts'] if p['id'] == post_id), None)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    
    fake_db['posts'] = [p for p in fake_db['posts'] if p['id'] != post_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)