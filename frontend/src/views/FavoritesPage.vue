<template>
  <div id="favorites">
    <v-container>
      <favorite-card v-for="(tour, i) in tours" :key="i" :tour="tour" favorite/>
    </v-container>
  </div>

</template>

<script>
import FavoriteCardComponent from "@/components/FavoriteCardComponent";

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
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg',
        title: 'Хаятт Ридженси Сочи',
        country: "Россия",
        description: 'Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного\n' +
            '        проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.\n' +
            '        В отеле предоставляется бесплатный Wi-Fi.',
        rating: 4.5,
        cost: 200000
      },
    ]
  }),
  methods: {
    currentDate(date) {
      const today = new Date()
      const yesterday = new Date(today.getTime() - 24 * 3600 * 1000)
      return date < yesterday
    }
  },
}
</script>

<style scoped>

</style>