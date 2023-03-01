function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    jobs.forEach((job) => {
        const newJob = queue.create('push_notification_code_3', job).save();

        newJob.on('enqueue', function(){
            console.log(`Notification job created ${newJob.id}`);

        }).on('complete', function(){
            console.log(`Notification job #${newJob.id} completed`);

        }).on('failed', function(errorMessage){
            console.log(`Notification job #${newJob.id} failed: ${errorMessage}`);
 
        }).on('progress', function(progress, data){
            console.log(`Notification job #${newJob.id} ${progress}% complete`);
        })
    })
}   

module.exports = createPushNotificationsJobs;
