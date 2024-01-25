<template>
  <form class="login-form">
    <div>
      <h2 class="title">Inscription</h2>
    </div>
    
      <label class="text" for="username">Username:</label>
      <input type="text" id="username" v-model="username" class="input-form" required>
    
    
      <label class="text" for="firstName">First Name:</label>
      <input type="text" id="firstName" v-model="firstName" class="input-form" required>
  
  
      <label class="text" for="lastName">Last Name:</label>
      <input type="text" id="lastName" v-model="lastName" class="input-form" required>
  
    
      <label class="text" for="email">Email:</label>
      <input type="email" id="email" v-model="email" class="input-form" required>
  
    
      <label class="text" for="password">Password:</label>
      <input type="password" id="password" v-model="password" class="input-form" required>
    
    
      <label class="text" for="phone">Phone:</label>
      <input type="tel" id="phone" v-model="phone" class="input-form" required>
    
    
      <label class="text" for="promotion">Promotion:</label>
      <input type="text" id="promotion" v-model="promotion" class="input-form" required>
  
    <button class="submit-button" type="submit">Creer un compte</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      phone: '',
      promotion: ''
    };
  }
};
</script>

<style scoped>
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
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
  width: 80%;
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

</style>