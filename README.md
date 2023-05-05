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

* Prepare the Flask Starter code and Configure the Azure Pipeline for Continous Delivery
    * Copy all neccessary Flask Starter files, including at least `app.py`, `requirements.txt`, `Housing_price_models/*`, `README.md`, `make_prediction.sh`, and `make_predictt_azure_app.sh`.
    * Test whether the flask application can run on Azure Cloud Shell, 
        * "`make install; python -m flask run`"
        * Check the port of the flask program is running and then edit the `make_prediction.sh` with the correct port number, then we should have the correct prediction and result like to followin:
        ```bash
        anthony [ ~ ]$ ./make_prediction.sh
        Port: 5000
        {"prediction":[20.35373177134412]}  
        ```
    * Test if we can deploy the starter code as an Azure Webapp service,
        * using command, "`az webapp up -g <resource_group> -n <app_name>`"
        * after the successful deployment of the webapp, we should have the URL to access from the retuen JSON output.
        * Check the Azure portal or follow the link from the result to check if the service endpoint is up and running.
        * Then, edit the correct URL in the `make_predict_acure_app.sh`.  IF the service runs, we should have the result like the following:
        ```bash
        anthony [ ~ ]$ ./make_prediction.sh
        Port: 443
        {"prediction":[20.35373177134412]} 
        ```  

* Then, we can setup the azure pipeline ans we could referred the details to the [offical documentation](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
    * Go to Azure Devops to create your development organization and create a new project.
    * Go to your new project and select `Pipeline` from you left hand side panel, and then create a new pipeline.
    * Select repository as "Github", select your project code repository and then anthenicate and authorize Azure Devops to access your Github repository.
    * Then configure using "Python to Linux Web App on Azure" as template to configure your pipeline. Then, we have to authorize the Pipeline to use your Azure resources.
    * Edit the pipeline YAML file, at least using the correct version of python.
    * After "Save and Commit" the YAML file, the new file will be committed to your repository and then pipeline will execute.  

 * Then, we can test the newly automatic deploy webapp by using "make_predict_azure_app.sh", the successful result will be similar to the following:
    ```bash
    anthony [ ~ ]$ ./make_prediction.sh
    Port: 443
    {"prediction":[20.35373177134412]} 
    ```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


