import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Redis client setup
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Initialize available seats
const initialAvailableSeats = 50;
let reservationEnabled = true;

// Reserve seats function
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Get current available seats function
const getCurrentAvailableSeats = async () => {
  const availableSeats = await getAsync('available_seats');
  return availableSeats ? parseInt(availableSeats, 10) : 0;
};

// Kue queue setup
const queue = kue.createQueue();

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

// Route to process the queue and reserve seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats <= 0) {
    reservationEnabled = false;
    return;
  }

  queue.process('reserve_seat', async (job, done) => {
    try {
      const newAvailableSeats = currentAvailableSeats - 1;
      await reserveSeat(newAvailableSeats);

      if (newAvailableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    } catch (error) {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

export default app;
