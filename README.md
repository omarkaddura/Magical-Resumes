


To bootstrap a new Next.js application, we need to create a new project directory and install the required dependencies using NPM (Node.js Package Manager).

Open a new terminal window (Ctrl+Alt+T on Linux or Command+Space on Mac) and execute the command below to create a new project folder that will house your Next.js application (replace your-project with the name of your project):

Command
mkdir your-project
And cd into your new directory:

Command
cd your-project
Next, run this command to initiate a new Node.js application and create a package.json file in the root of your project:

Command
npm init -y
The npm init -y command creates a package.json file in the root of your project directory. The -y flag initializes the file with default values.

The package.json file will allow you to easily install and use NPM package dependencies in your project. It will also make things like sharing your project with other developers easier if you wish to do so in the future.

Check out the NPM documentation if you want to learn more about the contents of the package.json file.

Now that we have a package.json file created, we can install the required NPM package dependencies for your Next.js website.

To get started, we'll need the Next, React, and React-Dom NPM packages.

You can install all of them at once with this command:

Command
npm install --save next react react-dom

start the application in development mode with this command:

Command
npm run dev
