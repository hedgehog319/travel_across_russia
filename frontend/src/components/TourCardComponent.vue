<template>
  <v-card class="mx-auto bor-rad-10 round" max-width="344">
    <router-link :to="{name: 'tour', query: {id: tour.tour_id}}">
      <v-img :src="tour.photo" height="200px" class="bor-rad-10" style="position: relative"/>

      <div style="left: 10px; bottom: 130px; position: absolute;" class="rounded pa-1 bg-height-40">
        <v-icon color="#fff">mdi-calendar-clock</v-icon>
        <span class="white--text pl-1 text-subtitle-1">{{ formatDays(tour.count_days) }}</span>
      </div>

      <div style="right: 10px; bottom: 130px; position: absolute;" class="rounded pa-1 bg-height-40">
        <span class="white--text text-h4">От {{ getPrice(tour.price) }}</span>
        <v-icon class="white--text text-h5" size="22" style="bottom: 4px">
          mdi-currency-rub
        </v-icon>
      </div>
    </router-link>

    <v-card-title class="d-inline-block text-truncate" style="max-width: 100%">
      <router-link :to="{name: 'tour', query: {id: tour.tour_id}}" class="hover text-decoration-none"
                   style="color: rgba(0,0,0,.87)">
        {{ tour.name }}
      </router-link>
    </v-card-title>

    <v-card-subtitle>
      <v-rating :value="tour.rating" color="amber" dense half-increments readonly size="20" class="pb-1"/>
      <v-spacer/>
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
      if (value > 10 && value < 20) return str + ' ночей';
      if (num > 1 && num < 5) return str + ' ночи';
      if (num === 1) return str + ' ночь';
      return str + ' ночей';
    },
  }
}
</script>

<style scoped>
.bor-rad-10 {
  border-radius: 10px
}

.bg-height-40 {
  background-color: rgba(0, 0, 0, 0.4);
  height: 40px
}

</style>
