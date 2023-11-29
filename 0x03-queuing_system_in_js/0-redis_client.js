// Import the necessary library
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

process.on('SIGINT', () => {
  client.quit(() => {
    console.log('Redis client disconnected from the server');
    process.exit();
  });
});
