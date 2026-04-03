import { apiClient } from './client';

export const getTasks = () => apiClient('/tasks/');
export const createTask = (task) => apiClient('/tasks/', { body: task });
export const updateTask = (id, updates) => apiClient(`/tasks/${id}`, { method: 'PUT', body: updates });
export const deleteTask = (id) => apiClient(`/tasks/${id}`, { method: 'DELETE' });
