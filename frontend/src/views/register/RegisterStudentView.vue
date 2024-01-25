<template>
  <div class="login-form-container">
    <RegisterStudentForm @submit="login" />
  </div>
</template>
  
<script>

import RegisterStudentForm from '@/components/RegisterStudentForm.vue';

export default {
  components: {
    RegisterStudentForm,
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