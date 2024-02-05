<template>
  <div>
    <div class="page-title">
      <h1>{{ internshipSpace.name }}</h1>
    </div>
    <div class="details-container">
      <h2>Promotion : {{ internshipSpace.promotion }}</h2>
      <h2>Instructions pour les étudiants : {{ internshipSpace.students_instruction }}</h2>
      <h2>Date de début des soumissions : {{ internshipSpace.startSubmissionDate }}</h2>
      <h2>Date de fin des soumissions :{{ internshipSpace.endSubmissionDate }}</h2>
    </div>
    <div class="details-container">
      <h2>Intitulé du stage : {{ internship.title }}</h2>
      <h2>Status : {{ internship.status }}</h2>
      <h2>Nom de l'entreprise : {{ internship.company }}</h2>
      <h2>Nom du tuteur entreprise : {{ internship.companyTutor }}</h2>
      <h2>Nom du tuteur école : {{ internship.academicTutor }}</h2>
      <h2>Début du stage : {{ internship.startDate }}</h2>
      <h2>Fin du stage : {{ internship.endDate }}</h2>
    </div>
    <div class="action-buttons-container"></div>
  </div>
</template>

<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { getOneInternship } from '@/api/internships'

export default {
  data() {
    return {
      internship: []
    }
  },
  mounted() {
    this.fetchInternship()
  },
  methods: {
    async fetchInternship() {
      console.log(this.userId)
      try {
        this.internship = await getOneInternship(this.internshipSpace.id, this.userId)
      } catch (error) {
        console.error('An error occurred while fetching internships:', error)
      }
    }
  },
  computed: {
    ...mapWritableState(useStore, ['internshipSpace']),
    ...mapWritableState(useStore, ['userId'])
  }
}
</script>

<style scoped>
.details-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  padding: 10px;
  margin: 0 auto;
  padding-left: 40px;
  margin-bottom: 30px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 10px;
  width: 80%;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
  font-size: 12px;
  font-family: Verdana, sans-serif;
}

.page-title {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
}

h1 {
  font-size: 32px;
  font-family: Verdana, sans-serif;
}

.action-buttons-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 0 auto;
  width: 81%;
}

.action-button {
  width: 100%;
  align-items: center;
  margin-top: 40px;
  margin-bottom: 20px;
  border-radius: 10px;
  margin-left: 20px;
  margin-right: 00px;
  height: 50px;
  border: solid 1px #c7c4c4;
  font-size: 15px;
  color: #f7f7f7;
  font-family: Verdana, sans-serif;
  font-weight: 800;
  border: solid 1px #c7c4c4;
  cursor: pointer;
}

#edit {
  background-color: #3571a9;
}

#delete {
  background-color: #ca2424;
}
</style>
