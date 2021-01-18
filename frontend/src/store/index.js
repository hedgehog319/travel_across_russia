import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// import modules
import cities from "@/store/cities";
import favTours from "@/store/favTours";

export default new Vuex.Store({
    modules: {
        cities,
        favTours,
    }
})
