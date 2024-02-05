<template>
  <div>
    <div class="page-title">
      <h1>Espaces de stage</h1>
    </div>
    <Table :columns="tableColumns" :items="internshipSpaces" />
    <div class="submit-button-container">
      <RouterLink to="/admin/internship-spaces/add" class="link">
        <button class="submit-button" type="submit">Créer un espace de stage</button>
      </RouterLink>
    </div>
  </div>
</template>

<script>
import Table from "@/components/Table.vue";
import { getAllInternshipSpaces } from "@/api/internshipSpaces";

export default {
  components: {
    Table,
  },
  data() {
    return {
      tableColumns: [
        { key: "name", label: "Intitulé" },
        { key: "promotion", label: "Promotion" },
        { key: "startSubmissionDate", label: "Début des soumissions" },
        { key: "endSubmissionDate", label: "Fin des soumissions" },
      ],
      internshipSpaces : [],
    };
  },
  mounted() {
    this.fetchInternshipSpaces();
  },
  methods: {
    async fetchInternshipSpaces() {
      try {
        this.internshipSpaces = await getAllInternshipSpaces();
      } catch (error) {
        console.error('An error occurred while fetching internship spaces:', error);
      }
    }
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

.submit-button {
  width: 100%;
  align-items: center;
  margin-top: 40px;
  margin-bottom: 20px;
  background-color: #3571a9;
  border-radius: 10px;
  height: 50px;
  border: solid 1px #c7c4c4;
  font-size: 15px;
  color: #f7f7f7;
  font-family: Verdana, sans-serif;
  font-weight: 800;
  border: solid 1px #c7c4c4;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #135c91;
}

.link {
  width: 100%;
  cursor: pointer;
}

.submit-button-container {
  display: flex;
  justify-content: center;
  width: 100%;
}
</style>
