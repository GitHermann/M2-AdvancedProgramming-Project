<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="header">
      <img src="./assets/LOGO_EFREI-WEB_blanc.png" alt="LOGO_EFREI-WEB_blanc">
    </div>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>

header {
  background-color: #3571a9;
  padding: 10px;
  text-align: left;
  color: white;
  border-radius: 10px;
  justify-content: center;
}

img {
  width: 100px;
  margin: 40px;
}


</style>  
