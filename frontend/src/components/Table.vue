<template>
  <table class="table">
    <thead>
      <tr>
        <th v-for="column in columns" :key="column.key">{{ column.label }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in items" :key="item.id" @click="navigateToDetails(item)">
        <td v-for="column in columns" :key="column.key">{{ item[column.key] }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { useStore } from '@/stores/store'
import { mapWritableState } from 'pinia'

export default {
  props: {
    columns: {
      type: Array,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
  },
  methods: {
    navigateToDetails(item) {
      if (this.$route.path.includes('student')) {
        this.internship = item;
        this.$router.push(`/student/internships/${item.id}`);
      }
      else if (this.$route.path.includes('company-tutor')) {
        this.$router.push(`/company-tutor/evaluation-forms/${item.id}`);
      }
      else if (this.$route.path.includes('admin')) {
        this.$router.push(`/admin/internship-spaces/${item.id}`);
      }
      
    },
  },
  computed: {
    ...mapWritableState(useStore, ['internship']),
  },
};
</script>

<style scoped>

.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 16px;
  font-family: Verdana, sans-serif;
}

.table th,
.table td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.table th {
  background-color: #f2f2f2;
  color: #333;
}

.table tbody tr:nth-child(even) {
  background-color: #f9f9f9;
}

.table tbody tr:hover {
  background-color: #f5f5f5;
  cursor: pointer;
}

</style>
