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

// Function to create a hash in Redis
function createHash() {
  // Use hset to store hash values
  client.hset(
    'HolbertonSchools',
    'Portland',
    '50',
    redis.print
  );
  client.hset(
    'HolbertonSchools',
    'Seattle',
    '80',
    redis.print
  );
  client.hset(
    'HolbertonSchools',
    'New York',
    '20',
    redis.print
  );
  client.hset(
    'HolbertonSchools',
    'Bogota',
    '20',
    redis.print
  );
  client.hset(
    'HolbertonSchools',
    'Cali',
    '40',
    redis.print
  );
  client.hset(
    'HolbertonSchools',
    'Paris',
    '2',
    redis.print
  );
}

function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error retrieving hash values: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

createHash();
displayHash();
