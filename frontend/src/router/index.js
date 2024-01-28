import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/login/LoginView.vue'
import LoginAcademicTutorView from '../views/login/LoginAcademicTutorView.vue'
import LoginAdminView from '../views/login/LoginAdminView.vue'
import LoginCompanyTutorView from '../views/login/LoginCompanyTutorView.vue'
import LoginStudentView from '../views/login/LoginStudentView.vue'
import RegisterAcademicTutorView from '../views/register/registerAcademicTutorView.vue'
import RegisterCompanyTutorView from '../views/register/RegisterCompanyTutorView.vue'
import RegisterStudentView from '../views/register/RegisterStudentView.vue'
import AdminSpaceHomeView from '../views/admin/AdminSpaceHomeView.vue'
import InternshipsView from '../views/InternshipsView.vue'


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
      path: '/login/academic-tutor',
      name: 'login-academic-tutor',
      component: LoginAcademicTutorView
    },
    {
      path: '/login/admin',
      name: 'login-admin',
      component: LoginAdminView
    },
    {
      path: '/login/company-tutor',
      name: 'login-company-tutor',
      component: LoginCompanyTutorView
    },
    {
      path: '/login/student',
      name: 'login-student',
      component: LoginStudentView
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
      path: '/admin',
      name: 'admin-space-home',
      component: AdminSpaceHomeView
    },
    {
      path: '/student/internships',
      name: 'student-internships',
      component: InternshipsView
    }
  ]
})

export default router
