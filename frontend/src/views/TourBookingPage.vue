<template>
  <div id="tour-booking">
    <v-container>
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1">Выбор тура</v-stepper-step>
          <v-divider/>
          <v-stepper-step :complete="e1 > 2" step="2">Заполнение документов</v-stepper-step>
          <v-divider/>
          <v-stepper-step step="3">Оплата тура</v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <v-card class="mb-12" color="grey lighten-1" height="300px">

            </v-card>

            <v-container style="display: flex">
              <!--TODO home redirect-->
              <v-btn @click="$router.push({name: 'home'})">Отмена</v-btn>
              <v-spacer/>
              <v-btn style="margin-right: 5px;" color="primary" @click="e1 = 2">Далее</v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card class="mb-12" color="lighten-1" height="300px" elevation="0">
              <v-list rounded>
                <v-subheader class="justify-center" style="font-size: 20px">Туристы</v-subheader>
                <div class="scrollbar round-track" style="height: 275px">
                  <v-list-item-group color="primary">
                    <v-list-item v-for="(tourist, i) in tourists" :key="i" @click="touristClick(i)">
                      <v-list-item-content>
                        <v-list-item-title v-if="!!tourist.lastname"
                                           v-text="tourist.lastname + ' ' + tourist.firstname"/>
                        <v-list-item-title v-else>Фамилия имя</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </div>
              </v-list>
            </v-card>

            <v-container style="display: flex">
              <v-btn @click="e1 = 1">Назад</v-btn>
              <v-spacer/>
              <v-btn icon @click="addTourist">
                <v-icon large>mdi-plus-circle-outline</v-icon>
              </v-btn>
              <v-spacer/>
              <v-btn style="margin-right: 5px;" color="primary" @click="e1 = 3">Далее</v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="3">
            <v-card class="mb-12" color="lighten-1" height="300px" elevation="0">
              <v-row style="margin-top: 5px" justify="center">
                <v-col style="padding: 0 12px" md="4">
                  <v-text-field height="35" v-model="formData.cardNumber" background-color="#f0f0f0" label="Номер карты"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>

                <v-col style="padding: 0 12px" md="4">
                  <v-text-field height="35" v-model="formData.cardName" background-color="#f0f0f0" label="Владелец"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>
              </v-row>

              <v-row justify="center">
                <v-col style="padding: 12px 12px; margin-top: 4px" md="2">
                  <v-select label="Месяц" solo dense v-model="formData.cardMonth"
                            :items="months"/>
                </v-col>

                <v-col style="padding: 12px 12px; margin-top: 4px" md="2">
                  <v-select label="Год" solo dense v-model="formData.cardYear"
                            :items="years"/>
                </v-col>

                <v-col style="padding: 0 12px;" md="2">
                  <v-text-field v-model="formData.cardCvv" background-color="#f0f0f0" label="CVV"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>
              </v-row>
            </v-card>

            <v-container style="display: flex">
              <v-btn @click="e1 = 2">Назад</v-btn>
              <v-spacer/>
              <v-btn style="margin-right: 5px;" color="primary" @click="e1 = 1">Завершить</v-btn>
            </v-container>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-container>

    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title class="justify-center"><span class="headline">Турист</span></v-card-title>

        <v-card-text>
          <v-container>
            <v-row justify="center">
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Фамилия" v-model="selectedTourist.lastname"/>
              </v-col>

              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Имя" v-model="selectedTourist.firstname"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="6" md="5">
                <v-menu ref="menu" v-model="birthDayMenu"
                        :close-on-content-click="false"
                        transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field v-model="selectedTourist.birthdate" label="Дата рождения"
                                  prepend-icon="mdi-calendar"
                                  readonly
                                  v-bind="attrs"
                                  v-on="on"/>
                  </template>

                  <v-date-picker v-model="selectedTourist.birthdate" no-title scrollable>
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" @click="birthDayMenu = false">Отмена</v-btn>
                    <v-btn text color="primary" @click="birthDayMenu = false">
                      OK
                    </v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="6" md="5">
                <v-select label="Тип документа" :items="['Паспорт', 'Загранпаспорт']"
                          v-model="selectedTourist.documentType"/>
              </v-col>

              <v-col cols="12" sm="6" md="2">
                <!--TODO number validation-->
                <v-text-field label="Серия" v-model="selectedTourist.series"/>
              </v-col>

              <v-col cols="12" sm="6" md="3">
                <!--TODO number validation-->
                <v-text-field label="Номер" v-model="selectedTourist.number"/>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-btn color="red darken-1" text @click="removeTourist">Удалить</v-btn>
          <v-spacer/>
          <v-btn color="blue darken-1" text @click="saveTourist">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="creating">
      Нельзя зарегистрировать больше 7 туристов. Для регистрации группы более 7 человек обратитесь к туроператору
    </v-snackbar>
  </div>
</template>

<script>

export default {
  name: "TourBooking",
  data() {
    return {
      e1: 1,
      dialog: false,
      birthDayMenu: false,
      creating: false,
      touristID: null,
      tourists: [],
      selectedTourist: {
        firstname: null,
        lastname: null,
        birthdate: null,
        documentType: null,
        series: null,
        number: null
      },
      formData: {
        cardName: '',
        cardNumber: '',
        cardMonth: '',
        cardYear: '',
        cardCvv: ''
      },
    }
  },
  computed: {
    months() {
      const months = []
      for (let i = 1; i <= 12; i++) {
        months.push(i < 10 ? '0' + i : i)
      }

      return months
    },
    years() {
      const years = []
      const year = new Date().getFullYear()
      for (let i = 0; i < 12; i++) {
        years.push(year + i)
      }

      return years
    }
  },
  methods: {
    touristClick(id) {
      this.touristID = id
      this.selectedTourist = {...this.tourists[id]}

      this.dialog = true
    },
    removeTourist() {
      this.tourists.splice(this.touristID, 1);

      this.dialog = false
    },
    addTourist() {
      if (this.tourists.length < 7) {
        this.tourists.push({
          firstname: null,
          lastname: null,
          birthdate: null,
          documentType: null,
          series: null,
          number: null
        })
      } else {
        this.creating = true
        window.setTimeout(() => {
          this.creating = false
        }, 6000)
      }
    },
    saveTourist() {
      this.tourists[this.touristID] = {...this.selectedTourist}

      this.dialog = false
    },
  }
}
</script>

<style scoped>

</style>