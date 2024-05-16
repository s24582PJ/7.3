const express = require('express');
const { Pool } = require('pg');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

const pool = new Pool({
  user: 'user',
  host: 'database',
  database: 'mydatabase',
  password: 'password',
  port: 5432,
});

app.get('/cars', async (req, res) => {
  const result = await pool.query('SELECT * FROM cars');
  res.json(result.rows);
});

app.post('/addCar', async (req, res) => {
  const { make, model, year } = req.body;
  const result = await pool.query('INSERT INTO cars (make, model, year) VALUES ($1, $2, $3) RETURNING *', [make, model, year]);
  res.json(result.rows[0]);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
