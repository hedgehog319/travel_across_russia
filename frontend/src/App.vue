<template>
  <v-app>
    <NavbarComponent/>
    <router-view
        style="
        padding-top: 64px;
        padding-bottom: 100px;
        height: 100%;
        background-size: cover;
        background-repeat: no-repeat;
         background-image: url('https://wallbox.ru/resize/1920x1080/wallpapers/main/201548/f66296165537f2c.jpg')"/>
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
  methods: mapActions(['fetchCities']),
  created() {
    this.fetchCities()
  },
};
</script>
