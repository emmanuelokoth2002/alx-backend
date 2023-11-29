import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    // Create a Kue queue in test mode
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient } });
    queue.testMode.enter();
  });

  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    // Expect an error to be thrown when jobs is not an array
    expect(() => createPushNotificationsJobs('not_an_array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    // Sample array of jobs
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    // Create push notification jobs
    createPushNotificationsJobs(jobs, queue);

    // Validate the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Validate the type of the jobs in the queue
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');

    // Validate job creation log messages
    expect(queue.testMode.jobs[0].log[0]).to.equal('Notification job created: 1');
    expect(queue.testMode.jobs[1].log[0]).to.equal('Notification job created: 2');
  });

  // Add more test cases as needed
});
