// Import the necessary library
import kue from 'kue';

const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!',
};

const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

process.exit(0);
