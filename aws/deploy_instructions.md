# AWS Deployment Instructions for AI Safety Red Team Project

## Prerequisites
- An AWS account
- AWS CLI installed and configured
- Docker installed on your local machine

## Step 1: Set Up AWS Environment
1. **Create an IAM Role**:
   - Go to the IAM console.
   - Create a new role with permissions for ECS, ECR, and any other services you plan to use.
   - Attach the role to your ECS task.

2. **Create a VPC** (if you don't have one):
   - Navigate to the VPC console.
   - Create a new VPC with public and private subnets.

3. **Set Up Security Groups**:
   - Create a security group that allows inbound traffic on the necessary ports (e.g., 80 for HTTP, 443 for HTTPS).

## Step 2: Build Docker Image
1. Navigate to the project root directory where the `Dockerfile` is located.
2. Build the Docker image:
   ```bash
   docker build -t ai-safety-redteam .
   ```

## Step 3: Push Docker Image to ECR
1. **Create an ECR Repository**:
   - Go to the ECR console.
   - Create a new repository named `ai-safety-redteam`.

2. **Authenticate Docker to ECR**:
   ```bash
   aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
   ```

3. **Tag and Push the Image**:
   ```bash
   docker tag ai-safety-redteam:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/ai-safety-redteam:latest
   docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/ai-safety-redteam:latest
   ```

## Step 4: Deploy on ECS
1. **Create a Task Definition**:
   - Go to the ECS console.
   - Create a new task definition using the Fargate launch type.
   - Specify the container details, including the image URI from ECR.

2. **Create a Service**:
   - In the ECS console, create a new service using the task definition created in the previous step.
   - Choose the desired number of tasks and configure load balancing if necessary.

## Step 5: Access the Application
- Once the service is running, you can access the application using the public IP or DNS name provided by the load balancer or the ECS service.

## Additional Notes
- Monitor the application using CloudWatch for logs and metrics.
- Ensure that your application adheres to best practices for security and performance on AWS.