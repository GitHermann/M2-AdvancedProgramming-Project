<template>
  <div>
    <div class="page-title">
      <h1>{{ internship.title }}</h1>
    </div>
		<div class="details-container" >
			<h2>Année : {{ internship.year }}</h2>
			<h2>Statut : {{ internship.status }}</h2>
			<h2>Entreprise : {{ internship.company }}</h2>
			<h2>Début : {{ internship.startDate }}</h2>
			<h2>Fin : {{ internship.endDate }}</h2>
		</div>
    <div>

    </div>
  </div>
</template>


<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'

export default {
	data() {
		return {
		}
	},
	methods: {
		// Add your methods here
	},
	computed: {
    ...mapWritableState(useStore, ['internship']),
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

</style>