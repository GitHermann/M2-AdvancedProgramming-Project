const baseUrl = ' http://localhost:5001';

const getOneInternship = async (internshipSpaceId, internshipId) => {
  try {
    const response = await fetch(`${baseUrl}/internship_spaces/${internshipSpaceId}/internships/${internshipId}`);
    return await response.json();
  } catch (error) {
    return { error: error.message || 'An error occurred' };
  }
};

export { getOneInternship };