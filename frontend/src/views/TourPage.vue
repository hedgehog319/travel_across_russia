<template>
  <div id="tour">
    <v-container>
      <v-card elevation="2" style="padding: 20px">

        <!-- TODO bad icon favorites       -->
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn icon style="position: absolute; right: 15px;" large v-bind="attrs" v-on="on">
              <v-icon large color="#ffd700">mdi-heart-outline</v-icon>
            </v-btn>
          </template>
          <span>В избранное</span>
        </v-tooltip>

        <v-card-title style="font-size: 30px" class="justify-center">Хаятт Ридженси Сочи</v-card-title>

        <v-slide-group class="pa-4" center-active show-arrows>
          <v-slide-item v-for="(image, n) in images" :key="n">
            <v-card class="ma-4" height="200" width="300">
              <v-row class="fill-height" align="center" justify="center">
                <v-scale-transition>
                  <v-img :src='image'/>
                </v-scale-transition>
              </v-row>
            </v-card>
          </v-slide-item>
        </v-slide-group>

        <v-card-text style="margin-left: 25px; width: 95%">
          <v-row align="center" class="mx-0">
            <!--TODO разобраться with rating-->
            <v-rating :value="4.5" color="amber" dense half-increments readonly size="20"/>
            <div class="grey--text ml-4">4.5 (413)</div>
          </v-row>

          <div class="my-4 subtitle-1">Россия, Сочи</div>

          <div>Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного
            проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.
            В отеле предоставляется бесплатный Wi-Fi.
          </div>

        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "TourPage",
  data() {  // TODO remove it
    return {
      images: ['https://cf.bstatic.com/images/hotel/max1280x900/269/269930027.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/186/186135320.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/264/264611854.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/113/113609375.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/255/255641589.jpg',
      ],
    }
  },
}
</script>

<style scoped>

</style>