<template>
  <div id="tour">
    <v-container v-if="!isLoad">
      <v-skeleton-loader class="mx-auto white" type="card" height="500"/>
    </v-container>
    <v-container v-if="isLoad">
      <v-card elevation="2" class="pa-5">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" icon large style="position: absolute; top: 10px; right: 12px;" @click="favClick">
              <v-icon v-if="tour.is_favourite" color="#ffd700" large>mdi-heart</v-icon>
              <v-icon v-else color="#ffd700" large>mdi-heart-outline</v-icon>
            </v-btn>
          </template>
          <span>В избранное</span>
        </v-tooltip>
        <router-link class="text-decoration-none hover" :to="{name: 'booking', query: {id: tour.tour_id}}">
          <v-btn elevation="1" large style="position: absolute; top: 10px; right: 60px;">
            <span>Купить тур</span>
            <v-icon color="black" large>mdi-book</v-icon>
          </v-btn>
        </router-link>

        <v-card-title class="justify-center mt-4" style="font-size: 30px">{{ tour.name }}</v-card-title>

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

        <v-card-text class="ml-6" style="width: 95%">
          <v-row align="center" class="mx-0">
            <!--TODO разобраться with rating if auth -->
            <v-rating :value="tour.rating" color="amber" :readonly="!isAuthorized" hover dense half-increments
                      size="25"/>
            <v-spacer/>
            <div style="font-weight: 500; font-size: 15px; color: black">
              <v-chip>Продолжительность: {{ tour.count_days }} дней</v-chip>
            </div>
          </v-row>

          <div class="my-4 subtitle-1">{{ tour.country_name }}, {{ tour.city_name }}</div>

          <div>{{ tour.description }}</div>

        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "TourPage",
  data() {
    return {
      tour: {
        tour_id: Number,
        name: String,
        time: String,
        country_name: String,
        city_name: String,
        src: String,
        description: String,
        rating: Number,
        is_favourite: Boolean,
        count_days: Number,
      },
      images: ['https://cf.bstatic.com/images/hotel/max1280x900/269/269930027.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/186/186135320.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/264/264611854.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/113/113609375.jpg',
        'https://cf.bstatic.com/images/hotel/max1280x900/255/255641589.jpg',
      ],
      isLoad: false,
    }
  },
  computed: {
    isAuthorized() {
      return this.$cookies.isKey('Token')
    }
  },
  methods: {
    ...mapActions(['removeFavTour', 'removeFavorite']),
    addFav(conf) {
      this.axios.post('api/fav-tours/', {tour: this.tour.tour_id}, conf)
      this.tour.is_favourite = true
    },
    removeFav(conf) {
      this.axios.delete(`api/fav-tours/${this.tour.tour_id}/`, conf)
      this.removeFavTour(this.tour.tour_id)
      this.removeFavorite(this.tour.tour_id)
      this.tour.is_favourite = false
    },
    favClick() {
      if (!this.$cookies.isKey('Token')) {
        this.favFail = true
        return
      }

      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      if (this.favorite || this.tour.is_favourite) this.removeFav(conf)
      else this.addFav(conf)
    }
  },
  created() {
    let conf = undefined
    if (this.$cookies.isKey("Token"))
      conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
    this.axios.get(`api/tours/?tour_id=${this.$route.query.id}`, conf)
        .then(resp => {
          if (resp.data.length > 0) {
            this.isLoad = true
            this.tour.tour_id = resp.data[0].tour_id
            this.tour.name = resp.data[0].name
            this.tour.country_name = resp.data[0].country_name
            this.tour.city_name = resp.data[0].city_name
            this.tour.description = resp.data[0].description
            this.tour.is_favourite = resp.data[0].is_favourite
            this.tour.rating = resp.data[0].rating
            this.tour.count_days = resp.data[0].count_days
          } else {
            this.$router.push({name: 'notfound'})
          }
        })
        .catch(err => {
          console.log(err)
        })
  }
}
</script>

<style scoped>

</style>