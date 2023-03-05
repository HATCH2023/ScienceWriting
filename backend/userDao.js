const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: String,
  password: String,
  firstName: String,
  lastName: String,
  role: String
});
const User = mongoose.model('User', userSchema);

module.exports = {
  async connect() {
    try {
      await mongoose.connect('mongodb://localhost/scriptor', { useNewUrlParser: true });
      console.log('Connected to MongoDB');
    } catch (err) {
      console.error('Could not connect to MongoDB', err);
    }
  },

  async addUser(newUser) {
    const user = new User(newUser);
    try {
      await user.save();
      return user;
    } catch (err) {
      throw new Error('Username already exists: ' + err.message);
    }
  },

  async deleteUser(username) {
    try {
      await User.findOneAndRemove({ username }).exec();
    } catch (err) {
      throw new Error('Could not delete user: ' + err.message);
    }
  },

  async login(username, password) {
    const matchingUser = await User.findOne({ username, password });
    if (matchingUser) {
      return matchingUser;
    } else {
      throw new Error('Invalid username or password');
    }
  },

  close() {
    mongoose.disconnect();
  }
}
