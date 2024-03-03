// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');

// Create Express application
const app = express();

// Connect to MongoDB database
mongoose.connect('mongodb+srv://raushan:nYXqTlrcim2jMfa5@cityscope-hj-09-11-2022.d55av.mongodb.net/?retryWrites=true&w=majority&appName=cityscope-hj-09-11-2022-production', {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => {
    console.log("Connected to MongoDB");
})
.catch((error) => {
    console.error("Error connecting to MongoDB:", error);
});

// Define a schema for queries
const querySchema = new mongoose.Schema({
    text: String,
    date: { type: Date, default: Date.now }
});

// Create a model based on the schema
const Query = mongoose.model('Query', querySchema);

// Route to fetch queries from the database
app.get('/queries', async (req, res) => {
    try {
        // Fetch all queries from the database
        const queries = await Query.find();

        // Send the queries as JSON response
        res.json(queries);
    } catch (error) {
        // If an error occurs, send an error response
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

