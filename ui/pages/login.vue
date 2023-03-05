<template>
  <v-row>
    <v-spacer />
    <v-col cols="12" md="4">
      <v-img contain src="/header.png"></v-img>
      <v-card>
        <v-card-title>Log In</v-card-title>
        <v-card-text>
          <v-form @keypress.enter="processSignIn">
            <v-text-field
              @keypress.enter="processSignIn"
              v-model="username"
              label="Username"
              type="text"
              required
            ></v-text-field>
            <v-text-field
              @keypress.enter="processSignIn"
              v-model="password"
              label="Password"
              type="password"
              required
              :error-messages="error"
            ></v-text-field>
            <v-expand-transition>
              <div v-show="isSigningUp">
                <v-text-field
                  @keypress.enter="processSignIn"
                  v-model="firstName"
                  label="First Name"
                  type="text"
                  required
                />
                <v-radio-group inline v-model="role">
                  <v-radio label="Admin" value="Admin" />
                  <v-radio label="Slave" value="Slave" />
                </v-radio-group>
              </div>
            </v-expand-transition>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="isSigningUp = !isSigningUp">{{ isSigningUp ? "Log In" : "Sign Up" }}</v-btn>
          <v-spacer />
          <v-btn @click="processSignIn">{{ isSigningUp ? "Sign Up" : "Log In" }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-spacer />
  </v-row>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Login",
  computed: {
    ...mapGetters("user", ["loggedIn"]),
  },
  data() {
    return {
      username: "",
      password: "",
      firstName: "",
      role: "",
      isSigningUp: false,
      error: ""
    };
  },
  methods: {
    ...mapActions("user", ["login", "signUp"]),
    processSignIn() {
      if (this.isSigningUp) {
        this.signUp({
          username: this.username,
          password: this.password,
          firstName: this.firstName,
          role: this.role
        }).then(() => {
            this.$router.push("/");
          })
          .catch(err => {
            this.error = err;
          })
      } else {
        this.login({
          username: this.username,
          password: this.password
        })
          .then(() => {
            this.$router.push("/");
          })
          .catch(err => {
            this.error = err.message;
          })
      }
    }
  },
  beforeMount() {
    if (this.loggedIn) {
      this.$router.push("/");
    }
  }
}
</script>
