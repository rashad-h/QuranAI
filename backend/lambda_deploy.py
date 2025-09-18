"""
AWS Lambda deployment script for QuranAI Backend
"""
import zipfile
import os

def create_lambda_package():
    """Create a deployment package for AWS Lambda"""
    
    # Files to include in the package
    files_to_zip = [
        'main.py',
        'requirements.txt'
    ]
    
    # Create zip file
    with zipfile.ZipFile('lambda-deployment.zip', 'w') as zipf:
        for file in files_to_zip:
            if os.path.exists(file):
                zipf.write(file)
                print(f"Added {file} to package")
            else:
                print(f"Warning: {file} not found")
    
    print("Lambda deployment package created: lambda-deployment.zip")
    print("\nNext steps:")
    print("1. Upload lambda-deployment.zip to AWS Lambda")
    print("2. Set handler to: main.handler")
    print("3. Configure API Gateway trigger")
    print("4. Set OPENAI_API_KEY environment variable in Lambda")

if __name__ == "__main__":
    create_lambda_package()
