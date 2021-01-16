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
          <template v-slot:activator="{ on: menu, attrs }" class="scrollbar">
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
            <v-list-item v-for="city in getCities" :key="city.id" @click="selectedItem(city)">
              <v-list-item-title>{{ city.name }}</v-list-item-title>
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

      <router-link v-if="isAuthorized" class="text-decoration-none hover" to="/favorites">
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
        <v-menu v-if="isAuthorized && !isSmall" offset-y>
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
            <v-list-item @click="$router.push({name: 'account'}).catch(()=>{})">
              <v-list-item-title>Личные данные</v-list-item-title>
            </v-list-item>

            <v-list-item link>
              <v-dialog v-model="dialog" width="500">
                <template v-slot:activator="{ on, attrs }">
                  <v-list-item-title v-bind="attrs" v-on="on"
                                     style="color: red; width: 120px">Выйти
                  </v-list-item-title>
                </template>

                <v-card>
                  <v-card-title class="headline grey lighten-2">Выход</v-card-title>
                  <v-card-text style="margin-top: 15px">
                    Вы действительно хотите выйти?
                  </v-card-text>
                  <v-divider/>
                  <v-card-actions>
                    <v-spacer/>
                    <v-btn color="red" text @click="dialog = false">Нет</v-btn>
                    <v-btn color="primary" text @click="logout">Да</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-list-item>
          </v-list>
        </v-menu>

        <!--TODO поправить на малом экране-->
        <div v-else-if="!isAuthorized && !isSmall">
          <v-btn elevation="0" class="round" color="primary" style="margin-right: 2px"
                 @click="$router.push({name: 'login'}).catch(()=>{})">Войти
          </v-btn>
          <v-btn elevation="0" class="round" color="primary" style="margin-left: 2px"
                 @click="$router.push({name: 'registration'}).catch(() => {})">Регистрация
          </v-btn>
        </div>

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

          <router-link v-if="isAuthorized && isSmall"
                       class="text-decoration-none hover" to="/account">
            <v-list-item>
              <v-icon>mdi-account-box-outline</v-icon>
              <v-list-item-title style="margin-left: 5px" class="text-subtitle-1">Профиль</v-list-item-title>
            </v-list-item>
          </router-link>

          <div v-else-if="!isAuthorized && isSmall">
            <v-list-item>
              <v-icon>mdi-login</v-icon>
              <v-list-item-title style="margin-left: 5px" class="text-subtitle-1"
                                 @click="this.$router.push({name: 'login'}).catch(()=>{})">
                Войти
              </v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-icon>mdi-account-plus</v-icon>
              <v-list-item-title style="margin-left: 5px" class="text-subtitle-1"
                                 @click="$router.push({name: 'registration'}).catch(() => {})">Регистрация
              </v-list-item-title>
            </v-list-item>
          </div>

          <router-link v-if="isAuthorized" class="text-decoration-none hover" to="/favorites">
            <v-list-item>
              <v-icon>mdi-heart-outline</v-icon>
              <v-list-item-title style="margin-left: 5px" class="text-subtitle-1">Избранное</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link class="text-decoration-none hover" to="/search">
            <v-list-item>
              <v-icon>mdi-map-search-outline</v-icon>
              <v-list-item-title style="margin-left: 5px" class="text-subtitle-1">Поиск тура</v-list-item-title>
            </v-list-item>
          </router-link>
          <router-link class="text-decoration-none hover" to="/booking">
            <v-list-item>
              <v-icon>mdi-book-plus</v-icon>
              <v-list-item-title style="margin-left: 5px" class="text-subtitle-1">Бронирование тура</v-list-item-title>
            </v-list-item>
          </router-link>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: "NavbarComponent",
  data() {
    return {
      dialog: false,
      isSmall: false,
      currentCity: "Владивосток",
      drawer: false,
      group: null,
    }
  },
  computed: {
    ...mapGetters(['getCities']),
    isAuthorized() {
      return this.$cookies.isKey('Token')
    }
  },
  methods: {
    selectedItem(city) {
      this.currentCity = city
    },
    onResize() {
      this.isSmall = window.innerWidth < 800
    },
    logout() {
      this.dialog = false
      this.$cookies.remove('Token')
      this.$router.push({name: 'home'})
    }
  },
  beforeDestroy() {
    if (typeof window === 'undefined') return

    window.removeEventListener('resize', this.onResize, {passive: true})
  },
  mounted() {
    this.onResize()
    window.addEventListener('resize', this.onResize, {passive: true})
  }
}
</script>

<style scoped>

</style>