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
      <HelloLucy/>
    </v-main>
  </v-app>
</template>

<script>
import HelloLucy from './components/HelloLucy';

export default {
  name: 'App',

  components: {
    HelloLucy,
  },

  data: () => ({
    //
  }),
};
</script>
