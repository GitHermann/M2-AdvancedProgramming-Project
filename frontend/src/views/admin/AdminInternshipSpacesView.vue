<template>
  <div>
    <div class="page-title">
      <h1>Espaces de stages</h1>
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
        { key: "name", label: "Intitulé" },
        { key: "promotion", label: "Promotion" },
        { key: "startSubmissionDate", label: "Début des soumissions" },
        { key: "endSubmissionDate", label: "Fin des soumissions" },
      ],
      tableData: [
				{
					id: 1,
					name: "Stage ingénieur M2",
					promotion: "2020-2021",
					startSubmissionDate: "2020-09-01",
					endSubmissionDate: "2021-02-28",
				},
				{
					id: 2,
					name: "Stage technique M1",
					promotion: "2019-2020",
					startSubmissionDate: "2019-09-01",
					endSubmissionDate: "2020-02-28",
				},
				{
					id: 3,
					name: "Stage découverte L2",
					promotion: "2018-2019",
					startSubmissionDate: "2018-09-01",
					endSubmissionDate: "2019-02-28",
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
