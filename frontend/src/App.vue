<template>
  <v-app>
    <NavbarComponent/>
    <router-view
        style="
        padding-top: 100px;
        padding-bottom: 50px;
        height: 100%;
        margin-bottom: 100px;
        background-size: cover;
        background-repeat: no-repeat;
         background-image: url('https://wallbox.ru/resize/1920x1080/wallpapers/main/201548/f66296165537f2c.jpg')"/>
    <FooterComponent/>
  </v-app>
</template>

<script>
import '@/assets/styles/my-style.css'
import NavbarComponent from "@/components/NavbarComponent";
import FooterComponent from "@/components/FooterComponent";

export default {
  name: 'App',

  components: {
    FooterComponent,
    NavbarComponent,
  },
};
</script>
