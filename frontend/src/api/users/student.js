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

const getAuthenticatedUser = async () => {
    try {
        const response = await fetch(`${baseUrl}/users/student/profile`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
        });
        return await response.json();
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};


export { studentLogin, getAuthenticatedUser };
