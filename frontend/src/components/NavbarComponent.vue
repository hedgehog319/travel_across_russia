<template>
  <div id="navbar">
    <v-app-bar absolute color="white">
      <v-toolbar-title v-if="isSmall">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>
      </v-toolbar-title>
      <router-link class="text-decoration-none hover" to="/">
        <v-toolbar-title v-if="!isSmall">
          <v-img max-height="100" max-width="180" src="@/assets/logo.jpg"/>
        </v-toolbar-title>
      </router-link>

      <v-spacer/>

      <div class="text-center">
        <v-menu v-if="!isSmall" offset-y rounded="b-xl">
          <template v-slot:activator="{ on: menu, attrs }">
            <v-tooltip bottom>
              <template v-slot:activator="{ on: tooltip }">
                <v-btn v-bind="attrs" v-on="{ ...tooltip, ...menu }" color="white" elevation="0">
                  <v-icon>mdi-map-marker</v-icon>
                  {{ currentCity }}
                </v-btn>
              </template>
              <span>Выбрать город</span>
            </v-tooltip>
          </template>
          <v-list>
            <v-list-item v-for="(city, index) in cities" :key="index" @click="selectedItem(city)">
              <v-list-item-title>{{ city }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>

      <router-link class="text-decoration-none hover" to="/booking">
        <v-tooltip v-if="!isSmall" bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" elevation="0" icon style="background: #FFFFFF; width: 50px">
              <v-icon color="black" dark large style="margin: 10px">mdi-book-plus</v-icon>
            </v-btn>
          </template>
          <span>Бронирование тура</span>
        </v-tooltip>
      </router-link>

      <router-link class="text-decoration-none hover" to="/search">
        <v-tooltip v-if="!isSmall" bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" elevation="0" icon style="background: #FFFFFF; width: 50px">
              <v-icon color="black" dark large style="margin: 10px">mdi-map-search</v-icon>
            </v-btn>
          </template>
          <span>Поиск тура</span>
        </v-tooltip>
      </router-link>

      <router-link class="text-decoration-none hover" to="/favorites">
        <v-tooltip v-if="!isSmall" bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" elevation="0" icon style="background: #FFFFFF; width: 50px">
              <v-icon color="black" dark large style="margin: 10px">mdi-heart-outline</v-icon>
            </v-btn>
          </template>
          <span>Избранное</span>
        </v-tooltip>
      </router-link>

      <div class="text-center">
        <v-menu v-if="isLogin && !isSmall" offset-y>
          <template v-slot:activator="{ on: menu, attrs }">
            <v-tooltip bottom>
              <template v-slot:activator="{ on: tooltip }">
                <v-btn v-bind="attrs" v-on="{ ...tooltip, ...menu }" icon>
                  <v-icon size="40px">mdi-account-circle</v-icon>
                </v-btn>
              </template>
              <span>Профиль</span>
            </v-tooltip>
          </template>
          <v-list>
            <router-link class="text-decoration-none" to="/account">
              <v-list-item>
                <v-list-item-title>Личные данные</v-list-item-title>
              </v-list-item>
            </router-link>
            <!-- TODO выход из аккаунта -->
            <v-list-item>
              <div>
                <v-dialog v-model="dialog" width="500">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn v-bind="attrs" v-on="on" dark elevation="0"
                           style="background: #FFFFFF; color: red; width: 120px">
                      Выйти
                    </v-btn>
                  </template>

                  <v-card>
                    <v-card-title class="headline grey lighten-2">
                      Выход
                    </v-card-title>
                    <v-card-text style="margin-top: 15px">
                      Вы действительно хотите выйти?
                    </v-card-text>
                    <v-divider/>
                    <v-card-actions>
                      <v-spacer/>
                      <v-btn color="red" text @click="dialog = false">Нет</v-btn>
                      <v-btn color="primary" text @click="dialog = false">Да</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
            </v-list-item>
          </v-list>
        </v-menu>
        <v-tooltip v-if="!isLogin && !isSmall" bottom>
          <template v-slot:activator="{ on, attrs }">
            <router-link class="text-decoration-none hover" to="/login">
              <v-btn v-bind="attrs" v-on="on" elevation="0" style="background: #FFFFFF; width: 50px">
                Войти
              </v-btn>
            </router-link>
          </template>
          <span>Вход в аккаунт</span>
        </v-tooltip>

        <router-link class="text-decoration-none hover" to="/">
          <v-toolbar-title v-if="isSmall">
            <v-img max-height="100" max-width="180" src="@/assets/logo.jpg"/>
          </v-toolbar-title>
        </router-link>

      </div>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute left temporary>
      <v-list dense nav>
        <v-list-item-group v-model="group" active-class=" text--accent-4">
          <router-link class="text-decoration-none hover" to="/account">
            <v-list-item>
              <v-list-item-title>Профиль</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link class="text-decoration-none hover" to="/favorites">
            <v-list-item>
              <v-list-item-title>Избранное</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link class="text-decoration-none hover" to="/search">
            <v-list-item>
              <v-list-item-title>Поиск тура</v-list-item-title>
            </v-list-item>
          </router-link>
          <router-link class="text-decoration-none hover" to="/booking">
            <v-list-item>
              <v-list-item-title>Бронирование тура</v-list-item-title>
            </v-list-item>
          </router-link>
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
      dialog: false,
      // TODO заменить на cookie
      isLogin: true,
      isSmall: false,
      currentCity: "Владивосток",
      cities: ['Владивосток', 'Москва', 'Казань', 'Ростов-на-Дону', 'Уфа'],
      drawer: false,
      group: null,
    }
  },
  methods: {
    selectedItem(city) {
      this.currentCity = city
    },
    onResize() {
      this.isSmall = window.innerWidth < 600
    }
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