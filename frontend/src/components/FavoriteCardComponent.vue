<template>
  <v-card class="rounded">
    <v-img :src="tour.src" class="rounded" height="200px" style="display: block; margin: 10px" :width="imgWidth"/>
    <v-card-text style="height: 100% !important;">
      <div>
        <p style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</p>
        <v-spacer/>
        <v-btn icon large style="position: absolute; top: 3px; right: 0">
          <v-icon color="#ffd700" large>mdi-heart</v-icon>
        </v-btn>
      </div>
      <p style="font-size: 20px; color: #242424; opacity: 0.7">{{ tour.description }}</p>
      <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20"/>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "FavoriteCardComponent",
  props: {
    tour: {
      src: String,
      title: String,
      country: String,
      description: String,
      rating: Number
    },
    imgWidth: {
      type: Number,
    }
  }
}
</script>

<style scoped>

</style>