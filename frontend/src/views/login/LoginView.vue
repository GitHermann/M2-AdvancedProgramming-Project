<template>
  <div>
    <div class="button-container">
      <div>
        <h2 class="title">Vous êtes :</h2>
      </div>
      <RouterLink to="/student/internship-spaces" class="button">
        <i class="icon ri-graduation-cap-line"></i>
        <span class="text">Étudiant</span>
      </RouterLink>
      <RouterLink
        to="/academic-tutor/login"
        class="button"
      >
        <i class="icon ri-school-line"></i>
        <span class="text">Tuteur École</span>
      </RouterLink>
      <RouterLink
        to="/company-tutor/evaluation-forms"
        class="button"
      >
        <i class="icon ri-building-4-line"></i>
        <span class="text">Tuteur Entreprise</span>
      </RouterLink>
      <RouterLink to="/admin/internship-spaces" class="button">
        <i class="icon ri-admin-line"></i>
        <span class="text">Administrateur</span>
      </RouterLink>
    </div>
  </div>
</template>

<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'

export default {
  props: ['login'],
  data() {
    return {
      user: {},
      username: '',
      password: ''
    }
  },
  computed: {
    ...mapWritableState(useStore, ['userType'])
  },
  methods: {
    updateUserType(type) {
      this.userType = type
    },
    async logUser() {
      try {
        this.user = await getAuthenticatedUser();
      } catch (error) {
        console.error('An error occurred while fetching user:', error);
      }
    }
  }
}
</script>

<style scoped>
.button-container {
  margin: 0 auto;
  margin-top: 50px;
  width: 90%;
  max-width: 600px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button {
  display: flex;
  align-items: center;
  padding: 20px;
  margin: 10px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 10px;
  width: 100%;
  height: 48px;
  text-decoration: none;
  color: #333232;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #e0e0e0;
}

.button:active {
  background-color: #d0d0d0;
}

.icon {
  margin-right: 20px;
  margin-left: 20px;
  font-size: 40px;
}

.title {
  font-size: 25px;
  font-family: Verdana, sans-serif;
}

.text {
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

@media (max-width: 480px) {
  .button-container {
    margin-top: 20px;
  }

  .button {
    padding: 15px;
    margin: 8px;
    font-size: 14px;
  }

  .icon {
    font-size: 30px;
    margin-right: 15px;
    margin-left: 15px;
  }

  .title {
    font-size: 20px;
  }

  .text {
    font-size: 14px;
  }
}

@media (min-width: 481px) and (max-width: 767px) {
  .button-container {
    margin-top: 30px;
  }

  .button {
    padding: 18px;
    margin: 10px;
    font-size: 16px;
  }

  .icon {
    font-size: 36px;
    margin-right: 18px;
    margin-left: 18px;
  }

  .title {
    font-size: 22px;
  }

  .text {
    font-size: 16px;
  }
}

@media (min-width: 768px) {
  .button-container {
    margin-top: 40px;
  }

  .button {
    padding: 22px;
    margin: 12px;
    font-size: 18px;
  }

  .icon {
    font-size: 42px;
    margin-right: 22px;
    margin-left: 22px;
  }

  .title {
    font-size: 28px;
  }

  .text {
    font-size: 18px;
  }
}
</style>
