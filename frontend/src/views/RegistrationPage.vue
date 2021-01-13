<template>
  <div id="registration">
    <v-form @submit.prevent="validateUser">
      <v-container class="mw-400">
        <v-card class="round" elevation="2">
          <v-card-title class="text-center">Регистрация</v-card-title>
          <v-container>
            <v-text-field v-model="form.login" :error-messages="loginErrors"
                          label="Логин"
                          @input="this.$v.form.login.$touch"
                          @keydown.space.prevent="null"/> <!--@keydown.space.prevent - перехватывает пробел-->

            <v-text-field v-model="form.email" :error-messages="emailErrors"
                          label="Email"
                          @keydown.space.prevent="null"/> <!--@keydown.space.prevent - перехватывает пробел-->

            <v-text-field v-model="form.password" :error-messages="passwordErrors"
                          :type="showPassword ? 'text' : 'password'"
                          label="Пароль"
                          @input="this.$v.form.password.$touch"
                          @keydown.space.prevent="null"/>
            <v-btn icon style="position: absolute; left: auto; right: 10px; top: auto; bottom: 144px"
                   @click="showPassword = !showPassword">
              <v-icon>{{ showPassword ? 'mdi-eye' : 'mdi-eye-off' }}</v-icon>
            </v-btn>
          </v-container>
          <v-card-actions>
            <v-container class="text-center">
              <v-btn block class="rounded-pill primary" elevation="0" type="submit">Загрегистрироваться</v-btn>
              <div style="margin-top: 10px">
                <span>Уже зарегистрировались? </span>
                <router-link class="text-decoration-none blue--text text--darken-2 hover" to="/login">
                  Войти
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
import {email, required} from 'vuelidate/lib/validators';

export default {
  name: "RegistrationPage",
  data() {
    return {
      form: {
        login: null,
        email: null,
        password: null
      },
      showPassword: false
    }
  },
  validations: {
    form: {
      login: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      },
      email: {
        required,
        email,
      },
      password: {
        required,
        ruLetter: (value) => !(/[а-я]/.test(value) || /[А-Я]/.test(value)),
      }
    }
  },
  computed: {
    loginErrors() {
      let mess = ''
      if (!this.$v.form.login.$dirty) return mess
      if (!this.$v.form.login.required) mess = 'Введите логин'
      else if (!this.$v.form.login.ruLetter) mess = 'Логин не должен содержать русскх букв'

      return mess
    },
    emailErrors() {
      let mess = ''
      if (!this.$v.form.email.$dirty) return mess
      if (!this.$v.form.email.required) mess = 'Введите email'
      else if (!this.$v.form.email.email) mess = 'Введён неверный email'

      return mess
    },
    passwordErrors() {
      let mess = ''
      if (!this.$v.form.password.$dirty) return mess
      if (!this.$v.form.password.required) mess = 'Введите пароль'
      else if (!this.$v.form.password.ruLetter) mess = 'Пароль не должен содержать русскх букв'

      return mess
    }
  },
  methods: {
    sendUser() {
      // TODO Написать запрос
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.sendUser()
      }
    },
  }
}
</script>

<style scoped>

</style>