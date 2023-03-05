<template>
  <v-row>
    <v-col cols="12">
      <v-card>
        <v-card-title>Review Generated Content</v-card-title>
        <v-card-text>
          <v-tabs v-model="tab" bg-color="primary">
            <v-tab value="pressRelease">Press Release</v-tab>
            <v-tab value="blog">Blog</v-tab>
            <v-tab value="facebook">Facebook</v-tab>
            <v-tab value="linkedIn">LinkedIn</v-tab>
            <v-tab value="twitter">Twitter</v-tab>
            <v-tab value="instagram">Instagram</v-tab>
          </v-tabs>

          <v-tabs-items v-model="tab">
            <v-tab-item>
              <v-checkbox v-model="pressReleasePublish" class="pl-3" label="Publish"/>
              <v-textarea auto-grow placeholder="Chad working hard..." :loading="!pressRelease" v-model="pressRelease" counter></v-textarea>
            </v-tab-item>

            <v-tab-item>
              <v-checkbox v-model="blogPublish" class="pl-3" label="Publish"/>
              <v-textarea auto-grow placeholder="Chad working hard..." :loading="!blogPost" v-model="blogPost" counter></v-textarea>
            </v-tab-item>

            <v-tab-item>
              <v-checkbox v-model="facebookPublish" class="pl-3" label="Publish"/>
              <v-textarea auto-grow placeholder="Chad working hard..." :loading="!facebookCaption" v-model="facebookCaption" counter></v-textarea>
            </v-tab-item>

            <v-tab-item>
              <v-checkbox v-model="linkedInPublish" class="pl-3" label="Publish"/>
              <v-textarea auto-grow placeholder="Chad working hard..." :loading="!linkedInCaption" v-model="linkedInCaption" counter></v-textarea>
            </v-tab-item>

            <v-tab-item>
              <v-checkbox v-model="twitterPublish" class="pl-3" label="Publish"/>
              <v-textarea auto-grow placeholder="Chad working hard..." :loading="!twitterCaption" v-model="twitterCaption" counter></v-textarea>
            </v-tab-item>

            <v-tab-item>
              <v-checkbox v-model="instagramPublish" class="pl-3" label="Publish"/>
              <v-textarea auto-grow placeholder="Chad working hard..." :loading="!instagramCaption" v-model="instagramCaption" counter></v-textarea>
            </v-tab-item>
          </v-tabs-items>
        </v-card-text>
      </v-card>
      <v-snackbar color="error" v-model="snackbar">
        Scraping Error. Please try another source.
        <v-btn
          text
          @click="$router.go(-1)"
        >
          Go Back
        </v-btn>
      </v-snackbar>
    </v-col>
  </v-row>
</template>

<script>
import { getSummary } from "@/api/dataService";
export default {
  name: "ReviewContent",
  data: () => ({
    tab: null,
    snackbar: false,

    pressRelease: "",
    pressReleasePublish: true,
    blogPost: "",
    blogPublish: true,
    instagramCaption: "",
    instagramImageUrl: "",
    instagramPublish: true,
    twitterCaption: "",
    twitterImageUrl: "",
    twitterPublish: true,
    linkedInCaption: "",
    linkedInImageUrl: "",
    linkedInPublish: true,
    facebookCaption: "",
    facebookImageUrl: "",
    facebookPublish: true
  }),
  created() {
    getSummary(this.$route.query.articleUrl).then(({data}) => {
      this.pressRelease = data.summary;
    }).catch(() => {
      this.snackbar = true;
    });
  }
};
</script>
