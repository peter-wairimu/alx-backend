const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklist.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`));
        return;
    }

    if (job.progress(50, 100)) {
        console.log(
            `Sending notification to ${phoneNumber}, with message: ${message}`
        );
    
    }
    done();
}

const queue = kue.createQueue();

queue.process("push_notification_code_2", 2, function(job, done){
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});
