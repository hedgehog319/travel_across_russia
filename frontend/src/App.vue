<template>
  <v-app>
    <router-view/>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import '@/assets/styles/my-style.sass'

export default {
  name: 'App',

  components: {
    // HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
