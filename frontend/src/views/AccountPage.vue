<template>
  <v-app id="account">
    <v-main>
      <v-container style="width: 50%;margin: auto">
        <v-card>
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Профиль</v-toolbar-title>
          </v-toolbar>
          <v-tabs vertical>
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
                      <th class="text-left"></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                      <td>Логин</td>
                      <td>testlogin</td>
                    </tr>
                    <tr>
                      <td>Имя</td>
                      <td>имя</td>
                    </tr>
                    <tr>
                      <td>Фамилия</td>
                      <td>фамилия</td>
                    </tr>
                    <tr>
                      <td>Email</td>
                      <td>test@mail.ru</td>
                    </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-card>
            </v-tab-item>
            <!-- TODO validation -->
            <v-tab-item>
              <v-card flat>
                <form style="margin: 15px" @submit.prevent="updateUserInfo">
                  <h2>Изменение профиля</h2>
                  <v-text-field v-model="user.username" :error-messages="usernameErrors"
                                label="Логин"
                                @input="inputHandler('username')"
                  /> <!--@keydown.space.prevent - перехватывает пробел-->
                  <v-text-field v-model="user.firstname" :error-messages="firstnameErrors"
                                label="Имя"
                                @input="inputHandler('firstname')"/>
                  <v-text-field v-model="user.lastname" :error-messages="lastnameErrors" label="Фамилия" required
                                @input="inputHandler('lastname')"/>
                  <v-text-field v-model="user.email" :error-messages="emailErrors"
                                label="Email"
                                @keydown.space.prevent="null"/>
                  <v-btn class="mr-4" style="margin-left: 20%;" type="submit">Принять изменения</v-btn>
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
      </v-container>
    </v-main>
  </v-app>
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
      invalidUser: false
    }
  },
  validations: {
    user: {
      username: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      firstname: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
        enLetter: (value) => !(/[a-z]/.test(value) || / [A-Z]/.test(value)),
      },
      lastname: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
        enLetter: (value) => !(/[a-z]/.test(value) || / [A-Z]/.test(value)),
      },
      email: {
        required,
      }
    }
  },
  computed: {
    usernameErrors() {
      let mess = ''
      if (!this.$v.user.username.$dirty) return mess
      if (!this.$v.user.username.required) mess = 'Введите логин'
      else if (!this.$v.user.username.ruLetter) mess = 'Логин не должен содержать русскх букв'

      return mess
    },
    firstnameErrors() {
      let mess = ''
      if (!this.$v.user.firstname.$dirty) return mess
      if (!this.$v.user.firstname.required) mess = 'Введите имя'
      else if (!this.$v.user.firstname.ruLetter && !this.$v.user.firstname.enLetter) {
        mess = 'Логин должен содержать или кириллицу, или латиницу'
      }

      return mess
    },
    lastnameErrors() {
      let mess = ''
      if (!this.$v.user.lastname.$dirty) return mess
      if (!this.$v.user.lastname.required) mess = 'Введите фамилию'
      else if (!this.$v.user.lastname.ruLetter && !this.$v.user.lastname.enLetter) {
        mess = 'Логин должен содержать или кириллицу, или латиницу'
      }

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
  }
}
</script>

<style scoped>

tr:hover {
  background-color: white !important;
}

</style>