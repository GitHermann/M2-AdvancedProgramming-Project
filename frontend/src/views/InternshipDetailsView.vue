<template>
  <div>
    <div class="page-title">
      <h1>{{ internship.title }}</h1>
    </div>
		<div>
			<h2>Année : {{ internship.year }}</h2>
			<h2>Statut : {{ internship.status }}</h2>
			<h2>Entreprise : {{ internship.company }}</h2>
			<h2>Début : {{ internship.startDate }}</h2>
			<h2>Fin : {{ internship.endDate }}</h2>
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