import axios from "axios";

export default {
    actions: {
        async fetchFavTours(ctx, conf) {
            const res = await axios.get('api/fav-tours/', conf)
                .catch(err => console.log(err))
            ctx.commit('updateFavTours', res.data)
        },
        removeFavTour(ctx, id) {
            ctx.commit('removeFavTour', id)
        }
    },
    mutations: {
        updateFavTours(state, favTours) {
            state.favTours = favTours
        },
        removeFavTour(state, id) {
            let rem = -1
            for (let i = 0; i < state.favTours.length; i++) {
                if (state.favTours[i].tour_id === id) {
                    rem = i
                    break
                }
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