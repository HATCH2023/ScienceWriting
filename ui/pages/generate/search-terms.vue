<template>
  <v-row class="full-height">
    <v-spacer />
    <v-col cols="12" md="6">
      <v-img contain src="/header.png"></v-img>
      <v-text-field
        @keypress.enter="search"
        v-model="searchTerms"
        solo
        prepend-icon="mdi-magnify"
        label="Search for terms to generate content"
      >
        <template v-slot:append>
          <v-btn color="primary" @click="search">
            Go
          </v-btn>
        </template>
      </v-text-field>
    </v-col>
    <v-spacer />
  </v-row>
</template>

<script>
export default {
  name: "SearchTerms",
  data: () => ({
    searchTerms: ""
  }),
  computed: {
    
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
