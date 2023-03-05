const express = require('express');
const app = express();
const userDao = require('./userDao');
app.use(express.json());

app.post('/api/user', (req, res) => {
  const user = req.body;
  userDao.addUser(user)
    .then(() => res.status(201).send())
    .catch(err => res.status(500).send(err.message));
})

app.delete("/api/user/:username", (req, res) => {
  const username = req.params.username;
  userDao.deleteUser(username)
    .then(() => res.status(200).send())
    .catch(err => res.status(500).send(err.message));
});

app.post('/api/login', (req, res) => {
  const { username, password } = req.body;
  userDao.login(username, password)
    .then(user => res.status(200).send(user))
    .catch(err => res.status(401).send(err.message));
})

userDao.connect().then(() => {
  app.listen(3069, () => console.log('Listening on port 3069'));
});

