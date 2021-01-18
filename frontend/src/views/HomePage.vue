<template>
  <div id="home">
    <v-container class="rounded"
                 style="display: flex;margin-bottom: 40px;background-color: rgba(255,224,138, 0.8)">
      <v-icon>mdi-shield-alert</v-icon>
      <h3>Информация для путешественников во время COVID-19:</h3>
      <div class="text-center">
        <v-dialog v-model="dialog" width="600">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" height="25px"
                   style="margin-left: 5px;margin-top:2px;background-color: rgba(255,229,157,0.9)">
              <h3>подробнее</h3>
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="headline grey lighten-2">
              Памятка для туристов на 23.03.2020 (COVID-19)
            </v-card-title>

            <v-card-text>
              <p>Оперативная информация Ростуризма по ссылке: <a target="_blank"
                                                                 href="https://www.russiatourism.ru/news/16620/">
                https://www.russiatourism.ru/news/16620/</a></p>
              <p>Чтобы предотвратить распространение коронавируса и других респираторных заболеваний,
                соблюдайте меры предосторожности.
              <p>Не забывайте о правилах гигиены. Тщательно мойте руки и обрабатывайте их антисептиком.</p>
              <p>Следите за самочувствием. Ежедневное измерение температуры – обязательная процедура для всех.</p>
              <p>Не забудьте очищать рабочие места (столы, канцелярские приборы, гаджеты, панели оргтехники, ручки
                дверей) специальными салфетками.</p>
              <p>Проветривайте рабочие помещения.</p>
              <p> Если вы почувствовали первые признаки недомогания на работе, сообщите руководителю и отправляйтесь
                домой. Обратитесь к врачу, который откроет вам больничный лист, или позвоните по телефону 103.</p>
              <p>Дополнительная контактная информация на сайте <a target="_blank" href="https://стопкоронавирус.рф">
                https://стопкоронавирус.рф</a></p>
            </v-card-text>

            <v-divider/>

            <v-card-actions>
              <v-spacer/>
              <v-btn color="primary" text @click="dialog = false">Понятно</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </v-container>


    <v-container class="rounded"
                 style="margin-bottom: 50px;background-color: rgba(255,255,255, 1);border: 3px solid #8a8a8a">
      <v-card flat width="100%">
        <span class="headline" style="margin-left: 20px">Поиск тура</span>
        <v-card-text>
          <v-form @submit.prevent="findTour">
            <v-container style="display: flex">
              <v-row>
                <v-col cols="12" md="3">
                  <v-autocomplete v-model="from" :items="getCitiesName" dense filled label="Откуда"/>
                </v-col>

                <v-col cols="12" md="3">
                  <v-autocomplete v-model="to" :items="getCitiesName" dense filled label="Куда"/>
                </v-col>

                <v-col cols="12" md="4">
                  <section style="margin-top: -6px; margin-right: 10px">
                    <span>Выбрать дату</span>
                    <date-picker :disabled-date="currentDate" v-model="date" confirm range
                                 style="width: 100%"/>
                  </section>
                </v-col>
                <v-col cols="12" md="1">
                  <v-btn large style="margin-top: 7px"
                         type="submit">Поиск
                  </v-btn>
                </v-col>

              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>

    <v-container class="rounded"
                 style="margin-bottom: 50px;background-color: rgba(255,255,255, 1);border: 3px solid #dedede">
      <span class="text-center text-h4">Почему "Путешествуй по России"?</span>
      <v-container class="justify-center text-center">
        <v-row>
          <v-col cols="12" md="4">
            <v-icon color="primary" size="50">mdi-speedometer</v-icon>
            <p class="text-h5">Высокая скорость работы сайта</p>
          </v-col>

          <v-col cols="12" md="4" style="display: block">
            <v-icon color="primary" size="50">mdi-map</v-icon>
            <p class="text-h5">Вам доступна любая точка России</p>
          </v-col>

          <v-col cols="12" md="4">
            <v-icon color="primary" size="50">mdi-shield</v-icon>
            <p class="text-h5">Мы гарантируем безопасность всех ваших данных</p>
          </v-col>
        </v-row>
      </v-container>
    </v-container>

    <v-container class=" rounded"
                 style="text-align:center;margin-top: 50px;margin-bottom: 50px;background-color: #6ba3dd;">
      <v-card class="mx-auto" max-width="100%">
        <v-container class="pa-1">
          <v-item-group multiple>
            <v-row>
              <v-col cols="12" lg="4" md="6" sm="6" xs="6" style="padding: 0; margin:0"
                     v-for="(item, i) in items" :key="i" @click="tt(item.title)">
                <v-item>
                  <v-img :src='item.src' class="text-right" height="200">
                    <v-sheet class="hover-card"
                             style="text-align: center; width: 100%; height: 100%;
                             background-color: rgba(44,44,47,0.3);">
                      <span style="color: #fff; font-size: 30px" class="unselectable">{{ item.title }}</span>
                    </v-sheet>
                  </v-img>
                </v-item>
              </v-col>
            </v-row>
          </v-item-group>
        </v-container>
      </v-card>
    </v-container>


    <v-container class="round" style="background-color:rgba(0, 0, 0, 0.5); padding: 5px; width: 80%;">
      <div class="text-center " style="font-size: 30px; font-weight: 500; color: #FFFFFF">Рекомендуемые туры</div>
      <v-row no-gutters style="margin-bottom: 10px; margin-top: 10px">
        <v-col v-for="n in 6" :key="n" align-self="center" cols="12" lg="4" md="6" sm="12" style="margin-bottom: 10px"
               xs="12">
          <tour-card :tour="tour"/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import {required} from 'vuelidate/lib/validators';
import {mapGetters} from 'vuex'
import TourCardComponent from "@/components/TourCardComponent";
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';


export default {
  name: "HomePage",
  components: {
    'tour-card': TourCardComponent,
    DatePicker,
  },
  computed: mapGetters(['getCitiesName']),
  data() {
    return {
      from: null,
      to: null,
      dialog: false,
      adults: 2,
      date: null,
      tour: {
        title: "Море не помеха!",
        img: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        id: 0,
        days: "21",
        country: "Россия",
        city: "Владивосток",
        cost: 200000
      },
      items: [
        {src: require("@/assets/img/moscow.jpg"), title: 'Москва'},
        {src: require("@/assets/img/peterburg.jpg"), title: 'Санкт-Петербург'},
        {src: require("@/assets/img/ekaterinburg.jpg"), title: 'Екатеринбург'},
        {src: require("@/assets/img/krasnodar.jpg"), title: 'Краснодар'},
        {src: require("@/assets/img/sochi.jpg"), title: 'Сочи'},
        {src: require("@/assets/img/vladivostok.jpg"), title: 'Владивосток'},
        {src: require("@/assets/img/ufa.jpg"), title: 'Уфа'},
        {src: require("@/assets/img/novosibirsk.jpg"), title: 'Новосибирск'},
        {src: require("@/assets/img/orenburg.jpg"), title: 'Оренбург'},
        {src: require("@/assets/img/kazan.jpg"), title: 'Казань'},
        {src: require("@/assets/img/xhabarovsk.jpg"), title: 'Хабаровск'},
        {src: require("@/assets/img/samara.jpeg"), title: 'Самара'}
      ],
      menu: false,
    }
  },
  validations: {
    from: {
      required,
    },
    to: {
      required,
    },
  },
  methods: {
    currentDate(date) {
      const today = new Date()
      const yesterday = new Date(today.getTime() - 24 * 3600 * 1000)
      return date < yesterday
    },
    findTour() {
      const query = {}

      if (this.from !== null) query['from'] = this.from
      if (this.to !== null) query['to'] = this.to
      if (this.date !== null && this.date[0] !== null)
        query['startDate'] =
            this.date[0].getFullYear() + '-' + (this.date[0].getMonth() + 1) + '-' + this.date[0].getDate()
      if (this.date !== null && this.date[1] !== null)
        query['endDate'] =
            this.date[1].getFullYear() + '-' + (this.date[1].getMonth() + 1) + '-' + this.date[1].getDate()


      this.$router.push({name: 'search', query: query})
    },
    tt(title) {
      this.$router.push({name: 'search', query: {to: title}})
    }
  }
}
</script>

<style scoped>

</style>