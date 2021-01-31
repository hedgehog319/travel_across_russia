<template>
  <div id="notfound">
    <v-container>
      <v-sheet class="rounded unselectable pa-12 ma-auto text-center" max-width="600px">
        <p class="text-h2">404</p>
        <p class="text-h4">Данной страницы не существует</p>
        <router-link to="/" class="text-decoration-none">
          <v-btn>Вернуться домой</v-btn>
        </router-link>
      </v-sheet>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "NotFoundPage"
}
</script>

<style scoped>

</style>