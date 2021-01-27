<template>
  <div id="tour-booking">
    <v-container>
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1" class="unselectable">Выбор тура</v-stepper-step>
          <v-divider/>
          <v-stepper-step :complete="e1 > 2" step="2" class="unselectable">Заполнение документов</v-stepper-step>
          <v-divider/>
          <v-stepper-step step="3" class="unselectable">Оплата тура</v-stepper-step>
          <v-progress-linear :active="loading" :indeterminate="loading" absolute bottom color="primary accent-4"/>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content step="1">

            <v-skeleton-loader v-if="!isLoad" type="card" height="300" class="mx-auto white"/>

            <div v-else>
              <v-card class="rounded unselectable" elevation="0" min-height="300"
                      :style="isSmall ? 'display: inline-block; margin: 10px'
                    : 'display: flex; margin: 10px;'">
                <v-img :src="tour.photo" height="300px" class="d-block ma-2 rounded"
                       :width="isSmall ? undefined : 300"/>
                <v-card-text class="d-flex flex-column justify-md-space-around">
                  <div class="mb-2">
                    <span class="text-h4 black--text">{{ tour.name }}, {{ tour.country_name }}</span>
                  </div>
                  <span class="grey--text text--secondary mb-2" style="font-size: 20px;">
                  {{ tour.description }}
                </span>
                  <div class="d-flex mt-2">
                    <div class="text-center black--text" style="font-size: 20px">
                      <span>Тип питания</span>
                      <v-radio-group row v-model="typeOfFood">
                        <v-tooltip bottom v-for="(type, i) in typesOfFood" :key="i">
                          <template v-slot:activator="{ on }">
                            <v-radio :ripple="false" v-on="on" :label="type.short" :value="i"/>
                          </template>
                          <span>{{ type.full }}</span>
                        </v-tooltip>
                      </v-radio-group>
                    </div>
                  </div>
                  <span class="unselectable" style="font-size: 30px">Стоимость тура: {{ getCost(tour.price) }} Р</span>

                </v-card-text>
              </v-card>
              <v-container class="d-flex">
                <v-btn @click="$router.push({name: 'home'})">Отмена</v-btn>
                <v-spacer/>
                <v-btn color="primary" class="mr-1" @click="e1 = 2">Далее</v-btn>
              </v-container>
            </div>
          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card class="mb-12" color="lighten-1" elevation="0" height="300px">
              <v-list rounded>
                <v-subheader class="justify-center" style="font-size: 20px">Туристы</v-subheader>
                <div class="scrollbar round-track" style="height: 275px">
                  <v-list-item-group color="primary">
                    <v-list-item v-for="(tourist, i) in tourists" :key="i" @click="touristClick(i)">
                      <v-list-item-content>
                        <v-list-item-title
                            v-text="tourist.document.lastname + '  ' + tourist.document.firstname + '  '
                            + tourist.document.birthdate + '  ' + tourist.document.type + '  '
                            + tourist.document.series + '  ' + tourist.document.number"/>
                      </v-list-item-content>
                    </v-list-item>
                  </v-list-item-group>
                </div>
              </v-list>
            </v-card>

            <v-container class="d-flex">
              <v-btn @click="e1 = 1">Назад</v-btn>
              <v-spacer/>
              <v-btn icon @click="addTourist">
                <v-icon large>mdi-plus-circle-outline</v-icon>
              </v-btn>
              <v-spacer/>
              <v-btn color="primary" class="mr-1" @click="goToPay">Далее</v-btn>
            </v-container>
          </v-stepper-content>

          <v-stepper-content step="3">

            <v-card class="mb-12" color="lighten-1" elevation="0" min-height="300">
              <v-row justify="center" class="mt-1">
                <v-col cols="12" lg="3" md="3" sm="3" style="margin: 0 6px; padding: 0;">
                  <v-text-field filled v-model="card.number" height="38" label="Номер карты"
                                :error-messages="cardNumberErrors" counter="16" maxlength="16"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>

                <v-col cols="12" lg="3" md="3" sm="3" style="margin: 0 6px; padding: 0;">
                  <v-text-field filled :value="card.name" height="38" label="Владелец"
                                @input="input => this.card.name = input.toUpperCase()"
                                :error-messages="cardNameErrors" counter="20" maxlength="20"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>
              </v-row>

              <v-row justify="center">
                <v-col cols="12" lg="2" md="2" sm="2" style="margin: 20px 6px; padding: 0 5px 0 5px;">
                  <v-select v-model="card.month" :items="months" dense label="Месяц"
                            :error-messages="cardMonthErrors"
                            solo/>
                </v-col>

                <v-col cols="12" lg="2" md="2" sm="2" style="margin: 20px 6px; padding: 0 5px 0 5px;">
                  <v-select v-model="card.year" :items="years" dense label="Год"
                            :error-messages="cardYearErrors"
                            solo/>
                </v-col>

                <v-col cols="12" lg="2" md="2" sm="2" style="margin: 0 6px; padding: 0;">
                  <v-text-field filled v-model="card.cvv" label="CVV" height="38"
                                :error-messages="cardCVVErrors" counter="3" maxlength="3"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px; margin-top: 0;
                                padding-top: 2px"/>
                </v-col>
              </v-row>

              <v-row v-if="!$cookies.isKey('Token')" justify="center">
                <v-col cols="12" lg="6" md="6" sm="6" style="margin: 20px 6px; padding: 0 5px 0 5px;">
                  <v-text-field filled v-model="email" height="38" label="Email"
                                :error-messages="emailErrors"
                                style="border-top-left-radius: 5px; border-top-right-radius: 5px;"/>
                </v-col>
              </v-row>

              <v-row class="mt-3" justify="center">
                <span class="text-h5">Итого к оплате: </span>
                <span class="ml-3" style="font-size: 23px">{{ getCost(tour.price) }}</span>
                <v-icon>mdi-currency-rub</v-icon>
              </v-row>
            </v-card>

            <v-container class="d-flex">
              <v-btn @click="e1 = 2">Назад</v-btn>
              <v-spacer/>
              <v-btn color="primary" class="mr-1" @click="toPay">Оплатить</v-btn>
            </v-container>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-container>

    <v-dialog v-model="touristDialog" max-width="500px">
      <v-card>
        <v-card-title class="justify-center">
          <span class="headline">Турист</span>

          <v-tooltip bottom>
            <template v-slot:activator="{ on }">
              <v-btn v-if="$cookies.isKey('Token')" icon absolute style="right: 5px"
                     v-on="on" @click="loadDocument">
                <v-icon>mdi-file-document</v-icon>
              </v-btn>
            </template>
            <span>Загрузить свой документ</span>
          </v-tooltip>
        </v-card-title>

        <v-card-text>
          <v-container>
            <v-row justify="center">
              <v-col cols="12" lg="6" md="6" sm="6">
                <v-text-field counter="20" maxlength="20" :error-messages="lastnameErrors"
                              :value="tourist.document.lastname"
                              @input="input => tourist.document.lastname = input.toUpperCase()"
                              label="Фамилия"/>
              </v-col>

              <v-col cols="12" lg="6" md="6" sm="6">
                <v-text-field counter="20" maxlength="20" :error-messages="firstnameErrors"
                              :value="tourist.document.firstname"
                              @input="input => tourist.document.firstname = input.toUpperCase()"
                              label="Имя"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" lg="12" md="12" sm="12">
                <v-menu ref="menu" v-model="birthDayMenu" :max-width="290"
                        :close-on-content-click="false"
                        transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field :error-messages="birthdateErrors" v-model="tourist.document.birthdate" v-bind="attrs"
                                  v-on="on"
                                  label="Дата рождения"
                                  prepend-icon="mdi-calendar"
                                  readonly/>
                  </template>
                  <v-date-picker :max="new Date().toJSON().slice(0,10)" v-model="tourist.document.birthdate" no-title
                                 scrollable>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="birthDayMenu = false">Отмена</v-btn>
                    <v-btn color="primary" text @click="birthDayMenu = false">OK</v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="12" sm="12">
                <v-select :error-messages="documentTypeErrors" v-model="tourist.document.type"
                          :items="getDocumentTypes" label="Тип документа"/>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" md="6" sm="6">
                <v-text-field counter="4" :error-messages="seriesErrors" maxlength="4" v-model="tourist.document.series"
                              label="Серия"/>
              </v-col>

              <v-col cols="12" md="6" sm="6">
                <v-text-field counter="6" :error-messages="numberErrors" maxlength="6" v-model="tourist.document.number"
                              label="Номер"/>
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

    <v-snackbar top v-model="maxLimit">
      Нельзя зарегистрировать больше 7 туристов. Для регистрации группы более 7 человек обратитесь к туроператору
    </v-snackbar>
    <v-snackbar top v-model="consistTourist">Укажите хотя бы одного туриста</v-snackbar>
    <v-snackbar top v-model="isPaid">Ваш тур оплачен</v-snackbar>
  </div>
</template>

<script>
import {required, minLength, numeric, email} from 'vuelidate/lib/validators'
import {mapGetters} from "vuex";

export default {
  name: "TourBooking",
  data() {
    return {
      selectedTypes: ['RO'],
      typesOfFood: [{short: 'RO', full: 'Без питания'},
        {short: 'BB', full: 'Только завтраки'},
        {short: 'HB', full: 'Завтрак и ужин'},
        {short: 'FB', full: 'Завтрак, обед и ужин'},
        {short: 'AI', full: 'Всё включено'}
      ],
      typeOfFood: 1,
      e1: 1,
      isSmall: false,
      tour: {
        tour_id: Number,
        name: String,
        price: Number,
        country_name: String,
        city_name: String,
        photo: String,
        description: String,
        rating: Number,
      },
      touristDialog: false,
      birthDayMenu: false,
      maxLimit: false,
      consistTourist: false,
      loading: false,
      touristID: null,
      tourists: [],
      tourist: {
        email: null,
        document: {
          firstname: null,
          lastname: null,
          birthdate: null,
          type: null,
          series: null,
          number: null
        }
      },
      card: {
        name: '',
        number: '',
        month: '',
        year: '',
        cvv: ''
      },
      email: null,
      isPaid: false,
      isLoad: false
    }
  },
  validations: {
    tourists: {
      required
    },
    tourist: {
      document: {
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
        type: {
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
        minLength: minLength(16),
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
        minLength: minLength(3),
        numeric
      }
    },
    email: {
      required,
      email
    }
  },
  computed: {
    ...mapGetters(['getDocumentTypes', 'getDocumentType', 'getDocumentId']),
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
      if (!this.$v.tourist.document.firstname.$dirty) return mess
      if (!this.$v.tourist.document.firstname.required) mess = 'Введите имя'
      else if (!this.$v.tourist.document.firstname.ruLetter) mess = 'Имя содержит русские буквы'
      else if (!this.$v.tourist.document.firstname.numbers) mess = 'Имя содержит цифры'

      return mess
    },
    lastnameErrors() {
      let mess = ''
      if (!this.$v.tourist.document.lastname.$dirty) return mess
      if (!this.$v.tourist.document.lastname.required) mess = 'Введите фамилию'
      else if (!this.$v.tourist.document.lastname.ruLetter) mess = 'Фамилия содержит русские буквы'
      else if (!this.$v.tourist.document.lastname.numbers) mess = 'Фамилия содержит цифры'

      return mess
    },
    birthdateErrors() {
      let mess = ''
      if (!this.$v.tourist.document.birthdate.$dirty) return mess
      if (!this.$v.tourist.document.birthdate.required) mess = 'Укажите дату рождения'

      return mess
    },
    documentTypeErrors() {
      let mess = ''
      if (!this.$v.tourist.document.type.$dirty) return mess
      if (!this.$v.tourist.document.type.required) mess = 'Выберите тип документа'

      return mess
    },
    seriesErrors() {
      let mess = ''
      if (!this.$v.tourist.document.series.$dirty) return mess
      if (!this.$v.tourist.document.series.required) mess = 'Введите серию документа'
      else if (!this.$v.tourist.document.series.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.tourist.document.series.minLength) mess = 'Введите 4 цифры'

      return mess
    },
    numberErrors() {
      let mess = ''
      if (!this.$v.tourist.document.number.$dirty) return mess
      if (!this.$v.tourist.document.number.required) mess = 'Введите номер документа'
      else if (!this.$v.tourist.document.number.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.tourist.document.number.minLength) mess = 'Введите 6 цифр'

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
      else if (!this.$v.card.number.minLength) mess = 'Номер карты слишком короткий'

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
      else if (!this.$v.card.cvv.minLength) mess = 'CVV карты слишком короткий'

      return mess
    },

    emailErrors() {
      let mess = ''
      if (!this.$v.email.$dirty) return mess
      if (!this.$v.email.required) mess = 'Введите email'
      else if (!this.$v.email.email) mess = 'Email не верный'

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
      if (this.touristID >= 0) {
        this.tourists.splice(this.touristID, 1);
        this.touristID = -1
      }

      this.touristDialog = false
    },
    addTourist() {
      if (this.tourists.length < 7) {
        this.$v.tourist.document.$reset()
        this.tourist = {
          email: null,
          document: {
            firstname: null,
            lastname: null,
            birthdate: null,
            type: null,
            series: null,
            number: null
          }
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
      this.$v.tourist.document.$touch()

      if (!this.$v.tourist.document.$invalid) {
        this.saveTourist()
      }
    },
    goToPay() {
      this.$v.tourists.$touch()

      if (!this.$v.tourists.$invalid) {
        this.e1 = 3
      } else {
        this.consistTourist = true
      }
    },
    async sendPay() {
      this.loading = true
      setTimeout(() => {
        this.loading = false
        this.isPaid = true
      }, 1000)

      if (this.email !== null)
        this.tourists[0].email = this.email
      else {
        const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
        await this.axios.get('/api/document/', conf)
            .then(res => {
              if (res.statusText === 'OK')
                this.tourists[0].email = res.data.email
            })
      }

      for (const i of this.tourists) {
        i.document.type = this.getDocumentId(i.document.type)
      }

      const booked = {
        tour_id: this.tour.tour_id,
        tourists: this.tourists
      }

      await this.axios.post('/api/booked-tours/', booked)
          .catch(err => console.log(err.response))
    },
    toPay() {
      this.$v.card.$touch()

      if (!this.$cookies.isKey('Token'))
        this.$v.email.$touch()

      if (!this.$v.card.$invalid &&
          (this.$cookies.isKey('Token') || !this.$v.email.$invalid)) {
        this.sendPay()
      }
    },
    onResize() {
      this.isSmall = window.innerWidth < 900
    },
    getCost(price) {
      return price.toString()
          .replace(/(\d{1,3}(?=(?:\d\d\d)+(?!\d)))/g, "$1 ")
    },
    loadDocument() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      this.axios.get('api/document/', conf)
          .then(res => {
            if (res.data.length > 0) {
              this.tourist.document = res.data[0]
              this.tourist.document.type = this.getDocumentType(this.tourist.document.type)
            }
          })
    }
  },
  beforeDestroy() {
    if (typeof window === undefined) return
    window.removeEventListener('resize', this.onResize, {passive: true})
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
  },
  created() {
    this.axios.get(`api/tours/?tour_id=${this.$route.query.id}`).then(resp => {
      if (resp.statusText === "OK") {
        this.tour = resp.data[0]
        this.isLoad = true
      }
    })
  }
}
</script>

<style scoped>

</style>