const baseUrl = ' http://127.0.0.1:5000';

const getAllinternshipSpaces = async () => {
    try {
        const response = await fetch(`${baseUrl}/internship_spaces`);
        return await response.json();
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};

export { getAllinternshipSpaces };



