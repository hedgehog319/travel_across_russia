<template>
  <v-card class="rounded" :style="isSmall
                                  ? 'display: inline-block; margin-bottom: 8px'
                                  : 'display: flex; margin-bottom: 8px'">
    <v-img src="https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg" height="200px"
           class="d-block rounded ma-2" :width="isSmall ? undefined : 300"/>
    <v-card-text class="d-flex flex-column justify-md-space-around">
      <div>
        <span class="text-h4 black--text">{{ tour.name }}, {{ tour.country }}</span>
        <v-spacer/>
        <v-btn icon large class="v-btn--absolute" style="top: 5px; right: 5px" @click="favClick">
          <v-icon v-if="tour.is_favourite || favorite" color="#ffd700" large>mdi-heart</v-icon>
          <v-icon v-else color="#ffd700" large>mdi-heart-outline</v-icon>
        </v-btn>
      </div>
      <span class="mb-2 text--secondary text-h6 grey--text">{{ tour.description }}</span>
      <div class="d-flex">
        <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20"/>
        <v-spacer/>
        <span style="font-size: 25px">
          {{ getCost(tour.price) }}
          <v-icon size="22">mdi-currency-rub</v-icon>
        </span>
      </div>
    </v-card-text>
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
          tour: Number,
          name: String,
          price: Number,
          country: String,
          src: String,
          description: String,
          rating: Number,
          is_favourite: Boolean
        }
      }
    },
    favorite: Boolean,
  },
  computed: mapGetters(['getFavTours']),
  data() {
    return {
      isSmall: false,
    }
  },
  methods: {
    ...mapActions(['removeFavTour']),
    getCost(price) {
      return price.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    onResize() {
      this.isSmall = window.innerWidth < 900
    },
    addFav(conf) {
      console.log(this.tour.tour)
      this.axios.post('api/fav-tours/', {tour: this.tour.tour}, conf)
      this.tour.is_favourite = true
    },
    removeFav(conf) {
      this.axios.delete(`api/fav-tours/${this.tour.tour}/`, conf)
      this.removeFavTour(this.tour.tour)
    },
    favClick() {
      if (!this.$cookies.isKey('Token')) return

      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      console.log(this.favorite + ' ' + this.tour.is_favourite)
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