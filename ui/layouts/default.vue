<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title :key="item.title">
              {{ item.title }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      fixed
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>{{ title || "Scriptor" }}</v-toolbar-title>

      <v-spacer />

      <v-btn v-if="loggedIn" text to="/account-settings">Hi, {{ firstName }}<v-icon right>mdi-account-circle</v-icon></v-btn>
      <v-btn v-else-if="$route.path !== '/login'" text to="/login">Log In</v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapState, mapGetters } from "vuex";
export default {
  name: 'DefaultLayout',
  data () {
    return {
      drawer: true,
      items: [
        {
          icon: 'mdi-file-document-edit',
          title: 'Generate',
          to: '/generate/search-terms'
        },
        {
          icon: 'mdi-earth',
          title: 'Publish',
          to: '/inspire'
        }
      ]
    }
  },
  computed: {
    ...mapState('user', ['firstName']),
    ...mapGetters('user', ['loggedIn',]),
    title () {
      return this.$route.meta.title
    }
  }
}
</script>

<style scoped>
.full-height {
  height: 100%;
}
</style>
