<template>
  <v-row>
    <v-spacer />
    <v-col cols="12" md="4">
      <v-img contain src="/header.png"></v-img>
      <v-card>
        <v-card-title>Log In</v-card-title>
        <v-card-text>
          <v-form>
            <v-text-field
              v-model="username"
              label="Username"
              type="text"
              required
            ></v-text-field>
            <v-text-field
              v-model="password"
              label="Password"
              type="password"
              required
            ></v-text-field>
            <v-expand-transition>
              <div v-show="signUp">
                <v-text-field
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
          <v-btn text @click="signUp = !signUp">{{ signUp ? "Log In" : "Sign Up" }}</v-btn>
          <v-spacer />
          <v-btn @click="login">{{ signUp ? "Sign Up" : "Log In" }}</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-spacer />
  </v-row>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      firstName: "",
      role: "",
      signUp: false
    };
  },
}
</script>
