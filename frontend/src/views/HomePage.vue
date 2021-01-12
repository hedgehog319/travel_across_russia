<template>
  <div id="home">
    <v-container style="background-color: #fff; padding: 5px; width: 72%" class="round">
      <div class="text-center" style="font-size: 30px; font-weight: 500;">Лучшие предложения туров</div>

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
        days: "21",
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