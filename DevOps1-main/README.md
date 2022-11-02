# DevOps1
 Goals 
 The goals of this small homework are: 
 1. To measure your Infrastructure as Code (IaC) knowledge, 
 2. To assess your coding skills, 
 3. To see if you adhere to best DevSecOps practices. 

 
 Description 
 As part of an imaginary medical platform hosted on AWS, we would like to have a simple 
 serverless application that allows us to validate and store some sensitive medical data to S3. For 
 simplicity, the medical data is a json payload: 
 {“Id”: 123456, “Age”: 70, “Sex”: “male”} 
 We would like the application to have the following components: 
 1. An API Gateway that allows POST that json payload, and triggers the Lambda function. 
 2. A Python Lambda function that: 
 2.1. Validates the payload, making sure the “Age” ﬁeld is between 50 and 100. 
 2.2. Saves the json to S3 if it has been validated (using the “Id” ﬁeld as ﬁle name). 
 3. A S3 bucket which will store the sensitive medical data. 
 4. + anything else you feel you need to include. 
 The minimal application is pictured in the ﬁgure below: 

 Deliverables 
 Please provide the following ﬁles: 
 1. Either a Terraform template or an AWS CDK Python code of that application. 
 2. The Python code of the lambda function. 
 

# Solution
First Clone the code and run terraform commands. 

```
git clone <URL>
cd <directory>
terraform init
terraform plan  #To verify
terraform apply -auto-approve
```

