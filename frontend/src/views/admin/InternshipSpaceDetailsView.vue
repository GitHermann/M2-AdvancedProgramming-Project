<template>
  <div>
    <div class="page-title">
      <h1>{{ internshipSpace.name }}</h1>
    </div>
		<div class="details-container" >
			<h2>Promotion : {{ internshipSpace.promotion }}</h2>
			<h2>Instructions pour les tuteurs : {{ internshipSpace.tutors_instruction }}</h2>
			<h2>Instructions pour les étudiants : {{ internshipSpace.students_instruction }}</h2>
			<h2>Date de début des soumissions : {{ internshipSpace.startSubmissionDate }}</h2>
			<h2>Date de fin des soumissions :{{ internshipSpace.endSubmissionDate }}</h2>
		</div>
    <div class="action-buttons-container">
      <button class="action-button" id="edit">Modifier</button>
      <button class="action-button" id="delete" @click="deleteSpace">Supprimer</button>
    </div>
  </div>
</template>


<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { deleteInternshipSpace } from '@/api/internshipSpaces'

export default {
	data() {
		return {
		}
	},
	methods: {
		deleteSpace() {
      deleteInternshipSpace(this.internshipSpace.id)
    }
	},
	computed: {
    ...mapWritableState(useStore, ['internshipSpace']),
  },
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
  background-color: #CA2424;
}


</style>