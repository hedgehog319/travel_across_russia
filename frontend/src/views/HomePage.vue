<template>
  <div id="home">
    <v-container class="rounded" style="display: flex;margin-bottom: 50px;background-color: rgba(255,224,138, 0.8)">
      <v-icon>mdi-shield-alert</v-icon>
      <h3>Информация для путешественников во время COVID-19:</h3>
      <div class="text-center">
        <v-dialog v-model="dialog" width="500">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" height="25px"
                   style="margin-left: 5px;margin-top:2px;background-color: rgba(255,229,157,0.9)">
              <h3>подробнее</h3>
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="headline grey lighten-2">
              Privacy Policy
            </v-card-title>

            <v-card-text>Some text</v-card-text>

            <v-divider/>

            <v-card-actions>
              <v-spacer/>
              <v-btn color="primary" text @click="dialog = false">I accept</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </v-container>


    <v-container class="rounded"
                 style="margin-bottom: 50px;background-color: rgba(255,255,255, 1);border: 3px solid #535353">
      <v-card flat width="100%">
        <span class="headline" style="margin-left: 20px">Поиск тура</span>
        <v-card-text>
          <v-form style="height: 75px;" @submit.prevent="findTour">
            <v-container>
              <v-row>
                <v-col cols="12" md="3" style="width: 100px">
                  <v-text-field label="Откуда" required/>
                </v-col>

                <v-col cols="12" md="3">
                  <v-text-field label="Куда" required/>
                </v-col>

                <v-col cols="12" md="3">
                  <section style="margin-top: -6px; margin-right: 10px">
                    <span>Выбрать дату</span>
                    <date-picker v-model="date" confirm range style="width: 100%"/>
                  </section>
                </v-col>

                <v-col cols="12" md="3">
                  <v-btn large style="margin-top: 7px" type="submit">Поиск</v-btn>
                </v-col>

              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>

    <v-container class=" rounded"
                 style="text-align:center;margin-top: 50px;margin-bottom: 50px;background-color: #6ba3dd;">
      <v-card class="mx-auto" max-width="100%">
        <v-container class="pa-1">
          <v-item-group multiple>
            <v-row>
              <v-col v-for="(item, i) in items" :key="i" cols="12" lg="4" md="6" sm="6"
                     style="padding: 0 !important; margin:0  !important;"
                     xs="6">
                <v-item>
                  <v-img :src='item.src' class="text-right" height="200" style="background-color: rgba(0, 0, 0, 0.6);">
                    <v-sheet class="hover-card"
                             style="align-items: center;text-align: center;z-index: 9999; background-color: rgba(44,44,47,0.3); width: 100%; height: 100%; ">
                      <span
                          style="color: #ffffff; z-index: 9999; position: relative; justify-content: center;align-items: center;font-size: 30px">{{
                          item.title
                        }}</span>
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
import TourCardComponent from "@/components/TourCardComponent";
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';

export default {
  name: "HomePage",
  components: {
    'tour-card': TourCardComponent,
    DatePicker,
  },
  data() {
    return {
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
        {src: 'https://mosaica.ru/image/index/848xauto/173104?water=', title: 'Москва'},
        {
          src: 'https://visit-petersburg.ru/media/uploads/audioguide/43/43_cover.jpg.1050x500_q95_crop_upscale.jpg',
          title: 'Санкт-Петербург'
        },
        {
          src: 'https://img-cdn.tinkoffjournal.ru/main____shutterstock_1117372322.dapuhxw21c35.jpg',
          title: 'Екатеринбург'
        },
        {
          src: 'https://img-cdn.tinkoffjournal.ru/main___krasnodar___shutterstock_1416491849.gujmyhwjakf6.jpg',
          title: 'Краснодар'
        },
        {
          src: 'https://tripplanet.ru/wp-content/uploads/europe/russia/sochi/dostoprimechatelnosti-sochi.jpg',
          title: 'Сочи'
        },
        {
          src: 'https://icf-russia.ru/wp-content/uploads/2019/08/pfolio-vladivostok.jpg',
          title: 'Владивосток'
        },
        {
          src: 'https://pravdapfo.ru/sites/default/files/i_11_18.jpg',
          title: 'Уфа'
        },
        {
          src: 'https://sib.fm/storage/article/November2019/z5fxvsaIxesnvhtfZvjg.jpg', title: 'Новосибирск'
        },
        {
          src: 'https://uraloved.ru/images/mesta/orenb-obl/orenburg/orenburg-9.jpg', title: 'Оренбург'
        },
      ],
      menu: false,
    }
  },
}
</script>

<style scoped>

</style>