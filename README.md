# Getting started with Django on Google Cloud Platform on App Engine Standard

This repository is an example of how to run a [Django](https://www.djangoproject.com/) 
app on Google App Engine Standard Environment. It uses the 
[Writing your first Django app](https://docs.djangoproject.com/en/1.9/intro/tutorial01/) as the 
example app to deploy.

# gcloud settings

1. You can set a different default project by typing

        gcloud config set project mywaterbuffalo-178002

2. Deploy new app

        gcloud app deploy

	The recommended approach is to remove the application element from your app.yaml file and instead, use a command-line flag to specify your application ID:
	To use the gcloud app deploy command, you must specify the --project flag:

        gcloud app deploy --project [YOUR_PROJECT_ID]

    To use the appcfg.py update command, you specify the -A flag:

        appcfg.py update -A [YOUR_PROJECT_ID]

    For more information about using these commands, see Deploying Your App.

    The application ID is the Cloud Platform Console project ID that you specified when you created the application in the Google Cloud Platform Console.

# Tutorial
See our [Running Django in the App Engine Standard Environment](https://cloud.google.com/python/django/appengine) tutorial for instructions for setting up and deploying this sample application.


# Configure the database settings

1. Open mysite/settings.py for editing.
2. In two places, replace <your-database-user> and <your-database-password> with the username and password you created previously. This helps set up the connection to the database for both App Engine deployment and local testing.
3. Run the following command. Copy the outputted connectionName value for the next step.

    `gcloud beta sql instances describe [YOUR_INSTANCE_NAME]`

4. Replace <your-cloudsql-connection-string> with connectionName from the previous step.
5. Close and save settings.py.

# Run the app on your local computer

1. To run the Django app on your local computer, you'll need a Python development environment set up, including Python, pip, and virtualenv. Follow these instructions to install on Linux , OS X, or Windows.
2. Create an isolated Python environment, and install dependencies:

    LINUX/MAC OS XWINDOWS

        virtualenv env
        source env/bin/activate
        pip install -r requirements-vendor.txt -t lib/
        pip install -r requirements.txt


3. Run the Django migrations to set up your models:

        python manage.py makemigrations
        python manage.py makemigrations polls
        python manage.py migrate

4. Start a local web server:

`python manage.py runserver`

5. In your web browser, enter this address:

`http://localhost:8000`

You should see a simple webpage with the following text: "Hello, world. You're at the polls index." The sample app pages are delivered by the Django web server running on your computer. When you're ready to move forward, press Ctrl+C to stop the local web server.

# Installing a third-party library

In order to use a third-party library, copy it into a folder in your project's source directory. The library must be implemented as pure Python code with no C extensions. The code is uploaded to App Engine with your application code, and counts towards file quotas.

To copy a library into your project:

1. Create a directory to store your third-party libraries, such as lib/.

        mkdir lib

2. Use pip (version 6 or later) with the -t <directory> flag to copy the libraries into the folder you created in the previous step. For example:

        pip install -t lib/ <library_name>

3. Create a file named appengine_config.py in the same folder as your app.yaml file.

4. Edit the appengine_config.py file and provide your library directory to the vendor.add() method.

        # appengine_config.py
        from google.appengine.ext import vendor

        # Add any libraries install in the "lib" folder.
        vendor.add('lib')

The appengine_config.py file above assumes that the current working directory is where the lib folder is located. In some cases, such as unit tests, the current working directory can be different. To avoid errors, you can explicity pass in the full path to the lib folder using:

        vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))

# Setting up the Cloud SQL instance

1. Create a Second Generation Cloud SQL instance and configure the root user.
2. If you don't want to use the root user to connect, create a user.
3. Using the Cloud SDK, get the Cloud SQL instance connection name to use as a connection string in your application code:

        gcloud sql instances describe [INSTANCE_NAME]

Record the value returned for connectionName. You can also find this value in the Instance details page of the Google Cloud Platform Console. For example, in the Cloud SDK output:

        gcloud sql instances describe instance1
        connectionName: project1:us-central1:instance1

4. To make a connection to the Google Cloud SQL use the cloud proxy script:

        ./cloud_sql_proxy -instances="mywaterbuffalo-178002:us-central1:mysqlwaterbuffalo"=tcp:3316

