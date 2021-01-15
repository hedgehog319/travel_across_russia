import axios from "axios";

export default {
    actions: {
        async fetchCities(ctx) {
            const res = await axios.get(`/api/cities`)
            ctx.commit('updateCities', res.data)
        },
    },
    mutations: {
        updateCities(state, cities) {
            state.cities = cities
        },
    },
    getters: {
        getCities(state) {
            return state.cities
        }
    },
    state: {
        cities: []
    }
}