<template>
  <v-card class="rounded" style="display: flex; margin: 10px">
    <v-img :src="tour.src" class="rounded" height="200px" style="display: block; margin: 10px" :width="imgWidth"/>
    <v-card-text style="height: 100% !important;">
      <div>
        <p style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</p>
        <v-spacer/>
        <v-btn icon large style="position: absolute; top: 5px; right: 5px">
          <v-icon v-if="favorite" color="#ffd700" large>mdi-heart</v-icon>
          <v-icon v-else color="#ffd700" large>mdi-heart-outline</v-icon>
        </v-btn>
      </div>
      <p style="font-size: 20px; color: #242424; opacity: 0.7">{{ tour.description }}</p>
      <div style="display: flex">
        <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20"/>
        <v-spacer/>
        <span style="right: 10px; bottom: 43px; font-size: 25px">{{ getCost(tour.cost) }}</span>
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
  methods: {
    getCost(cost) {
      return cost.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    }
  }
}
</script>

<style scoped>

</style>