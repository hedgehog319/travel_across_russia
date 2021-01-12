<template>
  <div id="home">
    <v-container style="display: flex;margin-bottom: 50px;background-color: rgba(255,224,138, 0.8)" class="rounded">
      <v-icon>mdi-shield-alert</v-icon>
      <h3>Информация для путешественников во время COVID-19:</h3>
      <v-btn height="25px" style="margin-left: 5px;margin-top:2px;background-color: rgba(255,229,157,0.9)">
        <h3>подробнее</h3>
      </v-btn>
    </v-container>


    <v-container style="display: flex;margin-bottom: 50px;background-color: rgba(219,219,219,0.8)" class="rounded">
      <v-card flat width="100%">
        <v-card-title>
          <h2>Поиск тура</h2>
        </v-card-title>
        <v-card-text>
          <v-form>
            <v-container>
              <v-row>
                <v-col cols="12" md="4">
                  <v-text-field label="Откуда" required>

                  </v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <v-text-field label="Куда" required>

                  </v-text-field>
                </v-col>

                <v-col cols="12" md="4">
                  <div class="example">
                    <datepicker></datepicker>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>


    <v-container style="text-align:center;margin-top: 50px;margin-bottom: 50px;background-color: #6ba3dd;"
                 class=" rounded">
      <v-card max-width="100%" class="mx-auto">
        <v-container class="pa-1">
          <v-item-group multiple>
            <v-row>
              <v-col v-for="(item, i) in items" :key="i" cols="12" xs="6" sm="6" md="6" lg="4"
                     style="padding: 0 !important; margin:0  !important;">
                <v-item v-slot="{ active, toggle }">
                  <v-img style="background-color: rgba(0, 0, 0, 0.6);" :src='item.src' height="200" class="text-right">
                    <v-sheet class="hover-card"
                             style="align-items: center;text-align: center;z-index: 9999; background-color: rgba(44,44,47,0.3); width: 100%; height: 100%; ">
                      <span
                          style="color: #ffffff; z-index: 9999; position: relative; justify-content: center;align-items: center;font-size: 30px">{{ item.title }}</span>
                    </v-sheet>
                  </v-img>
                </v-item>
              </v-col>
            </v-row>
          </v-item-group>
        </v-container>
      </v-card>
    </v-container>


    <v-container style="background-color:rgba(0, 0, 0, 0.5); padding: 5px; width: 80%;" class="round">
      <div class="text-center " style="font-size: 30px; font-weight: 500; color: #FFFFFF">Рекомендуемые туры</div>
      <v-row no-gutters v-for="n in 2" :key="n" style="margin-bottom: 10px; margin-top: 10px">
        <v-col style="margin-bottom: 10px" v-for="n in 3" :key="n" cols="12" xs="12" sm="12" md="12" lg="4"
               align-self="center">
          <tour-card :tour="tour"/>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import TourCardComponent from "@/components/TourCardComponent";
import SearchPage from "@/views/SearchPage";
import Datepicker from 'vuejs-datepicker';

export default {
  name: "HomePage",
  components: {
    SearchPage,
    'tour-card': TourCardComponent,
    Datepicker,
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
      items: [
        {
          src: 'https://mosaica.ru/image/index/848xauto/173104?water=',
          title: 'Москва'
        },
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
          src: 'https://sib.fm/storage/article/November2019/z5fxvsaIxesnvhtfZvjg.jpg',
          title: 'Новосибирск'
        },
        {
          src: 'https://uraloved.ru/images/mesta/orenb-obl/orenburg/orenburg-9.jpg',
          title: 'Оренбург'
        },
      ],
    }
  }
}
</script>

<style scoped>

</style>