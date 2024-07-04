import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:5000/api'
});

export const register = (user) => api.post('/register', user);
export const login = (credentials) => api.post('/login', credentials);
export const logout = () => api.post('/logout');
export const getBooks = () => api.get('/books');
export const addBook = (book) => api.post('/books', book);
export const requestTransaction = (transaction) => api.post('/transactions', transaction);
export const approveTransaction = (transactionId) => api.post(`/transactions/${transactionId}/approve`);
export const returnTransaction = (transactionId) => api.post(`/transactions/${transactionId}/return`);
export const getTransactions = () => api.get('/transactions');
export const getUsers = () => api.get('/users');
export const updateUser = (userId, user) => api.put(`/users/${userId}`, user);
export const deleteUser = (userId) => api.delete(`/users/${userId}`);

export default api;
