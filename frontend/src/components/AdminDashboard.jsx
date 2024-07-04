import React, { useEffect, useState } from 'react';
import { getUsers, updateUser, deleteUser } from '../api';

function AdminDashboard() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const fetchUsers = async () => {
            const result = await getUsers();
            setUsers(result.data);
        };

        fetchUsers();
    }, []);

    const handleUpdateUser = async (id, role) => {
        await updateUser(id, { role });
        const result = await getUsers();
        setUsers(result.data);
    };

    const handleDeleteUser = async (id) => {
        await deleteUser(id);
        const result = await getUsers();
        setUsers(result.data);
    };

    return (
        <div>
            <h2>Admin Dashboard</h2>
            <table>
                <thead>
                    <tr>
                        <th>Username</th>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map(user => (
                        <tr key={user.id}>
                            <td>{user.username}</td>
                            <td>{user.email}</td>
                            <td>
                                <select
                                    value={user.role}
                                    onChange={(e) => handleUpdateUser(user.id, e.target.value)}
                                >
                                    <option value="Guest">Guest</option>
                                    <option value="Member">Member</option>
                                    <option value="Librarian">Librarian</option>
                                    <option value="Admin">Admin</option>
                                </select>
                            </td>
                            <td>
                                <button onClick={() => handleDeleteUser(user.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default AdminDashboard;
