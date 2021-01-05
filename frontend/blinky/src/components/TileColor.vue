<template>
  <v-container>
    <v-row justify="center">
  <v-card
    class="mt-5"
    width="1300"
  >
    <v-container fluid>
      <v-row justify="center">
        <div>{{selected}}</div>
      </v-row>
      <v-row dense>
        <v-col cols="2"
          v-for="(color, idx) in colors" :key="`fruit-${idx}`"
        >
        <v-card v-if="! dark_colors.includes(color)"
          :color="color"
          class="black--text align-end"
          height="200"
          @click="setColor(color)"
          elevation="2">
            <v-card-title v-text="color" ></v-card-title>
          </v-card>
        <v-card v-else
          :color="color"
          class="white--text align-end"
          height="200"
          @click="setColor(color)"
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
  import axios from 'axios'
  const COLORS = [
    'blue', 'orange', 'brown', 'red', 'green', 'white', 'yellow', 'lime', 'black', 'grey', 'teal'
  ]

  export default {
    data: () => ({
      selected: '',
      colors: COLORS,
      dark_colors: ['black', 'blue darken-4', 'brown']
    }),
    methods: {
      setColor: function (color) {
        this.selected=color
        
        axios.post(`http://0.0.0.0:8127/color?color=${color}`)
      }
    } 
  }
</script>