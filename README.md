# Shortcode

## **Overview**

Shortcode is project that enables shortening / assigning aliases to url making redirection more cleaner. It uses a whole API structure using Django Rest Framework to make necessary API calls.

### **Features**

Shortcode provides the below features:

1. Assign short codes to urls, making navigation easier.
2. Navigate to urls using alias / shortcodes.
3. Get usage stats for the url aliases.

## **Installation**

1. Install Python 3.9+.
2. Install virtualenv package via pip.
3. Create a virtual environment using by - _virtualenv \<env-name\>_
4. Navigate to the environment directory and activate by - _.\Scripts\activate_. Once activated, the environment name will be prefixed to the path in the terminal.
5. Navigate to within the project directory.
6. Refer to the _requirements.txt_ file within the project directory and install all the packages enlisted by - _pip install -r requirements.txt_.
7. Run the command - _python manage.py runserver_ to verify the development server running without any errors.

If there is any problem with the installation process, send your queries to *amitabhpal0210@gmail.com*.

## \*\*Things that could have been done

1. Add urls for-\
   a. getting all existing shortcodes
   b. updating any existing shortcode
   c. adding API documentation
   d. changing the text for 404 error
   e. adding more unit test cases
   f. make the 'readme' documentation more cleaner
   g. adding pytest config to the project
   h. making the project compatible with linux

## **Third-party integrations**

The third party packages used for the project are as below.

1. rest_framework - for API architecture
