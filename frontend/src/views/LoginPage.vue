<template>
  <div id="login">
    <v-form @submit.prevent="validateUser">
      <v-container class="mw-400">
        <v-card class="round" elevation="2">
          <v-card-title class="text-center">Вход</v-card-title>
          <span v-if="invalidUser" class="text-center error--text unselectable"
                style="position: absolute; left: 77px; top: 50px">Неверный логин или пароль</span>

          <v-container>
            <v-text-field v-model="user.username" :error-messages="usernameErrors"
                          label="Логин"
                          @input="inputHandler('username')"
                          @keydown.space.prevent=""/> <!--@keydown.space.prevent - перехватывает пробел-->
            <v-text-field v-model="user.password" :error-messages="passwordErrors"
                          :type="showPassword ? 'text' : 'password'"
                          label="Пароль"
                          @input="inputHandler('password')"
                          @keydown.space.prevent=""/>
            <v-btn icon style="position: absolute; left: auto; right: 10px; top: auto; bottom: 144px"
                   @click="showPassword = !showPassword">
              <v-icon>{{ showPassword ? 'mdi-eye' : 'mdi-eye-off' }}</v-icon>
            </v-btn>
          </v-container>
          <v-card-actions>
            <v-container class="text-center">
              <v-btn block class="rounded-pill primary" elevation="0" type="submit">Войти</v-btn>
              <div style="margin-top: 10px">
                <span>Нет аккаунта? </span>
                <router-link class="text-decoration-none blue--text text--darken-2 hover" to="/registration">
                  Зарегистрируйся
                </router-link>
              </div>
            </v-container>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import {required} from 'vuelidate/lib/validators';

export default {
  name: "LoginPage",
  data() {
    return {
      user: {
        username: null,
        password: null
      },
      showPassword: false,
      invalidUser: false
    }
  },
  validations: {
    user: {
      username: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      password: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
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
    passwordErrors() {
      let mess = ''
      if (!this.$v.user.password.$dirty) return mess
      if (!this.$v.user.password.required) mess = 'Введите пароль'
      else if (!this.$v.user.password.ruLetter) mess = 'Пароль не должен содержать русскх букв'

      return mess
    }
  },
  methods: {
    async checkUser() {
      let authorized = false
      await this.axios.post(`/auth/jwt/create/`, this.user).then(
          res => {
            if (res.statusText === 'OK') {  // status === 200
              this.$cookies.set('Token', res.data.access)
              authorized = true
            }
          }
      ).catch((err) => {
        if (err.response.statusText === 'Unauthorized') { // status === 401
          this.invalidUser = true
        }
      })

      if (authorized) {
        await this.$router.push({name: 'home'})
      }
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.checkUser()
      }
    },
    inputHandler(field) {
      this.invalidUser = false
      this.$v.user[field].$touch()
    }
  }
}
</script>

<style lang="sass" scoped>

</style>