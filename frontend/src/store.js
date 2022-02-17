import { createStore } from 'vuex'

export default createStore({
  state() {
    return {
      server: process.env.NODE_ENV === 'development' ? 'http://127.0.0.1:8000/api/' : 'https://api.vinfixer.com/api/',
      auth_headers: { 'Authorization': 'JWT ' + localStorage.getItem('access_token') },
    }
  },

  actions: {},

  mutations: {
    setAuthHeaders(state, access) {
      localStorage.setItem('access_token', access)
      state.auth_headers = { 'Authorization': 'JWT ' + access }
    },
  }
})