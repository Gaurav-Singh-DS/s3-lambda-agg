# 📊 AWS Lambda - S3 Triggered CSV Aggregator

This project demonstrates how to build a **serverless data processing pipeline** using **AWS Lambda** and **Amazon S3** with automatic logging in **CloudWatch**.

Whenever a CSV file is uploaded to the S3 bucket, the Lambda function is triggered automatically. The function reads the file, aggregates GDP values by country, and writes the result back into the same bucket under an `output/` prefix — while avoiding infinite recursion loops.

---

## 🚀 Project Workflow

1. **Upload CSV file** to an S3 bucket (e.g., `input/data.csv`).
2. **S3 Event Trigger** invokes the Lambda function.
3. **Lambda Execution**:
   - Reads the CSV file from S3.
   - Parses rows using the `csv` module.
   - Aggregates GDP values grouped by country.
   - Writes the result into the same S3 bucket at `output/agg.json`.
   - Skips processing files already inside `output/` to avoid re-trigger loops.
4. **CloudWatch Logs** automatically capture execution details for monitoring and debugging.

---

## 🛠️ Technologies Used

- **AWS Lambda** – serverless compute
- **Amazon S3** – input/output data storage
- **Amazon CloudWatch** – logging & monitoring
- **Python 3.x**
  - `boto3` for S3 interaction
  - `csv` and `json` for parsing & serialization

---

## 📂 Project Structure
s3-lambda-agg/
│── lambda_function.py     # your code
│── README.md              # explanation
│── steps.txt              # Steps


