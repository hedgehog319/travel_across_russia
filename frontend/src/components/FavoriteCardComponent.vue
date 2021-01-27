<template>
  <v-card class="rounded unselectable" :style="isSmall
                                  ? 'display: inline-block; margin-bottom: 8px'
                                  : 'display: flex; margin-bottom: 8px'">
    <router-link class="text-decoration-none" :to="{name: 'tour', query: {id: tour.tour_id}}">
      <v-img :src="tour.photo" height="200px"
             class="d-block rounded ma-2 hover" :width="isSmall ? undefined : 300"/>
    </router-link>
    <v-card-text class="d-flex flex-column justify-md-space-around" :style="isSmall ? '' : 'max-width: 65%'">
      <div>
        <router-link class="text-decoration-none hover" :to="{name: 'tour', query: {id: tour.tour_id}}">
          <span class="text-h4 black--text">{{ tour.name }}, {{ tour.country_name }}</span>
        </router-link>
        <v-spacer/>
        <v-btn icon large class="v-btn--absolute" style="top: 5px; right: 5px" @click="favClick">
          <v-icon v-if="tour.is_favourite || favorite" color="#ffd700" large>mdi-heart</v-icon>
          <v-icon v-else color="#ffd700" large>mdi-heart-outline</v-icon>
        </v-btn>
      </div>
      <div class="mb-2 text--secondary text-h6 grey--text">
        <span>{{ divideDescription(tour.description) }}</span>
      </div>
      <div class="d-flex">
        <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20"/>
        <v-spacer/>
        <span style="font-size: 21px">
          Тип питания: {{ tour.food_type }}
        </span>
        <v-spacer/>
        <span style="font-size: 25px">
          {{ getCost(tour.price) }}
          <v-icon size="22">mdi-currency-rub</v-icon>
        </span>
      </div>
    </v-card-text>


    <v-snackbar top v-model="favFail">Чтобы добавить тур в избранное, необходимо войти в аккаунт</v-snackbar>
  </v-card>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "FavoriteCardComponent",
  props: {
    tour: {
      required: true,
      type: Object,
      default() {
        return {
          tour_id: Number,
          name: String,
          price: Number,
          country_name: String,
          city_name: String,
          food_type: String,
          photo: String,
          description: String,
          rating: Number,
          is_favourite: Boolean,
        }
      }
    },
    favorite: Boolean,
  },
  computed: mapGetters(['getFavTours']),
  data() {
    return {
      isSmall: false,
      favFail: false,
    }
  },
  methods: {
    divideDescription(str) {
      if (str.length > 250)
        return str.slice(0, 250) + '...'
      return str
    },
    ...mapActions(['removeFavTour', 'removeFavorite']),
    getCost(price) {
      return price.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    onResize() {
      this.isSmall = window.innerWidth < 900
    },
    addFav(conf) {
      this.axios.post('api/fav-tours/', {tour_id: this.tour.tour_id}, conf)
          .catch(err => console.log(err.response))
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
  beforeDestroy() {
    if (typeof window === undefined) return
    window.removeEventListener('resize', this.onResize, {passive: true})
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
  },
}
</script>

<style scoped>

</style>