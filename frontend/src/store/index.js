import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// import modules
import cities from "@/store/cities";
import favTours from "@/store/favTours";
import tours from "@/store/tours";

export default new Vuex.Store({
    modules: {
        cities,
        favTours,
        tours,
    }
})
