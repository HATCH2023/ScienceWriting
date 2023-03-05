<template>
  <v-row>
    <v-spacer />
    <v-col cols="12" md="8">
      <div class="text-h4 pa-4 text-center">Scientific Articles on {{ searchTerms }}</div>
      <div v-if="loading" class="text-center mt-12">
        <v-progress-circular :size="128" :width="7" indeterminate color="primary" />
      </div>
      <v-card
        v-else
        @click="selectedResult = article"
        :class="{ selected: selectedResult === article }"
        class="my-4"
        v-for="article in articles"
        :key="article.resultID"
      >
        <v-card-title>{{ article.resultTitle }}</v-card-title>
        <v-card-text>{{ article.resultSnippet }}</v-card-text>
        <v-card-actions>
          <v-spacer /><v-btn target="_blank" :href="article.resultLink" text><v-icon left>mdi-eye</v-icon>Preview</v-btn>
        </v-card-actions>
      </v-card>
      <div class="text-right" v-if="!loading">
        <v-btn color="primary" @click="next">Next<v-icon right>mdi-chevron-right</v-icon></v-btn>
      </div>
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
    next() {
      this.$router.push({
        path: "/generate/review-content",
        query: {
          articleUrl: this.selectedResult.resultLink,
        }
      });
    }
  },
  created() {
    getArticlesForKeywords(this.searchTerms, this.lastValidResultIndex).then(({data}) => {
      this.articles = data.resultList;
      this.lastValidResultIndex = data.lastValidResultIndex;
      this.loading = false;

      // Select the first result by default
      this.selectedResult = this.articles[0];
    });
  }
}
</script>

<style scoped>
.selected {
  background: #0e586f;
}
</style>
