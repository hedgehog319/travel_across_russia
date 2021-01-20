<template>
  <div id="tour">
    <v-container>
      <v-card elevation="2" style="padding: 20px">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" icon large style="position: absolute; top: 10px; right: 12px;">
              <v-icon color="#ffd700" large>mdi-heart-outline</v-icon>
            </v-btn>
          </template>
          <span>В избранное</span>
        </v-tooltip>

        <v-card-title class="justify-center" style="font-size: 30px">Хаятт Ридженси Сочи</v-card-title>

        <v-slide-group center-active class="pa-4" show-arrows>
          <v-slide-item v-for="(image, n) in images" :key="n">
            <v-card class="ma-4" height="200" width="300">
              <v-row align="center" class="fill-height" justify="center">
                <v-scale-transition>
                  <v-img :src='image'/>
                </v-scale-transition>
              </v-row>
            </v-card>
          </v-slide-item>
        </v-slide-group>

        <v-card-text style="margin-left: 25px; width: 95%">
          <v-row align="center" class="mx-0">
            <!--TODO разобраться with rating if auth -->
            <v-rating :value="0" color="amber" hover dense half-increments size="25"/>
            <v-spacer/>
            <div style="font-weight: 500; font-size: 15px; color: black">
              <v-chip>Продолжительность: 20 дней</v-chip>
            </div>
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