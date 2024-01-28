import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
  state: () => ({
    userType: 'admin',
    userFirstName: 'John',
    userLastName: 'DOE',
  }),
})
