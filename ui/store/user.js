import axios from 'axios';

export const state = () => ({
  username: '',
  role: '',
  firstName: ''
})

export const getters = {
  loggedIn(state) {
    return state.username !== '';
  }
}

export const mutations = {
  setUser(state, user) {
    state.username = user.username;
    state.role = user.role;
    state.firstName = user.firstName;
  }
}

export const actions = {
  async login({ commit }, { username, password }) {
    try {
      const response = await axios.post('/api/login', { username, password });
      commit('setUser', response.data);
    } catch (err) {
      throw new Error('Invalid username or password');
    }
  },
  async signUp({ commit }, user) {
    try {
      await axios.post('/api/user', user);
      commit('setUser', user);
    } catch (err) {
      throw new Error('Username already exists');
    }
  }
}
