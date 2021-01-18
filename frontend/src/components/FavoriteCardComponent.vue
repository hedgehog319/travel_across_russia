<template>
  <v-card class="rounded" :style="isSmall ? 'display: inline-block; margin: 10px': 'display: flex; margin: 10px'">
    <v-img :src="tour.src" class="rounded" height="200px" style="display: block; margin: 10px"
           :width="isSmall ? undefined : 300"/>
    <v-card-text style="height: 100% !important;">
      <div style="margin-bottom: 10px">
        <span style="font-size: 30px; color: black">{{ tour.name }}, {{ tour.country }}</span>
        <v-spacer/>
        <v-btn icon large style="position: absolute; top: 5px; right: 5px" @click="favClick">
          <v-icon v-if="isFavTour(tour.id)" color="#ffd700" large>mdi-heart-outline</v-icon>
          <v-icon v-else color="#ffd700" large>mdi-heart</v-icon>
        </v-btn>
      </div>
      <span style="font-size: 20px; color: #242424; opacity: 0.7; margin-bottom: 10px">{{ tour.description }}</span>
      <div style="display: flex; margin-top: 10px">
        <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20"/>
        <v-spacer/>
        <span style="right: 10px; bottom: 43px; font-size: 25px">
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
          id: Number,
          name: String,
          price: Number,
          country: String,
          src: String,
          description: String,
          rating: Number
        }
      }
    }
  },
  computed: mapGetters(['getFavTours']),
  data() {
    return {
      isSmall: false,
    }
  },
  methods: {
    ...mapActions(['isFavTour']),
    getCost(price) {
      return price.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    onResize() {
      this.isSmall = window.innerWidth < 900
    },
    addFav(conf) {
      this.axios.post('api/fav-tours/', {tour: this.tour.id}, conf)
    },
    removeFav(conf) {
      this.axios.delete(`api/fav-tours/${this.tour.id}/`, conf)
    },
    favClick() {
      if (!this.$cookies.isKey('Token')) return

      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      if (this.isFavTour(this.tour.id())) this.removeFav(conf)
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