<template>
  <v-row>
    <v-spacer />
    <v-col cols="12" md="8">
      <div class="text-h3 pa-4 text-center">Articles on {{ searchTerms }}</div>
      <v-card
        @click.stop="selectedResult(article)"
        :class="{ selected: selectedResult === article }"
        class="my-4"
        v-for="article in articles"
        :key="article.resultID"
      >
        <v-card-title>{{ article.resultTitle }}</v-card-title>
        <v-card-text>{{ article.resultSnippet }}</v-card-text>
      </v-card>
    </v-col>
    <v-spacer />
  </v-row>
</template>

<script>
import { getArticlesForKeywords } from "@/api/dataService";
export default {
  name: "PickResults",
  data: () => ({
    articles: [],
    lastValidResultIndex: 0,
    loading: true,
    selectedResult: null
  }),
  computed: {
    searchTerms() {
      return this.$route.query.searchTerms
    }
  },
  methods: {
    selectResult(article) {
      if (this.selectedResult === article)
        this.selectedResult = null;
      else
        this.selectedResult = article;
    }
  },
  created() {
    getArticlesForKeywords(this.searchTerm, this.lastValidResultIndex).then(({data}) => {
      this.articles = data.resultList;
      this.lastValidResultIndex = data.lastValidResultIndex;
      this.loading = false;
    });
  }
}
</script>

<style scoped>
.selected {
  border: 3px solid skyblue;
}
</style>
