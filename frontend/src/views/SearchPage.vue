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
                  <v-row>
                    <v-col cols="12" md="4">
                      <v-autocomplete v-model="from" :items="cities" dense filled label="Откуда"></v-autocomplete>
                    </v-col>

                    <v-col cols="12" md="4">
                      <v-autocomplete v-model="to" :items="cities" dense filled label="Куда"></v-autocomplete>
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
                      <v-rating style="margin-top: 15px" :value="4.5" color="amber" dense half-increments size="30"/>
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
                            <v-radio v-on="on" v-bind="attrs" :label="type.short" :value="i"/>
                          </template>
                          <span>{{type.full}}</span>
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

      <v-card v-if="isSmall" v-for="(tour, i) in tours" :key="i" class="rounded" style="padding-top: 10px;margin: 10px">
        <v-img v-if="isMobile" :src="tour.src" class="rounded" height="200px" style="margin: 0 10px 10px 10px"/>
        <v-card-text style="height: 100% !important;">
          <div>
            <span style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</span>
            <v-spacer/>
            <v-btn icon large style="position: absolute; bottom: 3px; right: 0">
              <v-icon color="#ffd700" large>mdi-heart</v-icon>
            </v-btn>
          </div>
          <p style="font-size: 20px; color: #242424; opacity: 0.7">
            Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного
            проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.
            В отеле предоставляется бесплатный Wi-Fi.
          </p>
          <v-rating :value="4.5" color="amber" dense half-increments readonly size="20"/>
        </v-card-text>
      </v-card>

      <v-card v-if="!isSmall" v-for="(tour, i) in tours" :key="i" class="rounded" style="display: flex;margin: 10px">
        <v-img :src="tour.src" class="rounded" height="200px" style="margin: 10px" width="300px"/>
        <v-card-text style="height: 100% !important;">
          <div>
            <p style="font-size: 30px; color: black">{{ tour.title }}, {{ tour.country }}</p>
            <v-spacer/>
            <v-btn icon large style="position: absolute; top: 3px; right: 0">
              <v-icon color="#ffd700" large>mdi-heart</v-icon>
            </v-btn>
          </div>
          <p style="font-size: 20px; color: #242424; opacity: 0.7">
            Отель Hyatt Regency Sochi расположен в центре Сочи, в 200 метрах от побережья Черного моря и Курортного
            проспекта. Прогулка до морского порта и торгового центра «Гранд-Марина» занимает 5 минут.
            В отеле предоставляется бесплатный Wi-Fi.
          </p>
          <v-rating :value="4.5" color="amber" dense half-increments readonly size="20"/>
        </v-card-text>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import DatePicker from "vue2-datepicker";

export default {
  name: "SearchPage",
  components: {
    DatePicker,
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
    cities: ['Москва', 'Санкт-Петербург', 'Уфа', 'Владивосток', 'Екатеринбург', 'Оренбург', 'Сочи', 'Краснодар'],
    from: null,
    to: null,
    time: null,
    date: null,
    trip: {
      name: '',
      location: null,
      start: null,
      end: null,
    },
    countries: ["Россия", "Франция", "Монголия"],
    tours: [
      {
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg', title: 'Хаятт Ридженси Сочи',
        country: "Россия"
      },
      {
        src: 'https://cf.bstatic.com/images/hotel/max1280x900/269/269929828.jpg', title: 'Хаятт Ридженси Сочи',
        country: "Россия"
      }
    ]
  }),
  beforeDestroy() {
    if (typeof window === 'undefined') return

    window.removeEventListener('resize', this.onResize, {passive: true})
  },

  mounted() {
    this.onResize()

    window.addEventListener('resize', this.onResize, {passive: true})
  },
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
}
</script>

<style scoped>

</style>