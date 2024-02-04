<template>
  <div>
    <div class="page-title">
      <h1>Mes formulaires d'évaluations</h1>
    </div>
    <Table :columns="tableColumns" :items="evaluationForms" />
  </div>
</template>
  
<script>
import Table from "@/components/Table.vue";
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'

export default {
  components: {
    Table,
  },
  data() {
    return {
      tableColumns: [
        { key: "year", label: "Année" },
        { key: "student", label: "Etudiant" },
        { key: "title", label: "Formulaire" },
        { key: "startSubmissionDate", label: "Date d'ouverture"},
        { key: "endSubmissionDate", label: "Date de fermeture"},
      ],
      evaluationForms: [
        {
          id: 1,
          year: "2023-2024",
          student: "Jean Dupont",
          title: "Formulaire intermédiaire",
          startSubmissionDate: "2024-01-01",
          endSubmissionDate: "2024-02-28",
        },
        {
          id: 2,
          year: "2023-2024",
          student: "Alexis Durand",
          title: "Formulaire fin de stage",
          startSubmissionDate: "2024-06-01",
          endSubmissionDate: "2024-07-01",
        },
      ],
    };
  },
  computed: {
    ...mapWritableState(useStore, ['internship']),
  },
  methods: {
    updateInternshipId(internshipId) {
      this.internshipId = internshipId;
    },
  },
};
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
