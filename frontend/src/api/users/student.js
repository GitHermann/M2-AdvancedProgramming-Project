const baseUrl = ' http://localhost:5000';

//const jwt = require('jsonwebtoken');
//const cookieParser = require('cookie-parser');

const studentLogin = async (credentials) => {

    let data;
    try {
        const response = await fetch(`${baseUrl}/users/student/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credentials),
        });

        if (response.ok) {
            data = await response.json();
             // Set the token as an HTTP-only cookie
            document.cookie = `access_token=${data.token}; path=/; secure; HttpOnly; SameSite=Strict`;
        } else {
            throw new Error('Invalid credentials');
        }
        return data;
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};

export { studentLogin };