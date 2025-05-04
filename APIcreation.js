// Import the Express library
const express = require('express');

// Create an Express application instance
const app = express();

// Define a route for HTTP GET requests to the root URL ('/')
// This route sends a simple text response to the client
app.get('/', (req, res) => {
  res.send('Welcome to my API');  // Sends 'Welcome to my API' as the response
});

// Start the server on port 3000 and log a message to the console
app.listen(3000, () => console.log('API running on port 3000'));
