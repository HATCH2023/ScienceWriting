<template>
  <v-row class="full-height">
    <v-spacer />
    <v-col cols="12" md="6">
      <v-img contain src="/header.png"></v-img>
      <v-text-field
        v-model="searchTerms"
        solo
        prepend-icon="mdi-magnify"
        :placeholder="exampleTerm"
      >
        <template v-slot:append>
          <v-btn color="primary" @click="search" @keypress.enter="search">
            Go
          </v-btn>
        </template>
      </v-text-field>
    </v-col>
    <v-spacer />
  </v-row>
</template>

<script>
const randomScienceTerms = [
  'Ecosystem services',
  'Genetically modified organisms',
  'Carbon footprint',
  'Machine learning',
  'Solar power',
  'Brain plasticity',
  'Nanomedicine',
  'Genetic engineering',
  'Quantum computing',
  'Planetary geology'
]

export default {
  name: "SearchTerms",
  data: () => ({
    searchTerms: ""
  }),
  computed: {
    exampleTerm() {
      return randomScienceTerms[Math.floor(Math.random() * randomScienceTerms.length)]
    }
  },
  methods: {
    search() {
      this.$router.push({ path: '/generate/pick-results', query: { searchTerms: this.searchTerms } })
    }
  }
}
</script>

<style scoped>
.full-height {
  height: 100%;
}
</style>
