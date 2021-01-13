<template>
  <v-app id="tour-booking">
    <v-container>
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1">Выбор тура</v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step :complete="e1 > 2" step="2">Заполнение документов</v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="3">Оплата тура</v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <v-card class="mb-12" color="grey lighten-1" height="200px">

            </v-card>
            <v-btn color="primary" @click="e1 = 2" style="margin-right: 5px;">Далее</v-btn>
            <v-btn text @click="e1 = 1">Отмена</v-btn>
          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card class="mb-12" color="grey lighten-1" height="200px">

            </v-card>
              <v-btn style="margin-right: 5px;" color="primary" @click="e1 = 3">Далее</v-btn>
              <v-spacer></v-spacer>
              <v-btn text @click="e1 = 1">Отмена</v-btn>
          </v-stepper-content>

          <v-stepper-content step="3">
            <v-card class="mb-12" color="grey lighten-1" height="200px">

            </v-card>
            <v-btn style="margin-right: 5px;" color="primary" @click="e1 = 1">Далее</v-btn>
            <v-btn text @click="e1 = 1">Отмена</v-btn>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "TourBooking",
  data () {
    return {
      e1: 1,
    }
  },
}
</script>

<style scoped>

</style>