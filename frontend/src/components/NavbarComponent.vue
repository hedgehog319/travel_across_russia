<template>
  <div id="navbar">
    <v-app-bar absolute color="white"
               scroll-target="#scrolling-techniques-7">
      <v-toolbar-title v-if="isSmall">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </v-toolbar-title>
      <router-link to="/" class="text-decoration-none hover">
        <v-toolbar-title v-if="!isSmall">
          <v-img max-height="100" max-width="180" src="@/assets/logo.jpg"/>
        </v-toolbar-title>
      </router-link>

      <v-spacer/>

      <div class="text-center">
        <v-menu offset-y
                rounded="b-xl">
          <template v-slot:activator="{ on: menu, attrs }">
            <v-tooltip bottom>
              <template v-slot:activator="{ on: tooltip }">
                <v-btn color="white" elevation="0"
                       v-bind="attrs"
                       v-on="{ ...tooltip, ...menu }">
                  <v-icon>mdi-map-marker</v-icon>
                  {{ currentCity }}
                </v-btn>
              </template>
              <span>Выбрать город</span>
            </v-tooltip>
          </template>
          <v-list>
            <v-list-item v-for="(city, index) in cities"
                         :key="index"
                         @click="selectedItem(city)">
              <v-list-item-title>{{ city }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>

      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon elevation="0" style="background: #FFFFFF; width: 50px"
                 v-bind="attrs"
                 v-on="on">
            <v-icon style="margin: 10px" large color="black" dark>
              mdi-heart-outline
            </v-icon>
          </v-btn>
        </template>
        <span>Избранное</span>
      </v-tooltip>

      <div class="text-center">
        <v-menu offset-y>
          <template v-slot:activator="{ on: menu, attrs }">
            <v-tooltip bottom>
              <template v-slot:activator="{ on: tooltip }">
                <v-btn icon
                       v-bind="attrs"
                       v-on="{ ...tooltip, ...menu }">
                  <v-icon size="40px">mdi-account-circle</v-icon>
                </v-btn>
              </template>
              <span>Профиль</span>
            </v-tooltip>
          </template>
          <v-list>
            <v-list-item v-for="(item, index) in profileItems" :key="index">  <!--TODO убрать v-for-->
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </v-app-bar>
    <!--TODO что сюда пихнуть?-->
    <v-navigation-drawer v-model="drawer" absolute left temporary>
      <v-list nav dense>
        <v-list-item-group v-model="group"
                           active-class="deep-purple--text text--accent-4">
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "NavbarComponent",
  data() {
    return {
      isSmall: false,
      currentCity: "Владивосток",
      cities: ['Владивосток', 'Москва', 'Казань', 'Ростов-на-Дону', 'Уфа'],
      profileItems: [{title: 'Личные данные'}, {title: 'Выйти'}],
      drawer: false,
      group: null,
    }
  },
  methods: {
    selectedItem: city => this.currentCity = city,
    onResize: () => this.isSmall = window.innerWidth < 500,
  },
  beforeDestroy() {
    if (typeof window === 'undefined') return // REDO изменить

    window.removeEventListener('resize', this.onResize, {passive: true})
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
  },
  watch: {
    group() {
      this.drawer = false
    },
  },
}
</script>

<style scoped>

</style>