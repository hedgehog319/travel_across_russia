import axios from "axios";

export default {
    actions: {
        async fetchFoodTypes(ctx) {
            const res = await axios.get('api/hotels/food-types/')
                .catch(err => console.log(err))
            ctx.commit('updateFoodTypes', res.data)
        }
    },
    mutations: {
        updateFoodTypes(state, foodTypes) {
            state.foodTypes = foodTypes
        }
    },
    getters: {
        getFoodTypes(state) {
            const types = []
            for (const [short, full] of Object.entries(state.foodTypes))
                types.push({short: short, full: full})

            return types
        },
        getFoodType: state => id => {
            return state.foodTypes[id] || undefined
        },
        // name: state => attrs => {} - передача атрибутов в getter
    },
    state: {
        foodTypes: {}
    }
}