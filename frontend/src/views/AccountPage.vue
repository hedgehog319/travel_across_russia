<template>
  <div id="account">
    <v-col style="margin: auto" cols="12" md="6">
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
              <v-simple-table style="margin: 10px;">
                <template v-slot:default>
                  <thead>
                  <tr>
                    <th class="text-left" style="font-size: 30px">Аккаунт</th>
                    <th class="text-left"/>
                  </tr>
                  </thead>
                  <tbody>
                  <tr>
                    <td>Логин</td>
                    <td>{{ user.username }}</td>
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
                    <td>Email</td>
                    <td>{{ user.email }}</td>
                  </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-card>
          </v-tab-item>
          <!-- TODO validation -->
          <v-tab-item>
            <v-card flat class="text-center">
              <form style="margin: 15px" @submit.prevent="updateUserInfo">
                <h2>Изменение профиля</h2>
                <v-text-field v-model="user.email" :error-messages="emailErrors" label="Email"/>
                <v-select :items="typeOfDocuments" v-model="document.name"/>
                <v-text-field v-model="document.firstname" :error-messages="firstnameErrors" label="Имя"/>
                <v-text-field v-model="document.lastname" :error-messages="lastnameErrors" label="Фамилия"/>
                <v-text-field v-model="document.series" :error-messages="seriesErrors" label="Серия документа"
                              maxlength="4"/>
                <v-text-field v-model="document.number" :error-messages="numberErrors" label="Номер документа"
                              maxlength="6"/>
                <v-btn class="mr-4" type="submit">Применить изменения</v-btn>
              </form>
            </v-card>
          </v-tab-item>

          <v-tab-item>
            <v-card flat>
              <v-card-text style="text-align: center">
                <p>Ваш список туров пуст</p>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs>
      </v-card>
    </v-col>
  </div>
</template>

<script>
import {required, minLength, numeric, email} from "vuelidate/lib/validators";

export default {
  name: "AccountPage",
  data() {
    return {
      user: {
        username: null,
        email: null,
      },
      document: {
        firstname: null,
        lastname: null,
        name: 'Паспорт',
        series: null,
        number: null,
      },
      invalidUser: false,
      typeOfDocuments: ['Паспорт', 'Заграничный паспорт']
    }
  },
  validations: {
    user: {
      email: {
        required,
        email
      }
    },
    document: {
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
      }
    }
  },
  computed: {
    firstnameErrors() {
      let mess = ''
      if (!this.$v.document.firstname.$dirty) return mess
      if (!this.$v.document.firstname.required) mess = 'Введите имя'
      else if (!this.$v.document.firstname.ruLetter) mess = 'Укажите имя на латинице'
      else if (!this.$v.document.firstname.numbers) mess = 'Имя содержит цифры'

      return mess
    },
    lastnameErrors() {
      let mess = ''
      if (!this.$v.document.lastname.$dirty) return mess
      if (!this.$v.document.lastname.required) mess = 'Введите фамилию'
      else if (!this.$v.document.lastname.ruLetter) mess = 'Укажите фамилию на латинице'
      else if (!this.$v.document.lastname.numbers) mess = 'Фамилия содержит цифры'

      return mess
    },
    emailErrors() {
      let mess = ''
      if (!this.$v.user.email.$dirty) return mess
      if (!this.$v.user.email.required) mess = 'Введите email'
      else if (!this.$v.user.email.email) mess = 'Введён неверный email'

      return mess
    },
    seriesErrors() {
      let mess = ''
      if (!this.$v.document.series.$dirty) return mess
      if (!this.$v.document.series.required) mess = 'Введите серию документа'
      else if (!this.$v.document.series.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.document.series.minLength) mess = 'Введите 4 цифры'

      return mess
    },
    numberErrors() {
      let mess = ''
      if (!this.$v.document.number.$dirty) return mess
      if (!this.$v.document.number.required) mess = 'Введите номер документа'
      else if (!this.$v.document.number.numeric) mess = 'Вы ввели не число'
      else if (!this.$v.document.number.minLength) mess = 'Введите 6 цифр'

      return mess
    },
  },
  methods: {
    updateUserInfo() {
      this.$v.$touch()
      console.log('befote')
      if (!this.$v.$invalid) {
        console.log('for')
        this.patchUserInfo()
      }
    },
    patchUserInfo() {
      const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
      const data = {
        first_name: this.document.firstname,
        last_name: this.document.lastname,
        series: this.document.series,
        number: this.document.number
      }

      this.axios.patch('api/documents/', data, conf)
          .catch(error => console.log(error))
    }
  },
  created() {
    const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
    this.axios.get('api/documents/', conf)
        .then(res => {
          if (res.data.length > 0) {
            this.document.firstname = res.data[0].first_name
            this.document.lastname = res.data[0].last_name
            this.document.series = res.data[0].series
            this.document.number = res.data[0].number
          }
        })
  }
}
</script>

<style scoped>
tr:hover {
  background-color: white !important;
}
</style>