
![Typing speed test]( https://github.com/shreyamalogi/Typing-Speed-Test-app/blob/main/TYPING%20SPEED%20TEST/output%20video/typingspeedtestgif.gif )

# Typing Speed Test app


This is a simple web application built with Flask that allows you to test and improve your typing speed. It provides you with random sentences to type, calculates your typing speed (words per minute - WPM), and gives you immediate feedback on your typing skills.

## Why This Project?

Are you looking to improve your typing skills or test your typing speed? This project is a fun way to do just that. It helps you practice typing with randomly generated sentences and provides instant feedback on your performance. Whether you're a student, a writer, or anyone who uses a keyboard, enhancing your typing speed is always beneficial.

## Tech Stack used: 
`Python` `Flask` `HTML/CSS` `JavaScript` `Jinja2`

## How to Use

1. Clone the repository to your local machine.
2. Install Flask if you haven't already by running `pip install Flask` in your terminal.
3. Run the application by executing `python app.py` in your terminal.
4. Open your web browser and navigate to `http://localhost:5000`.
5. Start typing the sentence displayed on the screen as fast and accurately as possible.
6. Once you've finished typing, your typing speed in WPM will be calculated and displayed.

## Features

- Randomly generated sentences for typing practice.
- Real-time calculation of your typing speed (WPM).
- User-friendly and responsive web interface.

**Author:** Shreya Malogi

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MIT License

Copyright (c) 2023 Shreya Malogi

## Contribute

Found a bug or have a feature request? [Open an issue](https://github.com/yourusername/typing-speed-test/issues) or [fork the project](https://github.com/yourusername/typing-speed-test/fork) and submit a pull request. Your contributions are always welcome!

If you find this project useful, please consider giving it a star on GitHub to show your support. Thank you!


## Further steps-

To deploy a Flask application on AWS Elastic Beanstalk, you will need to configure your project properly. Here's a general outline of the steps to set up your Flask application for deployment on Elastic Beanstalk:

1. **Create a Flask Application:**
   Ensure you have a Flask application that is working correctly on your local machine.

2. **Project Structure:**
   Make sure your project structure is organized. A basic structure might look like this:

   ```
   your_project/
   ├── application.py  # Your Flask app's entry point
   ├── requirements.txt  # List of required packages
   ├── .ebextensions/   # Optional: Elastic Beanstalk configuration files
   ├── static/          # Folder for static files (CSS, JavaScript, images)
   ├── templates/       # Folder for HTML templates
   └── ...
   ```

3. **`requirements.txt`:**
   Create or update your `requirements.txt` file to include all the dependencies needed for your Flask application, including Flask itself. You can generate this file using `pip freeze`:

   ```
   pip freeze > requirements.txt
   ```

4. **AWS Elastic Beanstalk Configuration:**
   Elastic Beanstalk uses a `config.yml` or `.ebextensions/` folder to define its configuration. You can use these to specify various settings for your application, like environment variables, database connections, and more.

   Here's a sample `.ebextensions` configuration for a basic Flask app:

   ```yaml
   option_settings:
     aws:elasticbeanstalk:container:python:
       WSGIPath: application:app
   ```

   In this example, `application` is the name of your Flask application file, and `app` is the Flask instance within it.

5. **Create an Elastic Beanstalk Application:**
   Create an Elastic Beanstalk application using the AWS Management Console or AWS CLI.

6. **Upload Your Code:**
   Upload your project code (including the `requirements.txt` file) to Elastic Beanstalk either via the AWS Management Console or the AWS CLI.

7. **Environment Configuration:**
   Configure your environment settings using the AWS Management Console or the AWS CLI. This includes setting environment variables, instance type, scaling, and other options.

8. **Deploy Your Application:**
   Deploy your application to Elastic Beanstalk using the AWS Management Console or the AWS CLI.

9. **Access Your Application:**
   Once the deployment is complete, you can access your Flask application via the Elastic Beanstalk URL provided.

10. **Monitoring and Scaling:**
    Monitor your application's performance and set up auto-scaling and other AWS services as needed.

