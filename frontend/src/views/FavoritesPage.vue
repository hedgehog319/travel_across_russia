<template>
  <div id="favorites" class="bg-cover">
    <v-container>
      <favorite-card v-for="tour in tours" :key="tour.id" :tour="tour" favorite/>
    </v-container>
  </div>
</template>

<script>
import FavoriteCardComponent from "@/components/FavoriteCardComponent";
import {mapActions} from "vuex";

export default {
  name: "FavoritesPage",
  components: {
    'favorite-card': FavoriteCardComponent
  },
  data: () => ({
    date: null,
    group: null,
    tours: [
      {
        id: 1,
        name: 'Хаятт Ридженси Сочи',
        price: 200000,
        country: "Россия",
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg',
        description: 'Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного\n' +
            '        проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.\n' +
            '        В отеле предоставляется бесплатный Wi-Fi.',
        rating: 4.5,
      },
    ]
  }),
  methods: {
    ...mapActions(['fetchFavTours']),
    currentDate(date) {
      const today = new Date()
      const yesterday = new Date(today.getTime() - 24 * 3600 * 1000)
      return date < yesterday
    }
  },
  created() {
    this.fetchFavTours({headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}})
  }
}
</script>

<style scoped>

</style>