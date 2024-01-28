<template>
  <form class="login-form">
    <div>
      <h2 class="title">Inscription</h2>
    </div>
    <div class="input-form-container">
      <label class="text" for="username">Nom d'utilisateur</label>
      <input type="text" id="username" v-model="username" class="input-form" required>
    </div>
    <div class="input-form-container">
      <label class="text" for="firstName">Prénom</label>
      <input type="text" id="firstName" v-model="firstName" class="input-form" required>
    </div>
    <div class="input-form-container">
      <label class="text" for="lastName">Nom</label>
      <input type="text" id="lastName" v-model="lastName" class="input-form" required>
    </div>
    <div class="input-form-container">
      <label class="text" for="email">Email</label>
      <input type="email" id="email" v-model="email" class="input-form" required>
    </div>
    <div class="input-form-container">
      <label class="text" for="password">Mot de passe</label>
      <input type="password" id="password" v-model="password" class="input-form" required>
    </div>
    <div class="input-form-container">
      <label class="text" for="phone">Téléphone</label>
      <input type="tel" id="phone" v-model="phone" class="input-form" required>
    </div>
    <button class="submit-button" type="submit">Créer un compte</button>
  </form>
  <div class="signin">
    <span class="text">Vous avez déjà un compte ? </span> 
    <RouterLink :to="`/login/${userType}`">
      <span class="text">Connectez-vous</span>
    </RouterLink>
  </div>
</template>

<script>

import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'

export default {
  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      phone: '',
    };
  },
  computed: {
    ...mapWritableState(useStore, ['userType']),
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
  margin-top: 4px;
  margin-bottom: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
  height: 20px;
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