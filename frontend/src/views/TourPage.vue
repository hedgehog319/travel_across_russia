<template>
  <div id="tour">
    <v-container>
      <v-skeleton-loader v-if="!isLoad" class="mx-auto white" type="card" height="500"/>

      <v-card v-else elevation="2" class="pa-5">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" icon large class="top-absolute" style="right: 12px;" @click="favClick">
              <v-icon v-if="tour.is_favourite" color="#ffd700" large>mdi-heart</v-icon>
              <v-icon v-else color="#ffd700" large>mdi-heart-outline</v-icon>
            </v-btn>
          </template>
          <span>В избранное</span>
        </v-tooltip>

        <router-link class="text-decoration-none hover" :to="{name: 'booking', query: {id: tour.tour_id}}">
          <v-btn elevation="1" large class="top-absolute" style="right: 60px;">
            <span>Купить тур</span>
            <v-icon color="black" large>mdi-book</v-icon>
          </v-btn>
        </router-link>

        <v-card-title class="justify-center mt-5 text-h4 ">{{ tour.name }}</v-card-title>

        <v-slide-group center-active class="pa-4" show-arrows>
          <v-slide-item v-for="(image, n) in images" :key="n">
            <div class="ma-4" style="height: 200px; width: 300px">
              <v-row align="center" class="fill-height" justify="center">
                <v-scale-transition>
                  <v-img contain :src='image.photo'/>
                </v-scale-transition>
              </v-row>
            </div>
          </v-slide-item>
        </v-slide-group>

        <v-card-text class="ml-6" style="width: 95%">
          <v-row align="center" class="mx-0">
            <!--TODO разобраться with rating if auth -->
            <v-rating v-model="tour.rating" color="amber" :readonly="!isAuthorized" hover dense half-increments
                      size="25" @input="rating"/>

            <v-spacer/>

            <div class="text-h5 text--black">
              <v-chip class="mr-1">Продолжительность: {{ formatDays(tour.count_days) }}</v-chip>
              <v-chip>Питание: {{ tour.food_type }}</v-chip>
            </div>
          </v-row>

          <div class="my-4 subtitle-1">{{ tour.country_name }}, {{ tour.city_name }}</div>

          <div>{{ tour.description }}</div>

        </v-card-text>
      </v-card>
    </v-container>

    <v-snackbar top v-model="isRated">Спасибо за ваш отзыв!</v-snackbar>
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
        food_type: String,
        photo: String,
        description: String,
        rating: Number,
        is_favourite: Boolean,
        count_days: Number,
      },
      images: [],
      isLoad: false,
      isRated: false,
    }
  },
  computed: {
    isAuthorized() {
      return this.$cookies.isKey('Token')
    },
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
    },
    rating() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      const data = {
        tour_id: this.tour.tour_id,
        rating: this.tour.rating * 2
      }

      this.axios.post('api/rating-tours/', data, conf)
          .then(res => {
            if (res.statusText === 'Created')
              this.isRated = true
          })
          .catch(err => console.log(err.response))
    },
    formatDays(str) {
      const value = +str % 100;
      const num = +str % 10;
      if(value > 10 && value < 20) return str + ' ночей';
      if(num > 1 && num < 5) return str + ' ночи';
      if(num === 1) return str + ' ночь';
      return str + ' ночей';
    },
  },
  async created() {
    let conf = undefined
    if (this.$cookies.isKey("Token"))
      conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
    await this.axios.get(`api/tours/?tour_id=${this.$route.query.id}`, conf)
        .then(resp => {
          if (resp.data.length > 0) {
            this.tour = resp.data[0]
            this.isLoad = true
          } else {
            this.$router.push({name: 'notfound'})
          }
        })
        .catch(err => {
          console.log(err)
        })

    await this.axios.get(`api/hotel-photos/?tour_id=${this.tour.tour_id}`)
        .then(res => {
          if (res.statusText === 'OK') {
            this.images = res.data
          }
        })
        .catch(err => console.log(err))
  }
}
</script>

<style scoped>
</style>