<template>
  <div id="search">
    <v-container>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <span class="text-h6">Критерии поиска</span>
          </v-expansion-panel-header>

          <v-expansion-panel-content>
            <v-container class="d-flex">
              <v-list width="100%">
                <v-list-item>
                  <v-row class="mb-1">
                    <v-col cols="12" md="4">
                      <v-autocomplete v-model="queries.from" :items="getCitiesName" dense filled label="Откуда"/>
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-autocomplete v-model="queries.to" :items="getCitiesName" dense filled label="Куда"/>
                    </v-col>

                    <v-col cols="12" md="4">
                      <section class="mr-3 mt-n2">
                        <span>Выбрать дату</span>
                        <date-picker :disabled-date="currentDate" v-model="queries.date" confirm range
                                     style="width: 100%"/>
                      </section>
                    </v-col>
                  </v-row>
                </v-list-item>
                <v-list-item>
                  <v-row>
                    <v-col cols="12" md="4" class="text-center">
                      <span class="text-h6">Рейтинг отеля</span>
                      <v-rating class="mt-2" v-model="queries.rating" color="amber" dense half-increments size="30"/>
                    </v-col>
                    <v-col cols="12" md="4">
                      <span class="text-subtitle-1">Цена тура: {{ getCost(rangePrice[0]) }} - {{
                          getCost(rangePrice[1])
                        }}</span>
                      <v-range-slider step="5000" class="mt-5" v-model="rangePrice" max="500000" min="0"/>
                    </v-col>
                    <v-col cols="12" md="4" class="text-center">
                      <span class="text-h6">Тип питания</span>
                      <div class="d-flex">
                        <v-tooltip bottom v-for="(type, i) in typesOfFood" :key="i">
                          <template v-slot:activator="{ on }">
                            <div v-on="on" class="ma-auto">
                              <v-checkbox style="max-height: 30px" :ripple="false" :label="type.short"
                                          :value="type.short" v-model="queries.foodTypes"/>
                            </div>
                          </template>
                          <span>{{ type.full }}</span>
                        </v-tooltip>
                      </div>
                    </v-col>
                  </v-row>
                </v-list-item>
                <v-list-item class="mt-3">
                  <v-row>
                    <v-btn class="ma-auto" width="200" @click="searchTours">Поиск</v-btn>
                  </v-row>
                </v-list-item>
              </v-list>
            </v-container>
          </v-expansion-panel-content>

        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>

    <v-container>
      <v-skeleton-loader v-if="!isLoad" type="card" height="300" class="mx-auto white"></v-skeleton-loader>
      <div v-else-if="isEmpty()">
        <favorite-card v-for="tour in getTours" :key="tour.tour" :tour="tour"/>
      </div>
      <v-card v-else class="ma-auto d-flex flex-column align-center justify-center grey lighten-2" height="300">
        <span class="text-h4 text-center">К сожалению, по вашему запросу ничего не найдено. Проверьте правильность
          ввода или попробуйте изменить запрос.</span>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import DatePicker from "vue2-datepicker";
import FavoriteCardComponent from "@/components/FavoriteCardComponent";
import {mapActions, mapGetters} from "vuex";

export default {
  name: "SearchPage",
  components: {
    DatePicker,
    'favorite-card': FavoriteCardComponent
  },
  data: () => ({
    typesOfFood: [{short: 'RO', full: 'Без питания'},
      {short: 'BB', full: 'Только завтраки'},
      {short: 'HB', full: 'Завтрак и ужин'},
      {short: 'FB', full: 'Завтрак, обед и ужин'},
      {short: 'AI', full: 'Всё включено'}
    ],
    queries: {
      from: null,
      to: null,
      rating: null,
      foodTypes: [],
      date: [],
    },
    rangePrice: [0, 100000],
    isLoad: false,
    isSmall: false,
    isMobile: false,
    trip: {
      name: '',
      location: null,
      start: null,
      end: null,
    },
  }),
  computed: mapGetters(['getCitiesName', 'getTours']),
  methods: {
    ...mapActions(['fetchTours']),
    currentDate(date) {
      return date < new Date((new Date()).getTime() - 24 * 3600 * 1000)
    },
    onResize() {
      this.isMobile = window.innerWidth < 500
      this.isSmall = window.innerWidth < 900
    },
    getCost(cost) {
      return cost.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    async searchTours() {
      this.isLoad = false
      let query = '?'

      if (this.queries.to !== null) query += 'city=' + this.queries.to
      if (this.queries.date.length > 0) {
        query += '&count_days=' + Math.round((this.queries.date[1] - this.queries.date[0]) / (24 * 3600 * 1000))
      }
      if (this.queries.rating !== null) query += '&rating=' + this.queries.rating * 2
      if (this.rangePrice.length !== undefined) query += '&price=' + this.rangePrice[0] + ',' + this.rangePrice[1]
      if (this.queries.foodTypes.length > 0) query += '&type_food=' + this.queries.foodTypes.join(',')

      let conf
      if (this.$cookies.isKey('Token'))
        conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}

      await this.fetchTours([conf, query])
      this.isLoad = true
    },
    isEmpty() {
      return this.getTours.length > 0;
    }
  },
  beforeDestroy() {
    if (typeof window === 'undefined') return

    window.removeEventListener('resize', this.onResize, {passive: true})
  },
  async mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
    let query = '?'

    if (this.$route.query.from !== undefined) this.queries.from = this.$route.query.from
    if (this.$route.query.to !== undefined) {
      this.queries.to = this.$route.query.to
      query += 'city=' + this.queries.to
    }
    if (this.$route.query.startDate !== undefined) {
      this.queries.date.push(new Date(this.$route.query.startDate.toString()))

      if (this.$route.query.endDate !== undefined) this.date.push(new Date(this.$route.query.endDate.toString()))
      else this.queries.date.push(new Date(this.$route.query.startDate.toString()))

      query += '&count_days=' + Math.round((this.queries.date[1] - this.queries.date[0]) / (24 * 3600 * 1000))
    }

    let conf
    if (this.$cookies.isKey('Token'))
      conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}

    await this.fetchTours([conf, query])
    this.isLoad = true
  },
}
</script>

<style scoped>

</style>