import React, { useState, useEffect } from 'react';
import { getTasks, createTask, updateTask, deleteTask } from '../api/tasks';

const Dashboard = ({ user, onLogout }) => {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [dueDate, setDueDate] = useState('');
  
  const fetchTasks = async () => {
    try {
      const data = await getTasks();
      setTasks(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleCreate = async (e) => {
    e.preventDefault();
    if (!title) return;
    try {
      const newTask = { title, description, due_date: dueDate ? new Date(dueDate).toISOString() : null };
      await createTask(newTask);
      fetchTasks();
      setTitle('');
      setDescription('');
      setDueDate('');
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteTask(id);
      fetchTasks();
    } catch (err) {
      console.error(err);
    }
  };

  const handleToggleStatus = async (task) => {
    try {
      const newStatus = task.status === 'Completed' ? 'Pending' : 'Completed';
      await updateTask(task.id, { status: newStatus });
      fetchTasks();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="dashboard-container">
      <header className="glass-panel dashboard-header">
        <h1>Smart Task Manager</h1>
        <div className="user-controls">
          <span>Hello, {user.username}</span>
          <button onClick={onLogout} className="btn outline-btn">Log Out</button>
        </div>
      </header>

      <main className="dashboard-content">
        <aside className="task-form-panel glass-panel">
          <h3>Add New Task</h3>
          <form onSubmit={handleCreate}>
            <div className="form-group">
              <input type="text" placeholder="Task Title" value={title} onChange={e => setTitle(e.target.value)} required />
            </div>
            <div className="form-group">
              <textarea placeholder="Description" value={description} onChange={e => setDescription(e.target.value)} />
            </div>
            <div className="form-group">
              <input type="date" value={dueDate} onChange={e => setDueDate(e.target.value)} />
            </div>
            <button type="submit" className="btn primary-btn">Add Task</button>
          </form>
        </aside>

        <section className="task-list-panel glass-panel">
          <h3>Your Tasks</h3>
          {tasks.length === 0 ? <p className="empty-state">No tasks yet. Create one!</p> : null}
          <div className="task-grid">
            {tasks.map(task => (
              <div key={task.id} className={`task-card ${task.status === 'Completed' ? 'completed' : ''}`}>
                <div className="task-header">
                  <h4>{task.title}</h4>
                  <span className={`status-badge ${task.status.toLowerCase().replace(' ', '-')}`}>{task.status}</span>
                </div>
                <p>{task.description}</p>
                {task.due_date && <small>Due: {new Date(task.due_date).toLocaleDateString()}</small>}
                <div className="task-actions">
                  <button onClick={() => handleToggleStatus(task)} className="btn small-btn">
                    {task.status === 'Completed' ? 'Mark Pending' : 'Complete'}
                  </button>
                  <button onClick={() => handleDelete(task.id)} className="btn small-btn danger-btn">Delete</button>
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
};

export default Dashboard;
