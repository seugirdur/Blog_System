import axios from 'axios';


export const getApi = axios.create({
    baseURL: 'http://localhost:8000/api',
    timeout: 1000,
})


