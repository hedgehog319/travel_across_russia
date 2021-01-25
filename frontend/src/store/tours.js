import axios from "axios";

export default {
    actions: {
        async fetchTours(ctx, [conf, query]) {
            const res = await axios.get(`api/tours/${query}`, conf)
            ctx.commit('updateTours', res.data)
        },
        // TODO первые 12 туров
        async fetchBestTours(ctx) {
            const res = await axios.get('api/tours/')
            ctx.commit('updateBestTours', res.data)
        },
        removeFavorite(ctx, id) {
            ctx.commit('removeFavorite', id)
        }
    },
    mutations: {
        updateTours(state, tours) {
            state.tours = tours
        },
        updateBestTours(state, tours) {
            state.bestTours = tours
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
        },
        getBestTours(state) {
            return state.bestTours
        }
    },
    state: {
        tours: [],
        bestTours: []
    }
}