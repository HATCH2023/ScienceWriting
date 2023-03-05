<template>
  <v-row>
    <v-spacer />
    <v-col cols="12" md="8">
      <div class="text-h3 pa-4 text-center">Articles on {{ searchTerms }}</div>
      <v-card>
        <v-card-title>Result 1</v-card-title>
      </v-card>
    </v-col>
    <v-spacer />
  </v-row>
</template>

<script>
export default {
  name: "PickResults",
  data: () => ({
    
  }),
  computed: {
    searchTerms() {
      return this.$route.query.searchTerms
    }
  },
  methods: {
    
  }
}
</script>

