<template>
  <div id="footer">
    <v-footer default padless class="unselectable" dark>
      <v-card class="lighten-1 white--text text-center" flat tile width="100%">
        <v-card-text>
          <v-btn v-for="icon in icons" :key="icon" class="mx-4 white--text" icon>
            <v-icon size="24px"> {{ icon }}</v-icon>
          </v-btn>
        </v-card-text>

        <v-divider/>

        <v-card-text class="white--text">{{ new Date().getFullYear() + " - Путешествуй по России" }}</v-card-text>
      </v-card>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "FooterComponent",
  data: () => ({
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-vk',
      'mdi-instagram',
    ],
  }),
}
</script>

<style scoped>

</style>