import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/login/LoginView.vue'
import LoginAcademicTutorView from '../views/login/LoginAcademicTutorView.vue'
import LoginAdminView from '../views/login/LoginAdminView.vue'
import LoginCompanyTutorView from '../views/login/LoginCompanyTutorView.vue'
import LoginStudentView from '../views/login/LoginStudentView.vue'
import RegisterAcademicTutorView from '../views/register/RegisterAcademicTutorView.vue'
import RegisterCompanyTutorView from '../views/register/RegisterCompanyTutorView.vue'
import RegisterStudentView from '../views/register/RegisterStudentView.vue'
import InternshipSpacesView from '../views/admin/InternshipSpacesView.vue'
import StudentInternshipSpacesView from '../views/student/StudentInternshipSpacesView.vue'
import StudentInternshipSpaceDetailsView from '../views/student/StudentInternshipSpaceDetailsView.vue'
import AddInternshipSpaceView from '../views/admin/AddInternshipSpaceView.vue'
import InternshipsView from '../views/InternshipsView.vue'
import InternshipDetailsView from '../views/InternshipDetailsView.vue'
import AddInternshipView from '../views/AddInternshipView.vue'
import InternshipSpaceDetailsView from '../views/admin/InternshipSpaceDetailsView.vue'
import EvaluationFormsView from '../views/company-tutor/EvaluationFormsView.vue'
import EvaluationFormDetailsView from '../views/company-tutor/EvaluationFormDetailsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/academic-tutor/login',
      name: 'login-academic-tutor',
      component: LoginAcademicTutorView,
    },
    {
      path: '/admin/login',
      name: 'login-admin',
      component: LoginAdminView,
    },
    {
      path: '/company-tutor/login',
      name: 'login-company-tutor',
      component: LoginCompanyTutorView,
    },
    {
      path: '/student/login',
      name: 'login-student',
      component: LoginStudentView,
    },
    {
      path: '/register/academic-tutor',
      name: 'register-academic-tutor',
      component: RegisterAcademicTutorView
    },
    {
      path: '/register/company-tutor',
      name: 'register-company-tutor',
      component: RegisterCompanyTutorView
    },
    {
      path: '/register/student',
      name: 'register-student',
      component: RegisterStudentView
    },
    {
      path: '/admin/internship-spaces',
      name: 'admin-internship-spaces',
      component: InternshipSpacesView
    },
    {
      path: '/admin/internship-spaces/:id',
      name: 'admin-internship-space-details',
      component: InternshipSpaceDetailsView
    },
    {
      path: '/student/internship-spaces',
      name: 'student-internship-spaces',
      component: StudentInternshipSpacesView
    },
    {
       path: '/student/internship-spaces/:id',
       name: 'student-internship-space-details',
       component: StudentInternshipSpaceDetailsView
    },
    {
      path: '/admin/internship-spaces/:id/internships',
      name: 'admin-internships',
      component: InternshipsView
    },
    {
      path: '/admin/internship-spaces/:internshipSpaceId/internships/:intershipId',
      name: 'admin-internship-details',
      component: InternshipDetailsView
    },
    {
      path: '/admin/internship-spaces/add',
      name: 'admin-add-internship-space',
      component: AddInternshipSpaceView
    },
    {
      path: '/student/internships/add',
      name: 'student-add-internship',
      component: AddInternshipView
    },
    {
      path: '/company-tutor/evaluation-forms',
      name: 'company-tutor-evaluation-forms',
      component: EvaluationFormsView
    },
    {
      path: '/company-tutor/evaluation-forms/:id',
      name: 'company-tutor-evaluation-form-details',
      component: EvaluationFormDetailsView
    }
  ]
})

export default router
