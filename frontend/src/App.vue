<template>
  <v-app class="bg">
    <NavbarComponent/>
    <router-view class="router"/>
    <FooterComponent/>
  </v-app>
</template>

<script>
import {mapActions} from 'vuex'
import NavbarComponent from "@/components/NavbarComponent";
import FooterComponent from "@/components/FooterComponent";
import '@/assets/styles/my-style.css'

export default {
  name: 'App',
  components: {
    FooterComponent,
    NavbarComponent,
  },
  methods: mapActions(['fetchCities', 'fetchDocumentTypes', 'fetchTopTours']),
  created() {

    this.fetchCities()
    this.fetchDocumentTypes()
    this.fetchTopTours(12)
  },
};
</script>

<style>
.router {
  margin: 5px;
  height: 100%;
  padding-top: 60px;
  padding-bottom: 100px;
}

.bg {
  background-image: url('./assets/img/bg.jpg') !important;
  background-size: cover !important;
  background-attachment: fixed !important;
}
</style>
