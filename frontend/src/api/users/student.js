const baseUrl = ' http://localhost:5000';

const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');

const studentLogin = async (credentials) => {
    try {
        const response = await fetch(`${baseUrl}/users/student/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credentials),
        });
        //const user = response.user;
        //const token = jwt.sign({ user }, secretKey, { expiresIn: '1h' });
        //cookieParser(token);
        //if (response.ok) {
            //const data = await response.json();
            //const token = data.token;
            // Verify the token here if needed
            // ...
            // Set the token in cookies or local storage
            
            // ...
        } else {
            throw new Error('Invalid credentials');
        }
        return await response.json();
   

    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};

export { studentLogin };