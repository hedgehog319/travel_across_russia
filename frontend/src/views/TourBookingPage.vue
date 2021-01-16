<template>
  <div id="tour-booking">
    <v-container>
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step editable :complete="e1 > 1" step="1" class="unselectable">Выбор тура</v-stepper-step>
          <v-divider/>
          <v-stepper-step editable :complete="e1 > 2" step="2" class="unselectable">Заполнение документов
          </v-stepper-step>
          <v-divider/>
          <v-stepper-step editable step="3" class="unselectable">Оплата тура</v-stepper-step>
          <v-progress-linear
              :active="loading"
              :indeterminate="loading"
              absolute
              bottom
              color="deep-purple accent-4"/>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">
            <v-card class="mb-12" color="grey lighten-1" height="300px">

            </v-card>

            <v-container style="display: flex">
              <!--TODO home redirect-->
              <v-btn @click="$router.push({name: 'home'})">Отмена</v-btn>
              <v-spacer/>
              <v-btn color="primary" style="margin-right: 5px;" @click="e1 = 2">Далее</v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card class="mb-12" color="lighten-1" elevation="0" height="300px">
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
              <v-btn color="primary" style="margin-right: 5px;" @click="e1 = 3">Далее</v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="3">

            <v-card class="mb-12" color="lighten-1" elevation="0" height="300px">
              <v-row justify="center" style="margin-top: 5px">
                <v-col cols="12" lg="3" md="3" sm="3" style="margin: 0 6px; padding: 0;">
                  <v-text-field v-model="card.number" background-color="#f0f0f0" height="38" label="Номер карты"
                                :error-messages="cardNumberErrors"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>

                <v-col cols="12" lg="3" md="3" sm="3" style="margin: 0 6px; padding: 0;">
                  <v-text-field v-model="card.name" background-color="#f0f0f0" height="38" label="Владелец"
                                :error-messages="cardNameErrors"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>
              </v-row>

              <v-row justify="center">
                <v-col cols="12" lg="2" md="2" sm="2" style="margin: 3px 6px; padding: 0;">
                  <v-select v-model="card.month" :items="months" dense label="Месяц"
                            :error-messages="cardMonthErrors"
                            solo/>
                </v-col>

                <v-col cols="12" lg="2" md="2" sm="2" style="margin: 3px 6px; padding: 0;">
                  <v-select v-model="card.year" :items="years" dense label="Год"
                            :error-messages="cardYearErrors"
                            solo/>
                </v-col>

                <v-col cols="12" lg="2" md="2" sm="2" style="margin: 0 6px; padding: 0;">
                  <v-text-field v-model="card.cvv" background-color="#f0f0f0" label="CVV" height="38"
                                :error-messages="cardCVVErrors"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px; margin-top: 0; padding-top: 2px"/>
                </v-col>
              </v-row>
            </v-card>

            <v-container style="display: flex">
              <v-btn @click="e1 = 2">Назад</v-btn>
              <v-spacer/>
              <v-btn color="primary" style="margin-right: 5px;" @click="toPay">Оплатить</v-btn>
            </v-container>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-container>

    <v-dialog v-model="touristDialog" max-width="500px">
      <v-card>
        <v-card-title class="justify-center"><span class="headline">Турист</span></v-card-title>

        <v-card-text>
          <v-container>
            <v-row justify="center">
              <v-col cols="12" lg="6" md="6" sm="6">
                <v-text-field :error-messages="lastnameErrors" v-model="tourist.lastname" label="Фамилия"/>
              </v-col>

              <v-col cols="12" lg="6" md="6" sm="6">
                <v-text-field :error-messages="firstnameErrors" v-model="tourist.firstname" label="Имя"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" lg="12" md="12" sm="12">
                <v-menu ref="menu" v-model="birthDayMenu" :max-width="290"
                        :close-on-content-click="false"
                        transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field :error-messages="birthdateErrors" v-model="tourist.birthdate" v-bind="attrs"
                                  v-on="on"
                                  label="Дата рождения"
                                  prepend-icon="mdi-calendar"
                                  readonly/>
                  </template>
                  <v-date-picker :max="new Date().toJSON().slice(0,10)" v-model="tourist.birthdate" no-title scrollable>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="birthDayMenu = false">Отмена</v-btn>
                    <v-btn color="primary" text @click="birthDayMenu = false">OK</v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="12" sm="12">
                <v-select :error-messages="documentTypeErrors" v-model="tourist.documentType"
                          :items="['Паспорт', 'Загранпаспорт']"
                          label="Тип документа"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="6" sm="6">
                <v-text-field :error-messages="seriesErrors" maxlength="4" v-model="tourist.series" label="Серия"/>
              </v-col>

              <v-col cols="12" md="6" sm="6">
                <v-text-field :error-messages="numberErrors" maxlength="6" v-model="tourist.number" label="Номер"/>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-btn color="red darken-1" text @click="removeTourist">Удалить</v-btn>
          <v-spacer/>
          <v-btn color="blue darken-1" text @click="saveClick">Сохранить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="maxLimit">
      Нельзя зарегистрировать больше 7 туристов. Для регистрации группы более 7 человек обратитесь к туроператору
    </v-snackbar>
  </div>
</template>

<script>
import {required, minLength, numeric} from 'vuelidate/lib/validators'

export default {
  name: "TourBooking",
  data() {
    return {
      e1: 1,
      touristDialog: false,
      birthDayMenu: false,
      maxLimit: false,
      loading: false,
      touristID: null,
      tourists: [],
      tourist: {
        firstname: null,
        lastname: null,
        birthdate: null,
        documentType: null,
        series: null,
        number: null
      },
      card: {
        name: '',
        number: '',
        month: '',
        year: '',
        cvv: ''
      },
    }
  },
  validations: {
    tourist: {
      firstname: {
        required,
        ruLetter: (v) => !(/[а-я]/.test(v) || /[А-Я]/.test(v)),
        numbers: (v) => !(/[0-9]/.test(v)),
      },
      lastname: {
        required,
        ruLetter: (v) => !(/[а-я]/.test(v) || /[А-Я]/.test(v)),
        numbers: (v) => !(/[0-9]/.test(v)),
      },
      birthdate: {
        required
      },
      documentType: {
        required
      },
      series: {
        required,
        minLength: minLength(4),
        numeric
      },
      number: {
        required,
        minLength: minLength(6),
        numeric
      }
    },
    card: {
      name: {
        required,
        ruLetter: (v) => !(/[а-я]/.test(v) || /[А-Я]/.test(v)),
        numbers: (v) => !(/[0-9]/.test(v)),
      },
      number: {
        required,
        numeric
      },
      month: {
        required
      },
      year: {
        required
      },
      cvv: {
        required,
        numeric
      }
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
    },
    firstnameErrors() {
      let mess = ''
      if (!this.$v.tourist.firstname.$dirty) return mess
      if (!this.$v.tourist.firstname.required) mess = 'Введите имя'
      else if (!this.$v.tourist.firstname.ruLetter) mess = 'Имя содержит русские буквы'
      else if (!this.$v.tourist.firstname.numbers) mess = 'Имя содержит цифры'

      return mess
    },
    lastnameErrors() {
      let mess = ''
      if (!this.$v.tourist.lastname.$dirty) return mess
      if (!this.$v.tourist.lastname.required) mess = 'Введите фамилию'
      else if (!this.$v.tourist.lastname.ruLetter) mess = 'Фамилия содержит русские буквы'
      else if (!this.$v.tourist.lastname.numbers) mess = 'Фамилия содержит цифры'

      return mess
    },
    birthdateErrors() {
      let mess = ''
      if (!this.$v.tourist.birthdate.$dirty) return mess
      if (!this.$v.tourist.birthdate.required) mess = 'Укажите дату рождения'

      return mess
    },
    documentTypeErrors() {
      let mess = ''
      if (!this.$v.tourist.documentType.$dirty) return mess
      if (!this.$v.tourist.documentType.required) mess = 'Выберите тип документа'

      return mess
    },
    seriesErrors() {
      let mess = ''
      if (!this.$v.tourist.series.$dirty) return mess
      if (!this.$v.tourist.series.required) mess = 'Введите серию документа'
      else if (!this.$v.tourist.series.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.tourist.series.minLength) mess = 'Введите 4 цифры'

      return mess
    },
    numberErrors() {
      let mess = ''
      if (!this.$v.tourist.number.$dirty) return mess
      if (!this.$v.tourist.number.required) mess = 'Введите номер документа'
      else if (!this.$v.tourist.number.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.tourist.number.minLength) mess = 'Введите 6 цифр'

      return mess
    },

    cardNameErrors() {
      let mess = ''
      if (!this.$v.card.name.$dirty) return mess
      if (!this.$v.card.name.required) mess = 'Введите владельца карты'
      else if (!this.$v.card.name.ruLetter) mess = 'Имя содержит русские символы'
      else if (!this.$v.card.name.numbers) mess = 'Имя содержит цифры'

      return mess
    },
    cardNumberErrors() {
      let mess = ''
      if (!this.$v.card.number.$dirty) return mess
      if (!this.$v.card.number.required) mess = 'Введите номер карты'
      else if (!this.$v.card.number.numeric) mess = 'Вы ввели не число'

      return mess
    },
    cardMonthErrors() {
      let mess = ''
      if (!this.$v.card.month.$dirty) return mess
      if (!this.$v.card.month.required) mess = 'Введите месяц окончания'

      return mess
    },
    cardYearErrors() {
      let mess = ''
      if (!this.$v.card.number.$dirty) return mess
      if (!this.$v.card.year.required) mess = 'Введите год окончания'

      return mess
    },
    cardCVVErrors() {
      let mess = ''
      if (!this.$v.card.cvv.$dirty) return mess
      if (!this.$v.card.cvv.required) mess = 'Введите cvv код'
      else if (!this.$v.card.cvv.numeric) mess = 'Вы ввели не число'

      return mess
    }
  },
  methods: {
    touristClick(id) {
      this.touristID = id
      this.tourist = {...this.tourists[id]}

      this.touristDialog = true
    },
    removeTourist() {
      this.tourists.splice(this.touristID, 1);

      this.touristDialog = false
    },
    addTourist() {
      if (this.tourists.length < 7) {
        this.$v.tourist.$reset()
        this.tourist = {
          firstname: null,
          lastname: null,
          birthdate: null,
          documentType: null,
          series: null,
          number: null
        }
        this.touristDialog = true
        this.touristID = -1
      } else {
        this.maxLimit = true
      }
    },
    saveTourist() {
      if (this.touristID < 0)
        this.tourists.push(this.tourist)
      else
        this.tourists[this.touristID] = this.tourist
      this.touristDialog = false
    },
    saveClick() {
      this.$v.tourist.$touch()

      if (!this.$v.tourist.$invalid) {
        this.saveTourist()
      }
    },
    sendPay() {
      this.loading = true
    },
    toPay() {
      this.$v.card.$touch()

      if (!this.$v.card.$invalid) {
        this.sendPay()
      }
    }
  },
  watch: {
    loading(val) {
      if (!val) return
      setTimeout(() => (this.loading = false), 1000)
    },
  },
}
</script>

<style scoped>

</style>