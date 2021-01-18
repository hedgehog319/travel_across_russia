<template>
  <div id="search">
    <v-container>
      <v-expansion-panels>
        <v-expansion-panel>
          <v-expansion-panel-header>
            <span class="text-h6">Критерии поиска</span>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-container style="display: flex">
              <v-list width="100%">
                <v-list-item>
                  <v-row style="margin-bottom: 5px">
                    <v-col cols="12" md="4">
                      <v-autocomplete v-model="from" :items="getCitiesName" dense filled
                                      label="Откуда"></v-autocomplete>
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-autocomplete v-model="to" :items="getCitiesName" dense filled label="Куда"></v-autocomplete>
                    </v-col>

                    <v-col cols="12" md="4">
                      <section style="margin-top: -6px; margin-right: 10px">
                        <span>Выбрать дату</span>
                        <date-picker :disabled-date="currentDate" v-model="date" confirm range
                                     style="width: 100%"/>
                      </section>
                    </v-col>
                  </v-row>
                </v-list-item>
                <v-list-item>
                  <v-row>
                    <v-col cols="12" md="4" class="text-center">
                      <span class="text-h6">Рейтинг отеля</span>
                      <v-rating style="margin-top: 10px" :value="4.5" color="amber" dense half-increments size="30"/>
                    </v-col>
                    <v-col cols="12" md="4">
                      <span class="text-subtitle-1">Цена тура: {{ getCost(price[0]) }} - {{ getCost(price[1]) }} </span>
                      <v-range-slider step="5000" style="margin-top: 20px" v-model="price" max="500000" min="0"/>
                    </v-col>
                    <v-col cols="12" md="4" class="text-center">
                      <span class="text-h6">Тип питания</span>
                      <v-radio-group row v-model="typeOfFood">
                        <v-tooltip bottom v-for="(type, i) in typesOfFood" :key="i">
                          <template v-slot:activator="{ on, attrs }">
                            <v-radio style="margin: auto" v-on="on" v-bind="attrs" :label="type.short" :value="i"/>
                          </template>
                          <span>{{ type.full }}</span>
                        </v-tooltip>
                      </v-radio-group>
                    </v-col>
                  </v-row>
                </v-list-item>
              </v-list>
            </v-container>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>


    <v-container>
      <favorite-card v-for="tour in tours" :key="tour.id" :tour="tour"/>
    </v-container>
  </div>
</template>

<script>
import DatePicker from "vue2-datepicker";
import FavoriteCardComponent from "@/components/FavoriteCardComponent";
import {mapGetters} from "vuex";

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
    typeOfFood: 1,
    price: [0, 100000],
    isSmall: false,
    isMobile: false,
    from: null,
    to: null,
    time: null,
    date: [],
    trip: {
      name: '',
      location: null,
      start: null,
      end: null,
    },
    tours: [
      {
        id: 1,
        name: 'Хаятт Ридженси Сочи',
        price: 200000,
        country: "Россия",
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg',
        description: 'Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного\n' +
            '        проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.\n' +
            '        В отеле предоставляется бесплатный Wi-Fi.',
        rating: 4.5,
      },
      {
        id: 2,
        name: 'Хаятт Ридженси Сочи',
        price: 20000,
        country: "Россия",
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg',
        description: 'Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного\n' +
            '        проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.\n' +
            '        В отеле предоставляется бесплатный Wi-Fi.',
        rating: 4.5,
      },
    ]
  }),
  computed: mapGetters(['getCitiesName']),
  methods: {
    currentDate(date) {
      const today = new Date()
      const yesterday = new Date(today.getTime() - 24 * 3600 * 1000)
      return date < yesterday
    },
    onResize() {
      this.isMobile = window.innerWidth < 500
      this.isSmall = window.innerWidth < 900
    },
    getCost(cost) {
      return cost.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    }
  },
  beforeDestroy() {
    if (typeof window === 'undefined') return

    window.removeEventListener('resize', this.onResize, {passive: true})
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})

    if (this.$route.query.from !== undefined) this.from = this.$route.query.from
    if (this.$route.query.to !== undefined) this.to = this.$route.query.to
    if (this.$route.query.startDate !== undefined) {
      this.date.push(new Date(this.$route.query.startDate.toString()))

      if (this.$route.query.endDate !== undefined) this.date.push(new Date(this.$route.query.endDate.toString()))
      else this.date.push(new Date(this.$route.query.startDate.toString()))
    }
  },
}
</script>

<style scoped>

</style>