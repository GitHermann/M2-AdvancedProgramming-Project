import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
  state: () => ({
    userType: '',
    userFirstName: 'John',
    userLastName: 'DOE',
    internshipId: 0,
    internship: {},
    internshipSpaceId: 0,
    internshipSpace: {},
  }),
})
