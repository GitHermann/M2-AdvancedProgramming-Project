import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/login/LoginView.vue'
import LoginAcademicTutorView from '../views/login/LoginAcademicTutorView.vue'
import LoginAdminView from '../views/login/LoginAdminView.vue'
import LoginCompanyTutorView from '../views/login/LoginCompanyTutorView.vue'
import LoginStudentView from '../views/login/LoginStudentView.vue'


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
    }
  ]
})

export default router
