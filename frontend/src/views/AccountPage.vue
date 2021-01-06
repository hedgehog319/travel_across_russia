<template>
  <v-app id="account">
    <v-main>
      <v-container style="width: 60%;">
        <v-card>
          <v-toolbar flat color="primary" dark>
            <v-toolbar-title>Имя Фамилия</v-toolbar-title>
          </v-toolbar>
          <v-tabs vertical>
            <v-tab>Информация</v-tab>
            <v-tab>Избранное</v-tab>
            <v-tab>Мои туры</v-tab>

            <v-tab-item>
              <v-card flat>
                <v-simple-table style="margin: 10px;">
                  <template v-slot:default>
                    <thead class="hover-none">
                    <tr>
                      <th class="text-left" style="font-size: 30px">
                        Аккаунт
                      </th>
                      <th class="text-left"></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr class="hover-none">
                      <td>Логин</td>
                      <td>testlogin</td>
                    </tr>
                    <tr class="hover-none">
                      <td>Имя</td>
                      <td>имя</td>
                    </tr>
                    <tr class="hover-none">
                      <td>Фамилия</td>
                      <td>фамилия</td>
                    </tr>
                    <tr class="hover-none">
                      <td>Email</td>
                      <td>test@mail.ru</td>
                    </tr>
                    <tr class="hover-none">
                      <td>Данные паспорта</td>
                      <td>1313123123</td>
                    </tr>
                    </tbody>
                  </template>
                </v-simple-table>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text style="text-align: center">
                  <p>Ваш список избранного пуст</p>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text style="text-align: center">
                  <p>
                    Ваш список туров пуст
                  </p>
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
export default {
  name: "AccountPage",
  data: () => ({
  }),
}
</script>

<style scoped>

</style>