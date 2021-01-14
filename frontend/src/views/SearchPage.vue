<template>
  <v-app id="search">
    <v-container>
      <v-expansion-panels>

        <v-expansion-panel>
          <v-expansion-panel-header>
            <template v-slot:default="{ open }">
              <v-row no-gutters>
                <v-col cols="4">Место отбытия</v-col>
                <v-col class="text--secondary" cols="8">
                  <v-fade-transition leave-absolute>
                    <span v-if="open" :key="0">Владивосток</span>
                    <span v-else :key="1">{{ trip.name }}</span>
                  </v-fade-transition>
                </v-col>
              </v-row>
            </template>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-text-field v-model="trip.name" placeholder="Например, Москва"/>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header v-slot="{ open }">
            <v-row no-gutters>
              <v-col cols="4">Место путешествия</v-col>
              <v-col class="text--secondary" cols="8">
                <v-fade-transition leave-absolute>
                  <span v-if="open" :key="0">Выберите страну для путешествия</span>
                  <span v-else :key="1">{{ trip.location }}</span>

                </v-fade-transition>
              </v-col>
            </v-row>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row no-gutters>
              <v-col cols="3">
                <span style="margin-bottom: 5px">Страна</span>
                <v-select v-model="trip.location" :items="countries" flat item-text="name" solo/>
              </v-col>
              <v-col cols="3">
                <span style="margin-bottom: 5px">Город</span>
                <v-select v-model="trip.location" :items="locations" flat item-text="name" solo/>
              </v-col>
            </v-row>
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header v-slot="{ open }">
            <v-row no-gutters>
              <v-col cols="4">Даты путешествия</v-col>
              <v-col class="text--secondary" cols="8">
                <v-fade-transition leave-absolute>
                  <span v-if="open">Когда вы хотите отправиться в путешествие?</span>
                  <v-row v-else no-gutters style="width: 100%">
                    <v-col cols="6">
                      Дата начала путешествия: {{ trip.start || 'Не выбрано' }}
                    </v-col>
                    <v-col cols="6">
                      Дата окончания путешествия: {{ trip.end || 'Не выбрано' }}
                    </v-col>
                  </v-row>
                </v-fade-transition>
              </v-col>
            </v-row>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row justify="space-around" no-gutters>
              <v-col cols="3">
                <v-menu ref="startMenu"
                        :close-on-content-click="false"
                        :return-value.sync="trip.start"
                        min-width="290px"
                        offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="trip.start"
                        v-bind="attrs"
                        v-on="on"
                        label="Дата начала путешествия"
                        prepend-icon="mdi-calendar"
                        readonly
                    />
                  </template>
                  <v-date-picker v-model="date" no-title scrollable>
                    <v-spacer/>
                    <v-btn color="primary" text @click="$refs.startMenu.isActive = false">Отмена</v-btn>
                    <v-btn color="primary" text @click="$refs.startMenu.save(date)">Выбрать</v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>

              <v-col cols="3">
                <v-menu
                    ref="endMenu"
                    :close-on-content-click="false"
                    :return-value.sync="trip.end"
                    min-width="290px"
                    offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="trip.end"
                        v-bind="attrs"
                        v-on="on"
                        label="Дата окончания путешествия"
                        prepend-icon="mdi-calendar"
                        readonly/>
                  </template>
                  <v-date-picker v-model="date" no-title scrollable>
                    <v-spacer/>
                    <v-btn color="primary" text @click="$refs.endMenu.isActive = false">
                      Отмена
                    </v-btn>
                    <v-btn color="primary" text @click="$refs.endMenu.save(date)">OK</v-btn>
                  </v-date-picker>
                </v-menu>
              </v-col>
            </v-row>
          </v-expansion-panel-content>

          <v-expansion-panel>
            <v-expansion-panel-header>
              <template v-slot:default="{ open }">
                <v-row no-gutters>
                  <v-col cols="4">Количество путешествующих</v-col>
                  <v-col class="text--secondary" cols="8">
                    <v-fade-transition leave-absolute>
                      <span v-if="open" :key="0"/>
                      <span v-else :key="1"/>
                    </v-fade-transition>
                  </v-col>
                </v-row>
              </template>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row justify="space-around" no-gutters>
                <v-col class="text--secondary" cols="3" style="margin-right: 20px">
                  <span style="margin-bottom: 5px">Количество взрослых</span>
                  <v-text-field placeholder="" type="number"/>
                </v-col>

                <v-col class="text--secondary" cols="3">
                  <span style="margin-bottom: 5px">Количество детей</span>
                  <v-text-field placeholder="" type="number"/>
                </v-col>
              </v-row>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "SearchPage",
  data: () => ({
    date: null,
    trip: {
      name: '',
      location: null,
      start: null,
      end: null,
    },
    countries: ["Россия", "Франция", "Монголия"],
  }),
}
</script>

<style scoped>

</style>