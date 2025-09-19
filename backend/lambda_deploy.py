"""
AWS Lambda deployment script for QuranAI Backend
"""
import zipfile
import os
import shutil
import subprocess

def create_lambda_package():
    """Create a deployment package for AWS Lambda with dependencies"""
    
    # Create a temporary directory for the package
    package_dir = "lambda_package"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)
    
    print("Installing dependencies...")
    # Install dependencies to the package directory
    subprocess.run([
        "pip", "install", "-r", "requirements.txt", "-t", package_dir
    ], check=True)
    
    # Copy main application file
    shutil.copy2("main.py", package_dir)
    
    print("Creating zip package...")
    # Create zip file
    with zipfile.ZipFile('lambda-deployment.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arc_name)
                
    # Clean up temporary directory
    shutil.rmtree(package_dir)
    
    print("✅ Lambda deployment package created: lambda-deployment.zip")
    print(f"📦 Package size: {os.path.getsize('lambda-deployment.zip') / 1024 / 1024:.2f} MB")
    print("\nNext steps:")
    print("1. Upload lambda-deployment.zip to AWS Lambda")
    print("2. Set handler to: main.handler")
    print("3. Configure API Gateway trigger")
    print("4. Set OPENAI_API_KEY environment variable in Lambda")

if __name__ == "__main__":
    create_lambda_package()
