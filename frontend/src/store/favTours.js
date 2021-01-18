import axios from "axios";

export default {
    actions: {
        async fetchFavTours(ctx, conf) {
            const res = await axios.get('api/fav-tours/', conf)
            ctx.commit('updateFavTours', res.data)
        },
        isFavTour(ctx, id) {
            for (const tour of ctx.state.favTours)
                if (tour.tour === id) return true

            return false
        }
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