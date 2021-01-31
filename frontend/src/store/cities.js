import axios from "axios";

export default {
    actions: {
        async fetchCities(ctx) {
            const res = await axios.get(`/api/cities/`)
                .catch(err => console.log(err))
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
            // return JSON.parse(JSON.stringify(state.cities)) // Observer converts to json
            return state.cities
        },
        getCitiesName(state) {
            // const citiesJSON = JSON.parse(JSON.stringify(state.cities))
            const cities = []
            for (const i of state.cities)
                cities.push(i.name)
            return cities
        }
    },
    state: {
        cities: []
    }
}