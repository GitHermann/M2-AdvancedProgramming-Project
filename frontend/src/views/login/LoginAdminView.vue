<template>
  <div class="login-form-container">
    <LoginForm @submit="login" />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue';

export default {
  components: {
    LoginForm,
  },
  methods: {
    login(userData) {
      console.log('Admin Login:', userData);
    },
  },
};
</script>
  
<style scoped>

.login-form-container {
  margin: 50px auto 0;
  width: 600px;
}

</style>
