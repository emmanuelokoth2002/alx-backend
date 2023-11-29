// Import the necessary library
import kue from 'kue';

// Create an array of jobs
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// Create a Kue queue
const queue = kue.createQueue();

// Loop through the array of jobs and create a new job for each object
jobs.forEach((jobData, index) => {
  // Create a new job in the 'push_notification_code_2' queue
  const job = queue.create('push_notification_code_2', jobData);

  // On successful job creation, log the job ID
  job.save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

  // On job completion, log the completion message
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  // On job failure, log the failure message
  job.on('failed', (err) => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // On job progress, log the progress message
  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
});

// Exit the process to end the script
process.exit(0);
