from flask import Blueprint, request, jsonify
from models import db
from models.user import User
from utils.auth import hash_password, verify_password, generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing fields!'}), 400
        
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists!'}), 409
        
    hashed_pw = hash_password(data['password'])
    new_user = User(username=data['username'], email=data['email'], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Missing credentials!'}), 400
        
    user = User.query.filter_by(email=data['email']).first()
    if not user or not verify_password(data['password'], user.password):
        return jsonify({'message': 'Invalid credentials!'}), 401
        
    token = generate_token(user.id)
    return jsonify({
        'message': 'Login successful!',
        'token': token,
        'user': user.to_dict()
    }), 200
