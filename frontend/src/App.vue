<template>
  <v-app>
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
  methods: mapActions(['fetchCities', 'fetchTours']),
  created() {
    let conf
    if (this.$cookies.isKey('Token'))
      conf = {headers: {Authorization: 'JWT ' + this.$cookies.get('Token')}}

    this.fetchCities()
    this.fetchTours(conf)
  },
};
</script>

<style>
.router {
  padding-top: 64px;
  padding-bottom: 100px;
  height: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-image: url('./assets/img/bg.jpg')
}
</style>
