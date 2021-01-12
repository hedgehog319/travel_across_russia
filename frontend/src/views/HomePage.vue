<template>
  <div id="home">
    <v-container style="background-color: #fff; padding: 5px; width: 72%" class="round">
      <span>Лучшие предложения туров</span>

      <v-row no-gutters v-for="n in 2" :key="n" style="margin-bottom: 10px; margin-top: 10px">
        <v-col v-for="n in 3" :key="n" cols="4" sm="4" md="4" align-self="center">
          <tour-card :tour="tour"/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import TourCardComponent from "@/components/TourCardComponent";

export default {
  name: "HomePage",
  components: {
    'tour-card': TourCardComponent,
  },
  data() {
    return {
      tour: {
        title: "Море не помеха!",
        id: 0,
        start: "21.01",
        end: "25.01",
        country: "Россия",
        city: "Владивосток",
        cost: 200000
      },
    }
  }
}
</script>

<style scoped>

</style>