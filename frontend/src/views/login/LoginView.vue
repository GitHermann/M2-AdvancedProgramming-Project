<template>
  <div>
    <div class="button-container">
      <div>
        <h2 class="title">Vous êtes :</h2>
      </div>
      <RouterLink to="/login/student" class="button">
        <i class="icon ri-graduation-cap-line"></i>
        <span class="text">Élève</span>
      </RouterLink>
      <RouterLink to="/login/academic-tutor" class="button">
        <i class="icon ri-school-line"></i>
        <span class="text">Tuteur École</span>
      </RouterLink>
      <RouterLink to="/login/company-tutor" class="button">
        <i class="icon ri-building-4-line"></i>
        <span class="text">Tuteur Entreprise</span>
      </RouterLink>
      <RouterLink to="/login/admin" class="button">
        <i class="icon ri-admin-line"></i>
        <span class="text">Administrateur</span>
      </RouterLink>
    </div>
  </div>
</template>

<style scoped>
.button-container {
  margin: 0 auto;
  margin-top: 50px;
  width: 600px;
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
  width: 90%;
  height: 48px;
  text-decoration: none;
  color: #333232;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
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
</style>
    
