from flask import Blueprint, request, jsonify
from models import db
from models.task import Task
from utils.auth import token_required
from datetime import datetime

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['GET'])
@token_required
def get_tasks(current_user_id):
    tasks = Task.query.filter_by(user_id=current_user_id).all()
    return jsonify([task.to_dict() for task in tasks]), 200

@task_bp.route('/', methods=['POST'])
@token_required
def create_task(current_user_id):
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'message': 'Title is required!'}), 400
        
    due_date = None
    if data.get('due_date'):
        try:
            # Handles format '2023-12-01T12:00:00Z'
            due_date_str = data['due_date'].replace('Z', '+00:00')
            due_date = datetime.fromisoformat(due_date_str)
        except ValueError:
            pass 

    new_task = Task(
        user_id=current_user_id,
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'Pending'),
        priority=data.get('priority', 'Medium'),
        due_date=due_date
    )
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({'message': 'Task created!', 'task': new_task.to_dict()}), 201

@task_bp.route('/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user_id, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
    if not task:
        return jsonify({'message': 'Task not found!'}), 404
        
    data = request.get_json()
    if 'title' in data: task.title = data['title']
    if 'description' in data: task.description = data['description']
    if 'status' in data: task.status = data['status']
    if 'priority' in data: task.priority = data['priority']
    if 'due_date' in data:
        if data['due_date'] is None:
            task.due_date = None
        else:
            try:
                due_date_str = data['due_date'].replace('Z', '+00:00')
                task.due_date = datetime.fromisoformat(due_date_str)
            except ValueError:
                pass
            
    db.session.commit()
    return jsonify({'message': 'Task updated!', 'task': task.to_dict()}), 200

@task_bp.route('/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user_id, task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
    if not task:
        return jsonify({'message': 'Task not found!'}), 404
        
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted!'}), 200
