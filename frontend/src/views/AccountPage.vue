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
                    <td>{{ user.firstname }}</td>
                  </tr>
                  <tr>
                    <td>Фамилия</td>
                    <td>{{ user.lastname }}</td>
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
                <v-text-field v-model="user.email" :error-messages="emailErrors"
                              label="Email"
                              @keydown.space.prevent=""/>
                <v-select :items="documents" v-model="document"/>
                <v-text-field v-model="user.firstname" :error-messages="firstnameErrors"
                              label="Имя"
                              @input="inputHandler('firstname')"/>
                <v-text-field v-model="user.lastname" :error-messages="lastnameErrors" label="Фамилия" required
                              @input="inputHandler('lastname')"/>
                <v-text-field v-model="user.lastname" :error-messages="lastnameErrors" label="Серия паспорта" required
                              @input="inputHandler('lastname')"/>
                <v-text-field v-model="user.lastname" :error-messages="lastnameErrors" label="Номер паспорта" required
                              @input="inputHandler('lastname')"/>
                <v-btn class="mr-4" type="submit">Принять изменения</v-btn>
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
import {required} from "vuelidate/lib/validators";

export default {
  name: "AccountPage",
  data() {
    return {
      user: {
        username: null,
        firstname: null,
        lastname: null,
        email: null,
      },
      invalidUser: false,
      document: 'Паспорт',
      documents: ['Паспорт', 'Заграничный паспорт']
    }
  },
  validations: {
    user: {
      firstname: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      lastname: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      email: {
        required,
      }
    }
  },
  computed: {
    firstnameErrors() {
      let mess = ''
      if (!this.$v.user.firstname.$dirty) return mess
      if (!this.$v.user.firstname.required) mess = 'Введите имя'
      else if (!this.$v.user.firstname.ruLetter) mess = 'Укажите имя на латинице'

      return mess
    },
    lastnameErrors() {
      let mess = ''
      if (!this.$v.user.lastname.$dirty) return mess
      if (!this.$v.user.lastname.required) mess = 'Введите фамилию'
      else if (!this.$v.user.lastname.ruLetter) mess = 'Укажите фамилию на латинице'

      return mess
    },
    emailErrors() {
      let mess = ''
      if (!this.$v.user.email.$dirty) return mess
      if (!this.$v.user.email.required) mess = 'Введите email'
      else if (!this.$v.user.email.email) mess = 'Введён неверный email'

      return mess
    },
  },
  methods: {
    updateUserInfo() {
      this.$v.$touch()

      if (!this.$v.$invalid) {

      }
    },
    inputHandler(field) {
      this.invalidUser = false
      this.$v.user[field].$touch()
    }
  },
  created() {
    const conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}
    // const res = this.axios.get('api/documents/', conf)
    // console.log(res)
    this.axios.get('api/documents/', conf)
        .then(res => {
          console.log(res)
        })
  }
}
</script>

<style scoped>

tr:hover {
  background-color: white !important;
}

</style>