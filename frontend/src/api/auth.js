import { apiClient } from './client';

export const login = (email, password) => {
  return apiClient('/auth/login', { body: { email, password } });
};

export const signup = (username, email, password) => {
  return apiClient('/auth/signup', { body: { username, email, password } });
};
