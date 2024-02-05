<script setup>
import { RouterView } from 'vue-router'
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { getAuthenticatedUser } from '@/api/users/student'
</script>

<template>
  <header>
    <div class="header">
      <RouterLink to="/">
        <img src="./assets/LOGO_EFREI-WEB_blanc.png" alt="LOGO_EFREI-WEB_blanc" />
      </RouterLink>
      <div v-if="this.$route.path.includes('student')" class="user-type-container">
        <i class="icon ri-graduation-cap-line"></i>
        <span class="text">Étudiant</span>
      </div>
      <div v-if="this.$route.path.includes('academic-tutor')" class="user-type-container">
        <i class="icon ri-school-line"></i>
        <span class="text">Tuteur École</span>
      </div>
      <div v-if="this.$route.path.includes('company-tutor')" class="user-type-container">
        <i class="icon ri-building-4-line"></i>
        <span class="text">Tuteur Entreprise</span>
      </div>
      <div v-if="this.$route.path.includes('admin')" class="user-type-container">
        <i class="icon ri-admin-line"></i>
        <span class="text">Administrateur</span>
      </div>
      <div class="user-name-container">
        <p>{{ userFirstName }} {{ userLastName }}</p>
      </div>
      <div class="user-icon-container">
        <i class="icon ri-account-circle-line"></i>
      </div>
    </div>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script>
import {useUserStore} from "@/stores/store.js";

export default {
  computed: {
    ...mapWritableState(useStore, ['userFirstName']),
    ...mapWritableState(useStore, ['userLastName'])
  },
  methods: {
    async logUser() {
      try {
        const store = useUserStore()
        this.user = await getAuthenticatedUser()
        console.log(this.user)
        store.setUser(this.user)
        console.log(store.getUser)
      } catch (error) {
        console.error('An error occurred while fetching user:', error)
      }
    }
  }
}
</script>

<style scoped>
.header {
  background-color: #3571a9;
  padding: 10px;
  color: white;
  border-radius: 10px;
  justify-content: left;
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 75px;
  margin-bottom: 40px;
}

img {
  width: 100px;
  margin: 40px;
}

.icon {
  font-size: 30px;
  margin-right: 16px;
}

.text {
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

.user-type-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-right: auto;
  margin-left: 15px;
  border: solid 2px #f7f7f7;
  border-radius: 15px;
  padding: 8px;
}

.user-name-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-right: 15px;
  margin-left: auto;
  border: solid 2px #f7f7f7;
  border-radius: 15px;
  padding: 8px;
  font-family: Verdana, sans-serif;
}

p {
  margin: 0;
}

main {
  margin: 24px;
}
</style>
