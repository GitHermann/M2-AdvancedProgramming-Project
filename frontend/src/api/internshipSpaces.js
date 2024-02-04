const baseUrl = ' http://127.0.0.1:5000';

const getAllinternshipSpaces = async () => {
    try {
        const response = await fetch(`${baseUrl}/internship_spaces`);
        return await response.json();
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};


const createInternshipSpace = async (internshipSpace) => {
    try {
        const startSubmissionDateArray = internshipSpace.startSubmissionDate.split('-').map(Number);
        const endSubmissionDateArray = internshipSpace.endSubmissionDate.split('-').map(Number);

        const formattedInternshipSpace = {
            name: internshipSpace.name,
            promotion: internshipSpace.promotion,
            students_instruction: internshipSpace.students_instruction,
            tutors_instruction: internshipSpace.tutors_instruction,
            startSubmissionDate: startSubmissionDateArray,
            endSubmissionDate: endSubmissionDateArray,
        };

        const response = await fetch(`${baseUrl}/internship_spaces`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formattedInternshipSpace),
        });

        return await response.json();
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};


const deleteInternshipSpace = async (internshipSpacedId) => {
    try {
        const response = await fetch(`${baseUrl}/internship_spaces/${internshipSpacedId}`, {
            method: 'DELETE',
        });

        return await response.json();
    } catch (error) {
        return { error: error.message || 'An error occurred' };
    }
};


export { getAllinternshipSpaces, createInternshipSpace, deleteInternshipSpace };



