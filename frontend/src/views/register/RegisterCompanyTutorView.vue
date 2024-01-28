<template>
  <div class="login-form-container">
    <RegisterTutorForm @submit="login" />
  </div>
</template>
  
<script>

import RegisterTutorForm from '@/components/RegisterTutorForm.vue';

export default {
  components: {
    RegisterTutorForm,
  },
};
</script>
    
<style scoped>
  
.login-form-container {
  margin: 0 auto;
  margin-top: 40px;
  width: 600px;
}

  </style>