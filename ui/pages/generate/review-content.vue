<template>
  <v-row>
    <v-col cols="12">
      <v-card>
        <v-card-title>Blog Post</v-card-title>
        <v-card-text>
          <v-textarea
            v-model="blogPost"
            counter
            placeholder="Loading..."
          ></v-textarea>
        </v-card-text>
      </v-card>
    </v-col>
    <v-col cols="12" md="6"></v-col>
    <v-col cols="12" md="6"></v-col>
  </v-row>
</template>

<script>
export default {
  name: "ReviewContent",
  data: () => ({
    blogPost: "",
    instagramCaption: "",
    instagramImageUrl: "",
    twitterCaption: "",
    linkedInCaption: "",
    facebookCaption: ""
  }),
  mounted() {
    this.blogPost = this.$route.query.articleUrl;
  }
};
</script>
