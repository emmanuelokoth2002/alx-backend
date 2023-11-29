// Import the necessary library
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

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

// Async function to display the value for a key in Redis
async function displaySchoolValue(schoolName) {
  try {
    // Retrieve the value for the key using async/await
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.error(`Error retrieving value for key ${schoolName}: ${error}`);
  }
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
