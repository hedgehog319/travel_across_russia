<template>
  <div id="footer">
    <v-footer dark padless absolute>
      <v-card flat tile width="100%"
              class="indigo lighten-1 white--text text-center">
        <v-card-text>
          <v-btn v-for="icon in icons" :key="icon"
                 class="mx-4 white--text" icon>
            <v-icon size="24px"> {{ icon }}</v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          Путешествуй по России - курсовой проект
        </v-card-text>

        <v-divider/>

        <v-card-text class="white--text">{{ new Date().getFullYear() }}</v-card-text>
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
      'mdi-linkedin',
      'mdi-instagram',
    ],
  }),
}
</script>

<style scoped>

</style>