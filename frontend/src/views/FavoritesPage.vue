<template>
  <div id="favorites">
    <v-container>
      <favorite-card v-for="tour in getFavTours" :key="tour.tour" :tour="tour" favorite/>
    </v-container>
  </div>
</template>

<script>
import FavoriteCardComponent from "@/components/FavoriteCardComponent";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "FavoritesPage",
  components: {
    'favorite-card': FavoriteCardComponent
  },
  data: () => ({
    date: null,
    group: null,
  }),
  computed: mapGetters(['getFavTours']),
  methods: mapActions(['fetchFavTours']),
  created() {
    this.fetchFavTours({headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}})
  }
}
</script>

<style scoped>

</style>