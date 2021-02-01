<template>
  <div id="favorites">
    <v-container>
      <v-skeleton-loader v-if="!isLoad" type="card" class="mx-auto white"/>
      <div v-else-if="isEmpty()">
        <favorite-card  v-for="tour in getFavTours" :key="tour.tour" :tour="tour" favorite/>
      </div>
      <v-card v-else class="ma-auto d-flex flex-column align-center justify-center" height="300" width="600">
        <span class="text-h4 text-center">Ваш список избранного пуст</span>
        <v-btn class="mt-3" :to="{name: 'search'}">Поиск туров</v-btn>
      </v-card>
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
    isLoad: false,
  }),
  computed: mapGetters(['getFavTours']),
  methods: {
    ...mapActions(['fetchFavTours']),
    isEmpty() {
      return this.getFavTours.length > 0
    }
  },
  async created() {
    await this.fetchFavTours({headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}})
    this.isLoad = true
  },
}
</script>

<style scoped>

</style>
