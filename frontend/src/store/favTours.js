import axios from "axios";

export default {
    actions: {
        async fetchFavTours(ctx, conf) {
            const res = await axios.get('api/fav-tours/', conf)
            ctx.commit('updateFavTours', res.data)
        },
        removeFavTour(ctx, tour) {
            ctx.commit('removeFavTour', tour)
        }
    },
    mutations: {
        updateFavTours(state, favTours) {
            state.favTours = favTours
        },
        removeFavTour(state, id) {
            let rem
            for (let i = 0; i < state.favTours.length; i++)
                if (state.favTours[i].tour === id) {
                    rem = i
                    break
                }

            if (rem >= 0) {
                state.favTours.splice(rem, 1)
            }
        }
    },
    getters: {
        getFavTours(state) {
            return state.favTours
        },
    },
    state: {
        favTours: []
    }
}