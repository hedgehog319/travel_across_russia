<template>
  <v-card class="rounded" :style="isSmall ? 'display: inline-block; margin: 10px': 'display: flex; margin: 10px'">
    <v-img :src="tour.src" class="rounded" height="200px" style="display: block; margin: 10px"
           :width="isSmall ? undefined : 300"/>
    <v-card-text style="height: 100% !important;">
      <div style="margin-bottom: 10px">
        <span style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</span>
        <v-spacer/>
        <v-btn icon large style="position: absolute; top: 5px; right: 5px">
          <v-icon v-if="favorite" color="#ffd700" large>mdi-heart</v-icon>
          <v-icon v-else color="#ffd700" large>mdi-heart-outline</v-icon>
        </v-btn>
      </div>
      <span style="font-size: 20px; color: #242424; opacity: 0.7; margin-bottom: 10px">{{ tour.description }}</span>
      <div style="display: flex; margin-top: 10px">
        <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20"/>
        <v-spacer/>
        <span style="right: 10px; bottom: 43px; font-size: 25px">
          {{ getCost(tour.cost) }}
          <v-icon size="22">mdi-currency-rub</v-icon>
        </span>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "FavoriteCardComponent",
  props: {
    tour: {
      required: true,
      type: Object,
      default() {
        return {
          src: String,
          title: String,
          country: String,
          description: String,
          cost: Number,
          rating: Number
        }
      }
    },
    imgWidth: {
      type: Number,
    },
    favorite: Boolean
  },
  data() {
    return {
      isSmall: false,
    }
  },
  methods: {
    getCost(cost) {
      return cost.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    onResize() {
      this.isSmall = window.innerWidth < 900
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