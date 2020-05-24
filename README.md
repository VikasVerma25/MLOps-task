# MLOps-task
We do machine learning, train the model and get the accuracy of the model. But normally we don't get the desired accuracy in the first attempt. We change the hyper parameters again and again then train the model again. This process continues until we get the accuracy we want. 

But doing this process manually is very much time consuming for us. That is why we need to integrate machine learning with DevOps to make this whole process automated. 

In this project we will create a setup with multiple jobs in Jenkins to achieve this goal as follows :-

# Job 1: 
It will be triggered by GitHub webhook as soon as there is some commit in the master branch in GitHub. It will download and copy the code to a particular location.

# Job 2: 
If Job 1 is successful, this job will run or start a container with respective ML software installed in it  and start training the model. If we have a CNN model then it will launch the container using the image containing required libraries for training the model ( I have done it for CNN only). After model is trained we will get an email notification about the model accuracy.

# Job 3: 
If Job 2 runs successfully, this job will check if we got the desired accuracy or not (here  >  98 %). If it gets that accuracy, everything is done. If not, then  Job 3 gets failed and trigger Job 4.

# Job 4: 
This job will help us to change the hyper parameters. After this job, Job 2 will again run and again train the model for new accuracy.

# Job 5: 
This job is just to monitor the container. If container fails it will launch it again.

[Click here For complete explanation of this project](https://www.linkedin.com/post/edit/6670275769748598784/)
