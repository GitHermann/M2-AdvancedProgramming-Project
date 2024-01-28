<template>
  <div>
    <h2>Mes stages</h2>
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
        { key: "id", label: "ID" },
        { key: "name", label: "Name" },
        { key: "position", label: "Position" },
        { key: "salary", label: "Salary" },
      ],
      tableData: [
        { id: 1, name: "John Doe", position: "Developer", salary: 50000 },
        { id: 2, name: "Jane Doe", position: "Designer", salary: 60000 },
      ],
    };
  },
};
</script>

<style scoped>

</style>
