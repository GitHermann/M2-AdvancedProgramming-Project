import Cookies from 'js-cookie';

const baseUrl = 'http://localhost:5000';

const studentLogin = async (credentials) => {
    let data;
    try {
        const response = await fetch(`${baseUrl}/users/student/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credentials),
            credentials: 'include',
        });

        if (response.ok) {
            data = await response.json();
        } else {
            throw new Error('Invalid credentials');
        }

        return data;
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};

export { studentLogin };
