<template>
  <v-card class="mx-auto" max-width="344" style="border-radius: 10px">
    <router-link :to="{name: 'tour', query: {id: tour.tour_id}}">
      <v-img :src="tour.photo" height="200px" style="position: relative; border-radius: 10px"/>

      <div style="left: 15px" class="absolute-bottom">
        <v-icon color="#fff">mdi-calendar-clock</v-icon>
        <span class="white--text pl-1">{{ formatDays(tour.count_days) }}</span>
      </div>

      <div style="right: 15px" class="absolute-bottom">
        <span class="white--text text-h5">От {{ getPrice(tour.price) }}</span>
        <v-icon class="white--text text-h5" size="22" style="bottom: 4px">mdi-currency-rub</v-icon>
      </div>
    </router-link>

    <v-card-title class="d-inline-block text-truncate" style="max-width: 100%">
      <router-link :to="{name: 'tour', query: {id: tour.tour_id}}" class="hover text-decoration-none"
                   style="color: rgba(0,0,0,.87)">
        {{ tour.name }}
      </router-link>
    </v-card-title>

    <v-card-subtitle>
      <v-icon color="primary">mdi-map-marker-outline</v-icon>
      <span style="color: #1976d2">{{ tour.country_name }}, {{ tour.city_name }}</span>
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
          tour_id: Number,
          name: String,
          time: String,
          country_name: String,
          city_name: String,
          photo: String,
          description: String,
          rating: Number,
          is_favourite: Boolean,
          count_days: Number,
        }
      }
    }
  },
  methods: {
    getPrice(price) {
      return price.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    formatDays(str) {
      const value = +str % 100;
      const num = +str % 10;
      if(value > 10 && value < 20) return str + ' ночей';
      if(num > 1 && num < 5) return str + ' ночи';
      if(num === 1) return str + ' ночь';
      return str + ' ночей';
    },
  }
}
</script>

<style scoped>

</style>