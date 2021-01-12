<template>
  <v-card class="mx-auto" max-width="344" style="border-radius: 10px">
    <router-link :to="{name: 'tour', query: {id: tour.id}}">
      <v-img style="position: relative; border-radius: 10px" height="200px"
             src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"/>

      <div style="position: absolute; bottom: 110px; left: 15px">
        <v-icon color="#fff">mdi-calendar</v-icon>
        <span style="color: #fff; padding-left: 5px">{{ tour.start }}-{{ tour.end }}</span>
      </div>

      <div style="position: absolute; bottom: 110px; right: 15px">
        <span style="color: #fff; font-size: 25px">От {{ getCost }}</span>
      </div>
    </router-link>

    <v-card-title class="d-inline-block text-truncate" style="max-width: 100%">
      <router-link :to="{name: 'tour', query: {id: tour.id}}" class="hover text-decoration-none"
                   style="color: rgba(0,0,0,.87)">
        {{ tour.title }}
      </router-link>
    </v-card-title>

    <v-card-subtitle>
      <v-icon color="primary">mdi-map-marker-outline</v-icon>
      <span style="color: #1976d2">{{ tour.country }}, {{ tour.city }}</span>
    </v-card-subtitle>

  </v-card>
</template>

<script>
export default {
  name: "TourCardComponent",
  props: {
    tour: {
      required: true,
      type: Object,
      default() {
        return {
          title: String,
          start: Date,
          end: Date,
          country: String,
          city: String,
          cost: Number
        }
      }
    }
  },
  computed: {
    getCost() {
      return this.tour.cost.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    }
  }
}
</script>

<style scoped>

</style>