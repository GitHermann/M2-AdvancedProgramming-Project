<template>
	<div class="container">
		<div class="page-title">
      <h1>Ajouter un espace de stage</h1>
    </div>
		<form class="login-form">
			<div class="input-form-container">
				<label class="text" for="name">Intitulé</label>
				<input type="text" id="name" v-model="name" class="input-form" required>
			</div>
			<div class="input-form-container">
				<label class="text" for="promotion">Promotion</label>
				<input type="number" id="promotion" v-model="promotion" class="input-form" required>
			</div>
			<div class="textarea-form-container">
				<label class="text" for="tutors_instruction">Instructions pour les tuteurs</label>
				<textarea id="tutors_instruction" v-model="tutors_instruction" class="textarea-form" required></textarea>
			</div>
			<div class="textarea-form-container">
				<label class="text" for="students_instruction">Instructions pour les étudiants</label>
				<textarea id="students_instruction" v-model="students_instruction" class="textarea-form" required></textarea>
			</div>
			<div class="input-form-container">
				<label class="text" for="password">Date de début des soumissions</label>
				<input type="date" id="startSubmissionDate" v-model="startSubmissionDate" class="input-form" required>
			</div>
			<div class="input-form-container">
				<label class="text" for="endSubmissionDate">Date de fin des soumissions</label>
				<input type="date" id="endSubmissionDate" v-model="endSubmissionDate" class="input-form" required>
			</div>
  		<button class="submit-button" type="submit">Créer un espace de stage</button>
  </form>
	</div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      promotion: '',
      tutors_instruction: '',
      students_instruction: '',
      startSubmissionDate: '',
      endSubmissionDate: '',
    };
  },
};
</script>

<style scoped>

.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	margin-top: 50px;
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

.submit-button {
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: #3571a9;
  border-radius: 10px;
  width: 50%;
  height: 50px;
  border: solid 1px #c7c4c4;
  font-size: 15px;
  color: #f7f7f7;
  font-family: Verdana, sans-serif;
  font-weight: 800;
  border: solid 1px #c7c4c4;
  cursor: pointer;
}

.title {
  font-size: 25px;
  font-family: Verdana, sans-serif;
  margin-bottom: 40px;
}

.text {
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

</style>