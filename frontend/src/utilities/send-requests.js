import * as userService from './users-service'

export default async function sendRequest(url, method = 'GET', payload = null) {
    const options = { method };
    if (payload) {
        options.headers = { 'Content-Type': 'application/json' };
        options.body = JSON.stringify(payload);
    }

    const token = userService.getToken();
    if(token){
        options.headers = options.headers || {};
        options.headers.Authorization = `Bearer ${token}`;
    }  

    const res = await fetch(url, options);
    console.log(res)
    if (res.ok) return res.json();
    throw new Error('Bad Request')
    
}