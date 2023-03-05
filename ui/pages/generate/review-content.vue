<template>
  <v-row>
    <v-col cols="12">
      <v-card class="mb-8">
        <v-card-actions><v-card-title>Review Generated Content</v-card-title><v-spacer /><v-btn @click="publish" color="primary">Publish<v-icon right>mdi-earth</v-icon></v-btn></v-card-actions>
      </v-card>
      <v-card>
        <v-card-text>
          <v-tabs v-model="tab" bg-color="primary">
            <v-tab value="pressRelease"><v-icon left>mdi-typewriter</v-icon>Press Release</v-tab>
            <v-tab value="blog"><v-icon left>mdi-post</v-icon>Blog</v-tab>
            <v-tab value="facebook"><v-icon left>mdi-facebook</v-icon>Facebook</v-tab>
            <v-tab value="linkedIn"><v-icon left>mdi-linkedin</v-icon>LinkedIn</v-tab>
            <v-tab value="twitter"><v-icon left>mdi-twitter</v-icon>Twitter</v-tab>
            <v-tab value="instagram"><v-icon left>mdi-instagram</v-icon>Instagram</v-tab>
            <v-tab value="instagram"><v-icon left>mdi-image</v-icon>Image</v-tab>
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
            
            <v-tab-item>
              <v-row class="mt-8">
                <v-col cols="12" md="6">
                  <v-card class="text-center">
                    <v-img :class="{ highlight: selectedImage === imageSrc1 }" v-if="imageSrc1" contain :src="imageSrc1" />
                    <v-progress-circular style="display: block; margin: auto" class="my-8" v-else indeterminate />
                    <v-btn @click="selectedImage = imageSrc1; selectedImagePath = imagePath1" class="mt-4" color="primary">Select</v-btn>
                  </v-card>
                </v-col>
                <v-col cols="12" md="6">
                  <v-card class="text-center">
                    <v-img :class="{ highlight: selectedImage === imageSrc2 }" v-if="imageSrc2" contain :src="imageSrc2" />
                    <v-progress-circular style="display: block; margin: auto" class="my-8"  v-else indeterminate />
                    <v-btn @click="selectedImage = imageSrc2; selectedImagePath = imagePath2" class="mt-4" color="primary">Select</v-btn>
                  </v-card>
                </v-col>
              </v-row>
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
import { getSummary, getPlatformContent, getArtificialImages, postFacebook, postTwitter, postLinkedIn, postInstagram } from "@/api/dataService";
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
    instagramPublish: true,
    twitterCaption: "",
    twitterPublish: true,
    linkedInCaption: "",
    linkedInPublish: true,
    facebookCaption: "",
    facebookPublish: true,
    selectedImage: null,
    selectedImagePath: null,

    imageSrc1: null,
    imagePath1: "",
    imageSrc2: null,
    imagePath2: null
  }),
  methods: {
    publish() {
      // if (instagramPublish) postInstagram(selectedImagePath, instagramCaption);
      if (twitterPublish) postTwitter(selectedImagePath, twitterCaption);
      if (linkedInPublish) postLinkedIn(selectedImagePath, linkedInCaption);
      if (facebookPublish) postFacebook(selectedImagePath, facebookCaption);
    }
  },
  created() {
    getSummary(this.$route.query.articleUrl).then(({data}) => {
      this.pressRelease = data.summary;
      getPlatformContent(data.summary)
        .then(({data}) => {
          data.forEach((platform) => {
            switch (platform.platform) {
              case "Instagram":
                this.instagramCaption = platform.post;
                break;
              case "Twitter":
                this.twitterCaption = platform.post;
                break;
              case "LinkedIn":
                this.linkedInCaption = platform.post;
                break;
              case "Facebook":
                this.facebookCaption = platform.post;
                break;
              case "Blog":
                this.blogPost = platform.post;
                break;
              default:
                break;
            }
          });
        });
      // get images
      getArtificialImages(data.summary)
        .then(({data}) => {
          this.imageSrc1 = data.url1;
          this.imageSrc2 = data.url2;
          this.imagePath1 = data.image1,
          this.imagePath2 = data.image2
        })
    }).catch((e) => {
      console.error(e);
      this.snackbar = true;
    });
  }
};
</script>

<style scoped>
.highlight {
  border: 4px solid #2196F3;
}
</style>
