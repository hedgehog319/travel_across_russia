<template>
  <form novalidate class="container mw-400" @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Вход</div>
      </md-card-header>

      <md-card-content>
        <span class="md-body-1 error" v-if="invalidUser">Неверный логин или пароль</span>

        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('login')">
              <label for="login">Login</label>
              <md-input name="login" id="login" autocomplete="given-name" v-model="form.login"
                        :disabled="sending"/>
              <span class="md-error" v-if="!$v.form.login.required">Необходимо указать логин</span>
            </md-field>
          </div>

          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('password')">
              <label for="password">Пароль</label>
              <md-input type="password" name="password" id="password" autocomplete="password"
                        v-model="form.password"></md-input>
              <span class="md-error" v-if="!$v.form.password.required">Введите пароль</span>
            </md-field>
          </div>
        </div>
      </md-card-content>

      <md-progress-bar md-mode="indeterminate" v-if="sending"/>

      <md-card-actions>
        <md-button type="submit" class="md-primary" :disabled="sending">Войти</md-button>
      </md-card-actions>
      <router-link to="register">Зарегистрироваться</router-link>
    </md-card>
  </form>
</template>

<script>
import axios from 'axios';
import {required} from 'vuelidate/lib/validators';

// TODO убирать "неверный логин или пароль" при вводе
export default {
  name: "Login",
  data: () => ({
    form: {
      login: null,
      password: null
    },
    invalidUser: false,
    sending: false,
  }),
  validations: {
    form: {
      login: {
        required,
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
        };
      }
    },
    clearForm() {
      this.$v.$reset()
      this.form.email = null
      this.form.password = null
    },
    checkUser() {
      this.sending = true

      // TODO поправить запрос
      const http = axios.create({baseURL: 'http://127.0.0.1:8000/'});
      http.get(`/api/users/?login=${this.form.login}`)
          .then((response) => {
            if (response.data.length !== 0) {
              if (response.data[0].password === this.form.password) {
                console.log('ok');
              } else {
                this.invalidUser = true
              }
            } else {
              this.invalidUser = true
            }
            this.sending = false
          });
    },
    validateUser() {
      this.$v.$touch()

      if (!this.$v.$invalid) {
        this.checkUser()
      }
    }
  }
}

</script>

<style lang="scss" scoped>

.error {
  color: #ff1744;
}

</style>