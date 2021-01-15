<template>
  <div id="favorites">
    <v-container>

      <v-card v-if="isSmall" v-for="(tour, i) in tours" :key="i" class="rounded" style="margin: 10px; padding-top: 10px">
        <v-img v-if="isMobile" :src="tour.src" class="rounded" height="200px" style="margin: 0 10px 10px 10px"/>
        <v-card-text style="height: 100% !important;">
          <div>
            <span style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</span>
            <v-spacer/>
            <v-btn icon large style="position: absolute; bottom: 3px; right: 0">
              <v-icon color="#ffd700" large>mdi-heart</v-icon>
            </v-btn>
          </div>
          <p style="font-size: 20px; color: #242424; opacity: 0.7">
            Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного
            проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.
            В отеле предоставляется бесплатный Wi-Fi.
          </p>
          <v-rating :value="4.5" color="amber" dense half-increments readonly size="20"/>
        </v-card-text>
      </v-card>

      <v-card v-if="!isSmall" v-for="(tour, i) in tours" :key="i" class="rounded" style="display: flex;margin: 10px">
        <v-img :src="tour.src" class="rounded" height="200px" style="display: block;margin: 10px" width="300px"/>
        <v-card-text style="height: 100% !important;">
          <div>
            <p style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</p>
            <v-spacer/>
            <v-btn icon large style="position: absolute; top: 3px; right: 0">
              <v-icon color="#ffd700" large>mdi-heart</v-icon>
            </v-btn>
          </div>
          <p style="font-size: 20px; color: #242424; opacity: 0.7">
            Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного
            проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.
            В отеле предоставляется бесплатный Wi-Fi.
          </p>
          <v-rating :value="4.5" color="amber" dense half-increments readonly size="20"/>
        </v-card-text>
      </v-card>
    </v-container>
  </div>

</template>

<script>
export default {
  name: "FavoritesPage",
  data: () => ({
    isMobile: false,
    isSmall: false,
    date: null,
    group: null,
    tours: [
      {
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg', title: 'Хаятт Ридженси Сочи',
        country: "Россия"
      },
      {
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg', title: 'Хаятт Ридженси Сочи',
        country: "Россия"
      }
    ]
  }),
  beforeDestroy() {
    if (typeof window === 'undefined') return

    window.removeEventListener('resize', this.onResize, {passive: true})
  },

  mounted() {
    this.onResize()

    window.addEventListener('resize', this.onResize, {passive: true})
  },
  methods: {
    currentDate(date) {
      const today = new Date()
      const yesterday = new Date(today.getTime() - 24 * 3600 * 1000)
      return date < yesterday
    },
    onResize() {
      this.isMobile = window.innerWidth < 500
      this.isSmall = window.innerWidth < 900
    }
  },
}
</script>

<style scoped>

</style>