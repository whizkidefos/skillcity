import sqlite3 from 'sqlite3';
import { fileURLToPath } from 'url';
import path from 'path';
import express from 'express';
import cors from 'cors';



const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const dbPath = path.resolve(__dirname, 'user_database.db');
const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READWRITE, (err) => {

    if (err) {
        console.error(err.message);
    } else {
        console.log('Connected to the SQLite database.');
    }
});

const app = express();
app.use(cors()); // Enable CORS
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.send(index.html);
});

// Add an API endpoint to retrieve user data
app.get('/users', (req, res) => {
    db.all(`SELECT * FROM Users`, [], (err, rows) => {
        if (err) {
            console.error(err.message);
            res.status(500).send('Error retrieving users from database');
        } else {
            res.status(200).json(rows);
        }
    });
});


app.post('/addUser', (req, res) => {
    const { username, email } = req.body;

    db.run(`INSERT INTO Users (username, email) VALUES (?, ?)`, [username, email], function(err) {
        if (err) {
            console.error(err.message);
            res.status(500).send('Error inserting user into database');
        } else {
            console.log(`A new user has been added with ID: ${this.lastID}`);
            res.status(200).send('User added successfully');
        }
    });
});

app.delete('/deleteUser/:id', (req, res) => {
    const id = req.params.id;

    db.run(`DELETE FROM Users WHERE id = ?`, id, function(err) {
        if (err) {
            console.error(err.message);
            res.status(500).send('Error deleting user from database');
        } else {
            console.log(`User with ID ${id} has been deleted`);
            res.status(200).send('User deleted successfully');
        }
    });
});

app.put('/updateUser/:id', (req, res) => {
    const id = req.params.id;
    const { username, email } = req.body;

    db.run(`UPDATE Users SET username = ?, email = ? WHERE id = ?`, [username, email, id], function(err) {
        if (err) {
            console.error(err.message);
            res.status(500).send('Error updating user in database');
        } else {
            console.log(`User with ID ${id} has been updated`);
            res.status(200).send('User updated successfully');
        }
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
