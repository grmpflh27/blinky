<template>
  <v-container>
    <v-row justify="center">
  <v-card
    class="mt-5"
    width="1300"
  >
    <v-container fluid>
      <v-row justify="center">
        <v-div>{{selected}}</v-div>
      </v-row>
      <v-row dense>
        <v-col
          v-for="(color, idx) in colors" :key="`fruit-${idx}`"
        >
        <v-card v-if="! dark_colors.includes(color)"
          :color="color"
          class="ma-3 black--text align-end"
          width="250"
          height="250"
          @click="selected=color"
          elevation="2">
            <v-card-title v-text="color" ></v-card-title>
          </v-card>
        <v-card v-else
          :color="color"
          class="ma-3 white--text align-end"
          width="250"
          height="250"
          @click="selected=color"
          elevation="2">
            <v-card-title v-text="color" ></v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
  </v-row>
  </v-container>
</template>

<script>
  const COLORS = [
    'blue', 'orange', 'brown', 'red', 'green', 'white', 'yellow', 'lime', 'black', 'blue darken-4', 'grey', 'teal'
  ]

  export default {
    data: () => ({
      selected: '',
      colors: COLORS,
      dark_colors: ['black', 'blue darken-4', 'brown']
    }),
  }
</script>