# Overview

The objective of the project is to demonstrate:

1. Using Github to complete continuous integration of an application; and
2. Using Azure Pipeline to perform both continuous delivery of an application.

## Project Plan

* A link to a Trello board for the project, [My Trello Board](https://trello.com/invite/b/GLPEQyB4/ATTId0375e6f976ea3a3b997051cbf2e9acb9F5AEA86/udacity-ci-cd-project)
* A link to a spreadsheet that includes the original and final project plan, [High-Level Project Plan](https://1drv.ms/x/s!Au3p6w0ds_fCgqBlz-rW5nQ475YwlA?e=mbFlLI)

## Instructions

* Architectural Diagram (Shows how key parts of the system work) is as follows:  
  

![alt text](img/Architecture.drawio.png "Process Flow Diagram of the workflow")

### Setup Instructions

* Setting up a `Github` repository for this `Azure Webapp` Service. 
    * Go to your Github how page, either using the `New` button on the left hand side repository panel or the drop down `+` menu on the top right hand corner and select `New Repository` to create a new repository.
    * Enter the new project name and select `python` at the `.gitignore` button so that Github will automatically exclude keeping track on some system generated files other than your source code.
    * The following screen show the screen creating the Github project:
    ![alt text](img/Github-create-project_1.1.1.png "Github Create Project")  

* Project cloned into Azure Cloud Shell
    * open Azure Cloud Shell from your Azure Portal
    * ensure you have setup the SSH access to your Github account on your Azure Cloud Shell.  Detail procedure could be found in [Connect With SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh), and [Add a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) from Github documentation.
    * Then, you can copy the SSH link of your newly created repository and using the following comand to clone your repository to your Azure Cloud Shell.
        ```bash
        anthony [ ~ ] $ git clone <your-github-project-ssh-link>
        ```
    * The following shows the screen after successful cloning repository from Github.
    ![alt text](img/git-cloned.png "Repository cloned")  


* Passing tests that are displayed after running the `make all` command from the `Makefile`
    * Then we can create scafolding code for testing of Github Action, including `hello.py`, `Makefile`, `requirements.txt` and `test_hello.py`.
    * We should create a virtual python environment for the code testing and continuous integration such as the following:
        ``` bash
        anthony [ ~ ]$ python -m venv cicd
        anthony [ ~ ]$ source cicd/bin/activate
        ```
    * Then, we should edit the `Makefile` to include the actions required for 2 stages, i.e. `install`, `lint`, and `test` as follows:
    * The we can run `make all` on Azure Cloud Shell to check any possible errors on our scaffolding codes.  The pass result should be similar as follows:
    ![alt text](img/successful-make-all_1.9.1.png "Successfully run \'make all\'")  
    
* Output of a test run
    * After `make all` is passed, we can create a `Github Actions`.
    * Go to your `Github` repository page and select the `Actions` tab.  Then, `Github` will suggest templates for your project.  For simiplicity, `Python Application` us selected.
    * Then, we have to modify the `python-app.yml` to do '`make install`', '`make lint`', and '`make test`' at different stages of `Actions`, for example as shown in the following screen capture. 
    ![Alt text](img/edit-github-action_1.12.1.png)  
    * Then, use the "`Start Commit`" button on the top right hand corner to commit the edited file to push to your repository.  Once new commit is pushed to the repository, the `Github Actions` will start to run the integration jobs as stated in the file.
    * If everything is fine, the following results could be found.
    ![Alt text](img/github-actions-results_1.14.1.png)
    ![Alt text](img/github-actions-results_1.14.2.png)  

* 
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


