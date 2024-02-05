<template>
  <form class="login-form" @submit.prevent="handleLogin">
    <div>
      <h2 class="title">Connexion</h2>
    </div>
    <div class="input-form-container">
      <label class="text" for="username">Nom d'utilisateur</label>
      <input v-model="username" type="text" id="username" name="username" class="input-form" required>
    </div>
    <div class="input-form-container">
      <label class="text" for="password">Mot de passe</label>
      <input v-model="password" type="password" id="password" name="password" class="input-form" required>
    </div>
    <button class="submit-button" type="submit">Se connecter</button>
  </form>
  <div class="signin">
    <span class="text">Vous n'avez pas de compte ? </span> 
    <RouterLink :to="`/register/${userType}`">
      <span class="text">Inscrivez-vous</span>
    </RouterLink>
  </div>
</template>
  
<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { studentLogin } from '@/api/users/student'

export default {
  props: ['login'],
  data() {
    return {
      username: '',
      password: '',
    };
  },
  computed: {
    ...mapWritableState(useStore, ['userType']),
  },
  methods: {
    async handleLogin() {
      console.log('Login:', this.username, this.password);
      if (this.$route.path.includes('student')) {
        try {
        this.loading = true;
        await new Promise(resolve => setTimeout(resolve, 2000));
        const response = await studentLogin({
          email: this.username,
          password: this.password,
        });
        console.log('userId', response);
        //this.resetForm();
      } catch (error) {
          console.error('Error submitting form:', error);
      } finally {
        this.loading = false;
        //this.$router.push('/admin/internship-spaces');
      }
      }
    },
  },
};
</script>

<style scoped>
.input-form-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  width: 90%;
}
.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  margin: 10px;
  margin-bottom: 30px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 10px;
  width: 90%;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2); 
}

.input-form {
  display: flex;
  align-items: center;
  padding: 10px;
  margin-top: 8px;
  margin-bottom: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
  height: 30px;
  border: solid 1px #c7c4c4;
}

.submit-button {
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: #3571a9;
  border-radius: 10px;
  width: 50%;
  height: 50px;
  border: solid 1px #c7c4c4;
  font-size: 15px;
  color: #f7f7f7;
  font-family: Verdana, sans-serif;
  font-weight: 800;
  border: solid 1px #c7c4c4;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #135c91;
}

.link {
  width: 100%;
  cursor: pointer;
}

.title {
  font-size: 25px;
  font-family: Verdana, sans-serif;
  margin-bottom: 40px;
}

.text {
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

.signin {
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>