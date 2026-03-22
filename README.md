# 🛡️ DevSecOps S3 Automation Lab

## 📌 Project Overview
This project uses **Terraform** to provision AWS infrastructure and a **Python (Boto3)** script to automatically detect and remediate public S3 bucket vulnerabilities.

### 🛠️ Tech Stack
* **Cloud:** AWS (S3, IAM)
* **IaC:** Terraform
* **Scripting:** Python 3.13 (Boto3)
* **Environment:** Kali Linux

## 🚀 The Challenge
I used Terraform to create a "Leaky" S3 bucket with Public Access enabled to simulate a real-world misconfiguration.

## 🐍 The Solution
The `s3_protector.py` script:
1. **Audits** buckets in `ap-south-1`.
2. **Identifies** public access vulnerabilities.
3. **Remediates** by forcing the bucket to a "Private" state.
