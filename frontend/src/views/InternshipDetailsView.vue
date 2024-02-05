<template>
  <div class="InternshipDetailsViewBody">
    <div class="page-title">
      <h1>{{ internship.title }}</h1>
    </div>
    <div class="details-container">
      <h2>Nom élève :</h2>
      <p>{{}}</p>
      <hr />
      <h2>Prénom élève :</h2>
      <p>{{}}</p>
      <hr />
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
    <div class="action-buttons-container">
      <button
        class="action-button"
        id="edit"
        v-if="internship.status == 'En cours de validation'"
        @click="validate"
      >
        Approuver stage
      </button>
      <button
        class="action-button"
        id="delete"
        v-if="internship.status == 'En cours de validation'"
        @click="reject"
      >
        Rejeter stage
      </button>
    </div>
  </div>
</template>

<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { setInternshipStatus } from '@/api/internships'

export default {
  data() {
    return {}
  },
  mounted() {},
  methods: {
    async validate() {
      setInternshipStatus(this.internship.id, 1)
    },
    async reject() {
      setInternshipStatus(this.internship.id, 2)
    }
  },
  computed: {
    ...mapWritableState(useStore, ['internship'])
  }
}
</script>

<style scoped>
.InternshipDetailsViewBody {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
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
