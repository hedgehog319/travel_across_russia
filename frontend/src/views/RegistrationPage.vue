<template>
  <div id="registration" class="bg-contain">
    <v-form @submit.prevent="validateUser">
      <v-container class="mw-400">
        <v-card class="round" elevation="2">
          <v-card-title class="text-center">Регистрация</v-card-title>

          <span v-if="invalidUser" class="text-center error--text"
                style="position: absolute; text-align: center; left: 77px; top: 50px; max-width: 214px">
            Пользователь с таким логином уже существует</span>

          <v-container>
            <v-text-field v-model="user.username" :error-messages="usernameErrors"
                          label="Логин"
                          @input="inputHandler('username')"
                          @keydown.space.prevent="null"/> <!--@keydown.space.prevent - перехватывает пробел-->

            <v-text-field v-model="user.email" :error-messages="emailErrors"
                          label="Email"
                          @keydown.space.prevent="null"/> <!--@keydown.space.prevent - перехватывает пробел-->

            <v-text-field v-model="user.password" :error-messages="passwordErrors"
                          :type="showPassword ? 'text' : 'password'"
                          label="Пароль"
                          @input="this.$v.user.password.$touch"
                          @keydown.space.prevent="null"/>
            <v-btn icon style="position: absolute; left: auto; right: 10px; top: auto; bottom: 144px"
                   @click="showPassword = !showPassword">
              <v-icon>{{ showPassword ? 'mdi-eye' : 'mdi-eye-off' }}</v-icon>
            </v-btn>
          </v-container>
          <v-card-actions>
            <v-container class="text-center">
              <v-btn block class="rounded-pill primary" elevation="0" type="submit">Зарегистрироваться</v-btn>

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

    <v-snackbar v-model="saved">Пользователь {{ user.username }} успешно создан</v-snackbar>
  </div>
</template>

<script>
import {email, required} from 'vuelidate/lib/validators';

export default {
  name: "RegistrationPage",
  data() {
    return {
      user: {
        username: null,
        email: null,
        password: null
      },
      showPassword: false,
      invalidUser: false,
      saved: false
    }
  },
  validations: {
    user: {
      username: {
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
    usernameErrors() {
      let mess = ''
      if (!this.$v.user.username.$dirty) return mess
      if (!this.$v.user.username.required) mess = 'Введите логин'
      else if (!this.$v.user.username.ruLetter) mess = 'Логин не должен содержать русскх букв'

      return mess
    },
    emailErrors() {
      let mess = ''
      if (!this.$v.user.email.$dirty) return mess
      if (!this.$v.user.email.required) mess = 'Введите email'
      else if (!this.$v.user.email.email) mess = 'Введён неверный email'

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
    async sendUser() {
      await this.axios.post(`/auth/users/`, this.user).then(res => {
        console.log(res.statusText)
        if (res.statusText === "Created") {
          this.saved = true;
        }
      })
          .catch(() => this.invalidUser = true)
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.sendUser()
      }
    },
    inputHandler(field) {
      this.invalidUser = false
      this.$v.user[field].$touch()
    },
  }
}
</script>

<style scoped>

</style>