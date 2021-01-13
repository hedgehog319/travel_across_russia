<template>
  <div id="favorites">
    <v-container>
      <v-card style="display: flex;margin: 10px" v-for="tour in tours" class="rounded">
          <v-img style="margin: 10px" class="rounded" height="200px" width="300px" :src="tour.src"/>
          <v-card-text style="height: 100% !important;">
            <div>
              <p style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</p>
              <v-spacer/>
              <v-btn icon  large v-bind="attrs" v-on="on" style="position: absolute; top: 3px; right: 0">
                <v-icon large color="#ffd700">mdi-heart</v-icon>
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

}
</script>

<style scoped>

</style>