<template>
  <form novalidate class="container mw-400" @submit.prevent="validateUser">
    <md-card class="md-layout-item">
      <md-card-header>
        <div class="md-title">Вход</div>
      </md-card-header>

      <md-card-content>
        <div class="md-layout md-gutter">
          <div class="md-layout-item md-small-size-100">
            <md-field :class="getValidationClass('email')">
              <label for="login">Email</label>
              <md-input name="login" id="login" autocomplete="given-name" v-model="form.email"
                        :disabled="sending"/>
              <span class="md-error" v-if="!$v.form.email.required">Необходимо указать email</span>
              <span class="md-error" v-else-if="!$v.form.email.email">Не верный email</span>
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
    </md-card>

    <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!</md-snackbar>
  </form>
</template>

<script>
import {
  required,
  email
} from 'vuelidate/lib/validators'


export default {
  name: "Login",
  data: () => ({
    form: {
      email: null,
      password: null
    },
    userSaved: false,
    sending: false,
    lastUser: null
  }),
  validations: {
    form: {
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
      const field = this.$v.form[fieldName];

      if (field) {
        return {
          'md-invalid': field.$invalid && field.$dirty
        };
      }
    },
    clearForm() {
      this.$v.$reset()
      this.form.email = null;
      this.form.password = null;
    },
    saveUser() {
      this.sending = true;

      // Instead of this timeout, here you can call your API
      window.setTimeout(() => {
        this.lastUser = `${this.form.email} ${this.form.password}`
        this.userSaved = true
        this.sending = false
        this.clearForm()
      }, 1500);
    },
    validateUser() {
      this.$v.$touch();

      if (!this.$v.$invalid) {
        this.saveUser();
      }
    }
  }
}

</script>

<style lang="scss" scoped>

</style>