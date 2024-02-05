<template>
  <div>
    <div class="page-title">
      <h1>Tous les stages</h1>
    </div>
    <InternshipTable :columns="tableColumns" :items="internships" />
  </div>
</template>

<script>
import InternshipTable from '@/components/InternshipTable.vue'
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'
import { getAllInternshipsInSpace } from '@/api/internships'

export default {
  components: {
    InternshipTable
  },
  data() {
    return {
      internshipSpaceId: 0,
      tableColumns: [
        { key: 'last_name', label: 'Nom' },
        { key: 'first_name', label: 'Prénom' },
        { key: 'status', label: 'Statut' },
        { key: 'title', label: 'Intitulé' },
        { key: 'company', label: 'Entreprise' },
        { key: 'startDate', label: 'Début' },
        { key: 'endDate', label: 'Fin' },
        { key: 'companyTutor', label: 'Tuteur entreprise' },
        { key: 'academicTutor', label: 'Tuteur école' }
      ],
      internships: [
        {
          id: 1,
          year: '2020-2021',
          status: 'En cours',
          title: 'Stage ingénieur M2',
          company: 'Sopra Steria',
          startDate: '2020-09-01',
          endDate: '2021-02-28'
        },
        {
          id: 2,
          year: '2019-2020',
          status: 'Validé',
          title: 'Stage technique M1',
          company: 'Sopra Steria',
          startDate: '2019-09-01',
          endDate: '2020-02-28'
        },
        {
          id: 3,
          year: '2018-2019',
          status: 'Validé',
          title: 'Stage découverte L2',
          company: 'Sopra Steria',
          startDate: '2018-09-01',
          endDate: '2019-02-28'
        }
      ]
    }
  },
  mounted() {
    this.internshipSpaceId = this.$route.params.id
    this.getAllInternships()
  },
  computed: {
    ...mapWritableState(useStore, ['internship'])
  },
  methods: {
    async getAllInternships() {
      try {
        this.internships = await getAllInternshipsInSpace(this.internshipSpaceId)
      } catch (error) {
        console.error('An error occurred while fetching all internships:', error)
      }
    }
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
</style>
