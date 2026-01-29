# AWS EC2 Cost Optimizer 🚀

A Python-based automation tool to identify unused AWS EC2 and EBS resources and help reduce cloud infrastructure costs.

## 📌 Overview
This project scans an AWS account to:
- Detect **stopped EC2 instances**
- Identify **unused (available) EBS volumes**
- Provide visibility into resources that may be incurring unnecessary costs

This tool is useful for cloud engineers, DevOps teams, and solution architects focused on **cost optimization** and **resource governance**.

## 🛠️ Technologies Used
- Python 3
- AWS SDK for Python (boto3)
- AWS EC2
- AWS EBS

## ⚙️ Features
- Lists all stopped EC2 instances
- Lists all unattached EBS volumes
- Lightweight, fast, and easy to extend
- Can be integrated with AWS Lambda or scheduled jobs

## 📂 Project Structure
aws-ec2-cost-optimizer/
├── ec2_cost_optimizer.py
└── README.md


## ▶️ How to Run
1. Configure AWS credentials:
'''bash
aws configure

2. Install dependencies:

pip install boto3

3. Run the script:

python ec2_cost_optimizer.py


📈 Sample Output
Stopped EC2 Instances: ['i-0abcd12345']
Unused EBS Volumes: ['vol-0123abcd']

🔮 Future Enhancements

Monthly cost estimation

Auto-tagging unused resources

Email or Slack notifications

Lambda + EventBridge automation

👨‍💻 Author

Hari Manikanta Velamkayala
AWS Solution Architect | Cloud & DevOps Engineer