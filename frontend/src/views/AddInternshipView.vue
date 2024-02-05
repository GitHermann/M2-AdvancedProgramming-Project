<template>
  <div class="container">
    <div class="page-title">
      <h1>Ajouter un stage</h1>
    </div>
    <form class="login-form" @submit.prevent="submitForm" :class="{ loading: loading }">
      <div class="input-form-container">
        <label class="text" for="company">Entreprise</label>
        <input type="text" id="company" v-model="company" class="input-form" required />
      </div>
      <div class="textarea-form-container">
        <label class="text" for="title">Description de la mission</label>
        <textarea id="title" v-model="title" class="textarea-form" required></textarea>
      </div>
      <div class="input-form-container">
        <label class="text" for="startDate">Date de début</label>
        <input type="date" id="startDate" v-model="startDate" class="input-form" required />
      </div>
      <div class="input-form-container">
        <label class="text" for="endSubmissionDate">Date de fin</label>
        <input type="date" id="endDate" v-model="endDate" class="input-form" required />
      </div>
      <div class="input-form-container">
        <label class="text" for="companyTutor">Tuteur entreprise</label>
        <input type="text" id="companyTutor" v-model="companyTutor" class="input-form" required />
      </div>
      <div class="input-form-container">
        <label class="text" for="academicTutor">Tuteur école</label>
        <input type="text" id="academicTutor" v-model="academicTutor" class="input-form" required />
      </div>
      <button class="submit-button" type="submit" :disabled="loading">
        <span v-if="!loading">Ajouter un stage</span>
        <span v-else>Ajout du stage...</span>
      </button>
    </form>
  </div>
</template>

<script>
import { addInternship } from '@/api/internships'
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'

export default {
  data() {
    return {
      loading: false,
      company: '',
      title: '',
      startDate: '',
      endDate: '',
      companyTutor: '',
      academicTutor: ''
    }
  },
  methods: {
    async submitForm() {
      try {
        this.loading = true
        const internship = {
          company: this.company,
          title: this.title,
          startDate: this.startDate,
          endDate: this.endDate,
          companyTutor: this.companyTutor,
          academicTutor: this.academicTutor
        }
        await new Promise((resolve) => setTimeout(resolve, 2000))
        await addInternship(internship, this.internshipSpace.id, this.userId)
      } catch (error) {
        console.error('Error submitting form:', error)
      } finally {
        this.loading = false
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
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
  width: 70%;
  margin: 0 auto;
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
  height: 70px;
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

.loading {
  opacity: 0.7;
  pointer-events: none;
}
</style>
