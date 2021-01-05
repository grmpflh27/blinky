<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h3>Neopixels for Lucy</h3>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <TileColor/>
    </v-main>
  </v-app>
</template>

<script>
import TileColor from './components/TileColor';

export default {
  name: 'App',

  components: {
    TileColor,
  },

  data: () => ({
    //
  }),
};
</script>
