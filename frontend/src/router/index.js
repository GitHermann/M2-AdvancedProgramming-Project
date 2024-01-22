import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import LoginAcademicTutorView from '../views/LoginAcademicTutorView.vue'
import LoginAdminView from '../views/LoginAdminView.vue'
import LoginCompanyTutorView from '../views/LoginCompanyTutorView.vue'
import LoginStudentView from '../views/LoginStudentView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
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
