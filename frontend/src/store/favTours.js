import axios from "axios";

export default {
    actions: {
        async fetchFavTours(ctx, conf) {
            const res = await axios.get('api/fav-tours/', conf)
            ctx.commit('updateFavTours', res.data)
        },
    },
    mutations: {
        updateFavTours(state, favTours) {
            state.favTours = favTours
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