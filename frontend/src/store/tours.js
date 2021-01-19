import axios from "axios";

export default {
    actions: {
        async fetchTours(ctx, conf) {
            const res = await axios.get('api/tours/', conf)
            ctx.commit('updateTours', res.data)
        },
        removeFavorite(ctx, id) {
            ctx.commit('removeFavorite', id)
        }
    },
    mutations: {
        updateTours(state, tours) {
            state.tours = tours
        },
        removeFavorite(state, id) {
            for (let i = 0; i < state.tours.length; i++) {
                if (state.tours[i].tour_id === id) {
                    state.tours[i].is_favourite = false
                    break
                }
            }
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