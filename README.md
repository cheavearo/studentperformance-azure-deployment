"# studentperformance" 

1. The EB CLI is located at:
C:\Users\User\AppData\Roaming\Python\Python312\Scripts
2. Inside your venv, run:
set PATH=%PATH%;C:\Users\User\AppData\Roaming\Python\Python312\Scripts

Then test: eb --version
3. >eb init -p python-3.11 studentperformance-prediction-v3 --region us-east-2

4. Create an environment and deploy your application to it with eb create:
>eb create stud-flask-env

