<template>
  <div id="login">
    <v-form @submit.prevent="">
      <v-container class="mw-400">
        <v-card elevation="2" class="round">
          <v-card-title class="text-center">Вход</v-card-title>
          <v-container>
            <v-text-field label="Логин" :rules="rules" hide-details="auto" class="rounded-pill"/>
            <v-text-field label="Пароль"></v-text-field>
          </v-container>

          <v-card-actions>
            <v-container class="text-center">
              <v-btn elevation="0" block class="rounded-pill primary">Login</v-btn>
              <div style="margin-top: 10px">
                <span>Нет аккаунта? </span>
                <router-link to="/" class="text-decoration-none blue--text text--darken-2 hover">
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

export default {
  name: "LoginPage",
  data() {
    return {
      rules: [
        value => !!value || 'Необходимо заполнить поле',
      ]
    }
  }
}
</script>

<style scoped>

</style>