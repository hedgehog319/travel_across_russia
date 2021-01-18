import axios from "axios";

export default {
    actions: {
        async fetchTours(ctx, conf) {
            const res = await axios.get('api/tours/', conf)
            ctx.commit('updateTours', res.data)
        }
    },
    mutations: {
        updateTours(state, tours) {
            state.tours = tours
        }
    },
    getters: {
        getTours(state) {
            return state.tours
        }
    },
    state: {
        tours: []
    }
}