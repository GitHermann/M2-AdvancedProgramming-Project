<template>
  <div>
    <div class="page-title">
      <h1>Mes stages</h1>
    </div>
    <Table :columns="tableColumns" :items="tableData" />
  </div>
</template>

<script>
import Table from "@/components/Table.vue";

export default {
  components: {
    Table,
  },
  data() {
    return {
      tableColumns: [
        { key: "year", label: "Année" },
        { key: "status", label: "Status" },
        { key: "title", label: "Intitulé" },
        { key: "company", label: "Entreprise" },
        { key: "startDate", label: "Début"},
        { key: "endDate", label: "Fin"},
      ],
      tableData: [
        {
          id: 1,
          year: "2020-2021",
          status: "En cours",
          title: "Stage ingénieur M2",
          company: "Sopra Steria",
          startDate: "2020-09-01",
          endDate: "2021-02-28",
        },
        {
          id: 2,
          year: "2019-2020",
          status: "Validé",
          title: "Stage technique M1",
          company: "Sopra Steria",
          startDate: "2019-09-01",
          endDate: "2020-02-28",
        },
        {
          id: 3,
          year: "2018-2019",
          status: "Validé",
          title: "Stage découverte L2",
          company: "Sopra Steria",
          startDate: "2018-09-01",
          endDate: "2019-02-28",
        },
      ],
    };
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
