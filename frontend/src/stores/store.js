import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
  state: () => ({
    userType: 'student',
    userFirstName: 'John',
    userLastName: 'DOE',
  }),
})
