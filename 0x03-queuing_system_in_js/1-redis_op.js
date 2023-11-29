// Import the necessary library
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Attempt to connect to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully handle process termination
process.on('SIGINT', () => {
  client.quit(() => {
    console.log('Redis client disconnected from the server');
    process.exit();
  });
});

// Function to set a new value for a key in Redis
function setNewSchool(schoolName, value) {
  // Set the value for the key schoolName
  client.set(schoolName, value, redis.print);
}

// Function to display the value for a key in Redis
function displaySchoolValue(schoolName) {
  // Retrieve and log the value for the key
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for key ${schoolName}: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
