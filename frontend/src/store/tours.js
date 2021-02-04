import axios from "axios";

export default {
    actions: {
        async fetchTours(ctx, [conf, query]) {
            const res = await axios.get(`api/tours/${query}`, conf)
                .catch(err => console.log(err))
            ctx.commit('updateTours', res.data)
        },
        async fetchTopTours(ctx, count) {
            const res = await axios.get(`api/top-tours/?count=${count}`)
                .catch(err => console.log(err))
            ctx.commit('updateTopTours', res.data)
        },
        removeFavorite(ctx, id) {
            ctx.commit('removeFavorite', id)
        }
    },
    mutations: {
        updateTours(state, tours) {
            state.tours = tours
        },
        updateTopTours(state, tours) {
            state.topTours = tours
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
        getTopTours(state) {
            return state.topTours
        }
    },
    state: {
        tours: [],
        topTours: []
    }
}