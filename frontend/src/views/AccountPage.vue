<template>
  <div id="account">
    <v-col class="ma-auto" cols="12" md="6">
      <v-card>
        <v-toolbar color="primary" dark flat>
          <v-toolbar-title>Профиль</v-toolbar-title>
        </v-toolbar>
        <v-tabs show-arrows>
          <v-tab>Информация</v-tab>
          <v-tab>Изменение данных</v-tab>
          <v-tab>Мои туры</v-tab>

          <v-tab-item>
            <v-card flat>
              <v-simple-table class="ma-2">
                <template v-slot:default>
                  <thead>
                  <tr>
                    <th class="text-left text-h4">Аккаунт</th>
                    <th class="text-left"/>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td>Логин</td>
                    <td>{{ user.username }}</td>
                  </tr>
                  <tr>
                    <td>Email</td>
                    <td>{{ user.email }}</td>
                  </tr>
                  <tr>
                    <td>Тип документа</td>
                    <td>{{ document.type }}</td>
                  </tr>
                  <tr>
                    <td>Имя</td>
                    <td>{{ document.firstname }}</td>
                  </tr>
                  <tr>
                    <td>Фамилия</td>
                    <td>{{ document.lastname }}</td>
                  </tr>
                  <tr>
                    <td>Дата рождения</td>
                    <td>{{ document.birthdate }}</td>
                  </tr>
                  <tr>
                    <td>Серия документа</td>
                    <td>{{ document.series }}</td>
                  </tr>
                  <tr>
                    <td>Номер документа</td>
                    <td>{{ document.number }}</td>
                  </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-card>
          </v-tab-item>

          <v-tab-item>
            <v-card flat class="text-center">
              <form class="ma-4" @submit.prevent="updateUserInfo">
                <h2>Изменение профиля</h2>
                <v-text-field v-model="new_email" :error-messages="emailErrors" label="Email"/>
                <v-select :items="getDocumentTypes" :error-messages="documentTypeErrors"
                          v-model="changed_document.type"/>
                <v-text-field :value="changed_document.firstname" :error-messages="firstnameErrors"
                              counter="20" @input="input => changed_document.firstname = input.toUpperCase()"
                              label="Имя"/>
                <v-text-field :value="changed_document.lastname" :error-messages="lastnameErrors"
                              counter="20" @input="input => changed_document.lastname = input.toUpperCase()"
                              label="Фамилия"/>
                <v-menu ref="menu" v-model="birthDayMenu" :max-width="290" :close-on-content-click="false"
                        transition="scale-transition">
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field :error-messages="birthdateErrors" v-model="changed_document.birthdate" v-bind="attrs"
                                  v-on="on"
                                  label="Дата рождения"
                                  prepend-icon="mdi-calendar"
                                  readonly/>
                  </template>
                  <v-date-picker :max="new Date().toJSON().slice(0,10)" v-model="changed_document.birthdate" no-title
                                 scrollable>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="birthDayMenu = false">Отмена</v-btn>
                    <v-btn color="primary" text @click="birthDayMenu = false">OK</v-btn>
                  </v-date-picker>
                </v-menu>
                <v-text-field counter="4" v-model="changed_document.series" :error-messages="seriesErrors"
                              label="Серия документа"
                              maxlength="4"/>
                <v-text-field counter="6" v-model="changed_document.number" :error-messages="numberErrors"
                              label="Номер документа"
                              maxlength="6"/>
                <v-btn class="mr-4" type="submit">Применить изменения</v-btn>
              </form>
            </v-card>
          </v-tab-item>

          <v-tab-item>
            <v-card flat>
              <v-card-text class="text-center">
                <p v-if="bookedTours.length === 0">Ваш список туров пуст</p>
                <div v-else>
                  <favorite-card v-for="tour in bookedTours" :key="tour.tour" :tour="tour"/>
                </div>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-col>

    <v-snackbar top v-model="updated">Данные пользователя обновлены</v-snackbar>
  </div>
</template>

<script>
import {required, minLength, numeric, email} from "vuelidate/lib/validators";
import {mapGetters} from "vuex";
import FavoriteCardComponent from "@/components/FavoriteCardComponent";

export default {
  name: "AccountPage",
  components: {
    'favorite-card': FavoriteCardComponent
  },
  data() {
    return {
      birthDayMenu: false,
      updated: false,
      user: {
        username: null,
        email: null,
      },
      document: {
        firstname: null,
        lastname: null,
        type: null,
        series: null,
        number: null,
        birthdate: null,
      },
      new_email: null,
      changed_document: {
        firstname: null,
        lastname: null,
        type: null,
        series: null,
        number: null,
        birthdate: null,
      },
      invalidUser: false,
      bookedTours: [],
    }
  },
  validations: {
    new_email: {
      required,
      email
    },
    changed_document: {
      firstname: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
        numbers: (v) => !(/[0-9]/.test(v)),
      },
      lastname: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
        numbers: (v) => !(/[0-9]/.test(v)),
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
      },
      birthdate: {
        required,
      },
      type: {
        required,
      }
    }
  },
  computed: {
    ...mapGetters(['getDocumentTypes', 'getDocumentType', 'getDocumentId']),
    firstnameErrors() {
      let mess = ''
      if (!this.$v.changed_document.firstname.$dirty) return mess
      if (!this.$v.changed_document.firstname.required) mess = 'Введите имя'
      else if (!this.$v.changed_document.firstname.ruLetter) mess = 'Укажите имя на латинице'
      else if (!this.$v.changed_document.firstname.numbers) mess = 'Имя содержит цифры'

      return mess
    },
    lastnameErrors() {
      let mess = ''
      if (!this.$v.changed_document.lastname.$dirty) return mess
      if (!this.$v.changed_document.lastname.required) mess = 'Введите фамилию'
      else if (!this.$v.changed_document.lastname.ruLetter) mess = 'Укажите фамилию на латинице'
      else if (!this.$v.changed_document.lastname.numbers) mess = 'Фамилия содержит цифры'

      return mess
    },
    emailErrors() {
      let mess = ''
      if (!this.$v.new_email.$dirty) return mess
      if (!this.$v.new_email.required) mess = 'Введите email'
      else if (!this.$v.new_email) mess = 'Введён неверный email'

      return mess
    },
    seriesErrors() {
      let mess = ''
      if (!this.$v.changed_document.series.$dirty) return mess
      if (!this.$v.changed_document.series.required) mess = 'Введите серию документа'
      else if (!this.$v.changed_document.series.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.changed_document.series.minLength) mess = 'Введите 4 цифры'

      return mess
    },
    numberErrors() {
      let mess = ''
      if (!this.$v.changed_document.number.$dirty) return mess
      if (!this.$v.changed_document.number.required) mess = 'Введите номер документа'
      else if (!this.$v.changed_document.number.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.changed_document.number.minLength) mess = 'Введите 6 цифр'

      return mess
    },
    birthdateErrors() {
      let mess = ''
      if (!this.$v.changed_document.birthdate.$dirty) return mess
      if (!this.$v.changed_document.birthdate.required) mess = 'Введите дату рождения'

      return mess
    },
    documentTypeErrors() {
      let mess = ''
      if (!this.$v.changed_document.type.$dirty) return mess
      if (!this.$v.changed_document.type.required) mess = 'Введите тип документа'

      return mess
    }
  },
  methods: {
    updateUserInfo() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.patchUserInfo()
      }
    },
    patchUserInfo() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      const document = {...this.changed_document}
      document.type = this.getDocumentId(this.changed_document.type)

      this.axios.patch('api/user-profile/', {email: this.new_email}, conf)
          .catch(err => console.log(err))

      this.axios.patch('api/documents/', document, conf)
          .catch(err => console.log(err))

      this.updated = true
      this.user.email = this.new_email
      this.document = {...this.changed_document}
    }
  },
  created() {
    const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
    this.axios.get('api/user-profile/', conf)
        .then(res => {
          if (res.statusText === 'OK') {
            this.user = res.data
            this.new_email = res.data.email
          }
        })

    this.axios.get('api/documents/', conf)
        .then(res => {
          if (res.data.length > 0) {
            this.document = {...res.data[0]}
            this.document.type = this.getDocumentType(res.data[0].type)

            this.changed_document = {...this.document}
          }
        })

    this.axios.get('api/booked-tours/', conf)
        .then(res => {
          if (res.data.length > 0)
            this.bookedTours = res.data
        })
  }
}
</script>

<style scoped>
tr:hover {
  background-color: white !important;
}
</style>
