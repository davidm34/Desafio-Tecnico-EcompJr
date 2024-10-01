import React, {useState, useEffect} from 'react'
import api from './api'


const [transactions, setTransactions] = useState([]);

const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
});

const fetchTransactions = async () => {
    const response = await api.get('/transactions/');
    setTransactions(response.data)
};

useEffect(() => {
    fetchTransactions();
}, []);

const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
        ...formData,
        [event.target.name]: value,
    });
}

const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/transactions/', formData);
    fetchTransactions();
    setFormData({
        name: '',
        email: '',
        password: ''    
    });
};
