<template>
  <div>
    <div class="page-title">
      <h1>{{ internshipSpace.name }}</h1>
    </div>
		<form class="login-form" @submit.prevent="saveEdit" :class="{ 'loading': loading }">
			<div class="input-form-container">
				<label class="text" for="name">Intitulé</label>
				<input type="text" id="name" v-model="internshipSpace.name" class="input-form" required :disabled="disabled">
			</div>
			<div class="input-form-container">
				<label class="text" for="promotion">Promotion</label>
				<input type="number" id="promotion" v-model="internshipSpace.promotion" class="input-form" required :disabled="disabled">
			</div>
			<div class="textarea-form-container">
				<label class="text" for="tutors_instruction">Instructions pour les tuteurs</label>
				<textarea id="tutors_instruction" v-model="internshipSpace.tutors_instruction" class="textarea-form" required :disabled="disabled"></textarea>
			</div>
			<div class="textarea-form-container">
				<label class="text" for="students_instruction">Instructions pour les étudiants</label>
				<textarea id="students_instruction" v-model="internshipSpace.students_instruction" class="textarea-form" required :disabled="disabled"></textarea>
			</div>
			<div class="input-form-container">
				<label class="text" for="password">Date de début des soumissions</label>
				<input type="date" id="startSubmissionDate" v-model="internshipSpace.startSubmissionDate" class="input-form" required :disabled="disabled">
			</div>
			<div class="input-form-container">
				<label class="text" for="endSubmissionDate">Date de fin des soumissions</label>
				<input type="date" id="endSubmissionDate" v-model="internshipSpace.endSubmissionDate" class="input-form" required :disabled="disabled">
			</div>
      <div class="action-buttons-container">
        <button class="action-button" id="edit" @click="editSpace" v-if="!editing">Modifier</button>
        <button class="action-button" id="edit" @click="saveEdit" v-if="editing">Sauvegarder</button>
        <button class="action-button" id="delete" @click="deleteSpace">Supprimer</button>
      </div>
    </form>
  </div>
</template>

<script>
import { getOneInternshipSpace, editInternshipSpace, deleteInternshipSpace } from '@/api/internshipSpaces'

export default {
	data() {
		return {
      internshipSpace: {},
      internshipSpaceId: 0,
      editing: false,
      disabled: true,
      loading: false,
      name: '',
      promotion: '',
      tutors_instruction: '',
      students_instruction: '',
      startSubmissionDate: '',
      endSubmissionDate: '',
		}
	},
  mounted() {
    this.internshipSpaceId = this.$route.params.id;
    this.fetchInternshipSpace();
  },
	methods: {
    async fetchInternshipSpace() {
      try {
        this.internshipSpace = await getOneInternshipSpace(this.internshipSpaceId);
      } catch (error) {
        console.error('An error occurred while fetching internship space:', error);
      }
    },
		deleteSpace() {
      deleteInternshipSpace(this.internshipSpace.id)
    },
    editSpace() {
      this.disabled = false;
      this.editing = true;
  
      console.log(this.$route.params.id);
      
    },
    async saveEdit() {
      try {
        this.loading = true;
        await new Promise(resolve => setTimeout(resolve, 2000));
        await editInternshipSpace({
          id: this.internshipSpace.id,
          name: this.name,
          promotion: this.promotion,
          tutors_instruction: this.tutors_instruction,
          students_instruction: this.students_instruction,
          startSubmissionDate: this.startSubmissionDate,
          endSubmissionDate: this.endSubmissionDate,
        });
      } catch (error) {
          console.error('Error submitting form:', error);
      } finally {
        this.loading = false;
      }
    },
	}
}
</script>


<style scoped>

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

.input-form-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  width: 90%;
}
.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
	padding-top: 50px;
  margin: 10px;
  margin-bottom: 30px;
  background-color: #f0f0f0;
  border: none;
  border-radius: 10px;
  width: 90%;
  margin: 0 auto;
}

.input-form {
  display: flex;
  align-items: center;
  padding: 10px;
  margin-top: 4px;
  margin-bottom: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
  height: 20px;
  border: solid 1px #c7c4c4;
}

.textarea-form-container {
	display: flex;
	flex-direction: column;
	align-items: left;
	width: 90%;
}

.textarea-form {
	display: flex;
	align-items: center;
	padding: 10px;
	margin-top: 4px;
	margin-bottom: 20px;
	background-color: #f7f7f7;
	border-radius: 10px;
	height: 100px;
	border: solid 1px #c7c4c4;
}


.text {
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

.loading {
  opacity: 0.7;
  pointer-events: none;
}

</style>