<template>
  <form novalidate class="container mw-400" @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Регистрация</div>
      </md-card-header>

      <md-card-content>
        <div class="md-layout-item md-small-size-100">
          <md-field :class="getValidationClass('login')">
            <label for="login">Логин</label>
            <md-input name="first-name" id="login" autocomplete="given-name" v-model="form.login"
                      :disabled="sending"/>
            <span class="md-error" v-if="!$v.form.login.required">Введите логин</span>
            <span class="md-error" v-else-if="!$v.form.login.minlength">Логин должен быть больше 3 символов</span>
            <span class="md-error" v-else-if="!$v.form.login.maxlength">Логин должен быть меньше 20 символов</span>
          </md-field>
        </div>

        <md-field :class="getValidationClass('email')">
          <label for="email">Email</label>
          <md-input type="email" name="email" id="email" autocomplete="email" v-model="form.email"
                    :disabled="sending"/>
          <span class="md-error" v-if="!$v.form.email.required">Введите email</span>
          <span class="md-error" v-else-if="!$v.form.email.email">Неверный email</span>
        </md-field>

        <div class="md-layout-item md-small-size-100">
          <md-field :class="getValidationClass('password')">
            <label for="password">Пароль</label>
            <md-input type="password" name="password" id="password" autocomplete="password"
                      v-model="form.password"></md-input>
            <span class="md-error" v-if="!$v.form.password.required">Введите пароль</span>
          </md-field>
        </div>
      </md-card-content>

      <md-progress-bar md-mode="indeterminate" v-if="sending"/>

      <md-card-actions>
        <md-button type="submit" class="md-primary" :disabled="sending">Создать</md-button>
      </md-card-actions>
    </md-card>

    <md-snackbar :md-active.sync="userSaved">Пользователь {{ form.login }} успешно создан!</md-snackbar>
  </form>
</template>

<script lang="js">
import {validationMixin} from 'vuelidate'
import axios from 'axios'
import {
  required,
  email,
  minLength,
  maxLength,
} from 'vuelidate/lib/validators'

export default {
  name: 'Registration',
  mixins: [validationMixin],
  data: () => ({
    form: {
      login: null,
      email: null,
      password: null
    },
    userSaved: false,
    sending: false,
    lastUser: null
  }),
  validations: {
    form: {
      login: {
        required,
        minlength: minLength(3),  // TODO проверить минимальное кол-во символов
        maxLength: maxLength(20)  // TODO проверить максимальное кол-во символов
      },
      email: {
        required,
        email
      },
      password: {
        required
      }
    }
  },
  methods: {
    getValidationClass(fieldName) {
      const field = this.$v.form[fieldName]

      if (field) {
        return {
          'md-invalid': field.$invalid && field.$dirty
        }
      }
    },
    clearForm() {
      this.$v.$reset()
      this.form.login = null
      this.form.email = null
      this.form.password = null
    },
    saveUser() {
      this.sending = true

      const post = {
        'login': this.form.login,
        'access_right': 0,
        'password': this.form.password
      }

      const http = axios.create({baseURL: 'http://localhost:8000/'});
      http.post('/api/users/', post)
          .then((response) => {
            console.log(response)
            if (response.statusText === "Created") { // status code 201
              this.sending = false
              this.userSaved = true
            }
          })
          .catch((error) => {
            console.log(error);
          });
      // TODO проверка на наличие логина
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.saveUser()
      }
    },
  }
}
</script>

<style lang="scss" scoped>
.md-progress-bar {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
}
</style>