const baseUrl = ' http://localhost:5001';

const getOneInternship = async (internshipSpaceId, internshipOrStudentId) => {
  try {
    const response = await fetch(`${baseUrl}/internship_spaces/${internshipSpaceId}/internships/${internshipOrStudentId}`);
    return await response.json();
  } catch (error) {
    return { error: error.message || 'An error occurred' };
  }
};

const getAllInternshipsInSpace = async (internshipSpaceId) => {
  try {
    const response = await fetch(`${baseUrl}/internship_spaces/${internshipSpaceId}/internships`);
    return await response.json();
  } catch (error) {
    return { error: error.message || 'An error occured' };
  }
}

const addInternship = async (internship, internshipSpaceId, internshipOrStudentId) => {
  try {
    const startDateArray = internship.startDate.split('-').map(Number);
    const endDateArray = internship.endDate.split('-').map(Number);

    const formattedInternship = {
      title: internship.title,
      startDate: startDateArray,
      endDate: endDateArray,
      company: internship.company,
      academicTutor: internship.academicTutor,
      companyTutor: internship.companyTutor
    }

    const response = await fetch(`${baseUrl}/internship_spaces/${internshipSpaceId}/internships/${internshipOrStudentId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formattedInternship)
    });
    return await response.json();
  } catch (error) {
    return { error: error.message || 'An error occurred' };
  }
}

export { getOneInternship, getAllInternshipsInSpace, addInternship };