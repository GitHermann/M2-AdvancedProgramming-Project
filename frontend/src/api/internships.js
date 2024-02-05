const baseUrl = ' http://localhost:5001';

const getOneInternship = async (internshipSpaceId, internshipOrStudentId) => {
  try {
    const response = await fetch(`${baseUrl}/internship_spaces/${internshipSpaceId}/internships/${internshipOrStudentId}`);
    return await response.json();
  } catch (error) {
    return { error: error.message || 'An error occurred' };
  }
};

export { getOneInternship };