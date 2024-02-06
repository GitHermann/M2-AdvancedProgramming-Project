<template>
  <div class="StudentInternshipSpaceDetailsViewBody">
    <div class="page-title">
      <h1>{{ internshipSpace.name }}</h1>
    </div>
    <div class="details-container-internship-space">
      <main>
        <article>
          <h2>Promotion</h2>
          <p>{{ internshipSpace.promotion }}</p>
        </article>
        <article>
          <h2>Instructions pour les étudiants</h2>
          <p>{{ internshipSpace.students_instruction }}</p>
        </article>
        <article>
          <h2>Date de début des soumissions</h2>
          <p>{{ internshipSpace.startSubmissionDate }}</p>
        </article>
        <article>
          <h2>Date de fin des soumissions</h2>
          <p>{{ internshipSpace.endSubmissionDate }}</p>
        </article>
      </main>
    </div>
    <div class="details-container" v-if="found">
      <h2>Intitulé du stage :</h2>
      <p>{{ internship.title }}</p>
      <hr />
      <h2>Status :</h2>
      <p>{{ internship.status }}</p>
      <hr />
      <h2>Nom de l'entreprise :</h2>
      <p>{{ internship.company }}</p>
      <hr />
      <h2>Nom du tuteur entreprise :</h2>
      <p>{{ internship.companyTutor }}</p>
      <hr />
      <h2>Nom du tuteur école :</h2>
      <p>{{ internship.academicTutor }}</p>
      <hr />
      <h2>Début du stage :</h2>
      <p>{{ internship.startDate }}</p>
      <hr />
      <h2>Fin du stage :</h2>
      <p>{{ internship.endDate }}</p>
    </div>
    <div class="action-buttons-container" v-if="!found">
      <RouterLink to="/student/internships/add" class="button" @click="">
        <i class="ri-file-add-line"></i>
        <span class="text">Ajouter un stage</span>
      </RouterLink>
    </div>
  </div>
</template>

<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { getOneInternship } from '@/api/internships'

export default {
  data() {
    return {
      found: true,
      internship: []
    }
  },
  mounted() {
    this.fetchInternship()
  },
  methods: {
    async fetchInternship() {
      try {
        this.internship = await getOneInternship(this.internshipSpace.id, this.userId)
        //console.log(this.internship.message)
        if (this.internship.message == 'Internship not found') {
          this.found = false
        }
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
.StudentInternshipSpaceDetailsViewBody {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.details-container-internship-space {
  width: 80%;
  margin-bottom: 30px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  font-family: Verdana, sans-serif;
  font-size: 12px;
  text-align: center;
  border-radius: 10px;
}
.details-container-internship-space main {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.details-container-internship-space main article {
  width: 20%;
  padding: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  background-color: #fafafa;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}
.details-container-internship-space main article h2 {
  width: 100%;
  color: #0d3765;
}
.details-container-internship-space main article p {
  width: 100%;
}

.details-container {
  width: 80%;
  margin-bottom: 30px;
  padding: 10px 25px 10px 25px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  font-family: Verdana, sans-serif;
  font-size: 12px;
  text-align: left;
  background-color: #f0f6fb;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}
.details-container h2 {
  width: 50%;
  color: #0d3765;
}
.details-container p {
  width: 50%;
  color: rgb(100, 100, 100);
}

hr {
  width: 100%;
  height: 0.5px;
  margin: 0px;
  background-color: rgb(200, 200, 200);
  border: 0;
}

.page-title {
  width: 100%;
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
  cursor: pointer;
}

.button {
  display: flex;
  align-items: center;
  padding: 20px;
  margin: 10px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 10px;
  width: 100%;
  height: 48px;
  text-decoration: none;
  color: #333232;
  box-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #e0e0e0;
}

.button:active {
  background-color: #d0d0d0;
}

.icon {
  margin-right: 20px;
  margin-left: 20px;
  font-size: 40px;
}

.text {
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

#edit {
  background-color: #3571a9;
}

#delete {
  background-color: #ca2424;
}
</style>
