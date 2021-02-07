> # Expenses Tracker APP 


# Installation
1. Run

  `pip3 install -r requirements.txt`. 

2. Create config.py. 

	*Prerequisite = A pre-existent database in a MySQL server*

	Rename config_template.py to config.py and fill in the 	information required.
	

3. Run 

	`python3 create.py`

3. Run 

	`python3 app.py` 


# Documentation 

The following document contains the breakdown of the development process of "Expense Tracker App".
This web application aims to help its users keep their day-to-day expenses under control.

The agreed requirements for this project / app are the following:

- An application with full CRUD functionality, using the following technologies (which we have learned during the last 4 weeks):

	* Databases (MySQL / SQLAlchemy)
	* Python Programming Language
	* Python Web Development: Flask / Gunicorn
	* Continuous Integration: Jenkins
	* Version control: Git
	* Unit Testing with Python: Pytest
	* Cloud Fundamentals


## User Goals & User stories

	

**The main objective** of creating this application is to put into practice the acquired knowledge, in a case similar to real life.

Therefore, the **first step** will be to define **who** would be the user of this application and **why** that person would want to use this tool.

>The targeted audience for this application are people who want to understand how are spending their money in order to better control their personal finances. 

Taking this information into account, we can start working on **user stories** and try to define what expectations our user may have.

![](https://trello-attachments.s3.amazonaws.com/6020265bdff1687e04112767/1189x339/f08c2f82d3e41a1d902ba430d76eeb33/Screenshot_2021-02-07_at_15.41.07.png)



(*)In order to satisfy, the MVP, I have prioritized the user stories that were focused on CRUD functionality and have left two of the stories (related to the visualization of expenses) for future releases.

## Project Tracking
A Trello Board has been used to keep a constant tracking of my activities, where I have been annotating the tasks derived from user stories and all significant changes, trying to emulate the Agile methodology at all times.


![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/9597faf1964abd9a3d1e25418d7c32ec/Screenshot_2021-02-07_at_11.50.46.png)
 


The appearance of the board, during development.

![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/6525d82867925e4774129ab1de058221/Screenshot_2021-02-07_at_12.14.20.png)

The board has evolved as the development of the application did. Given the presence of blocks, I added a new tab called "Blocked" where the problems, that have needed investigation and a trial/error approach, are noted.

<img src="https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/c985c81d09b4a10d974cd08e0651b5d8/1.png"/>
The appearance of the board, at the end of development. 

![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/b564559c30cd6207b0b4bf16c4aeeca3/Screenshot_2021-02-07_at_12.52.45.png)

## Relational Database

The following diagram shows which tables will be created and what is their relationship (One to Many).

The application has two tables: Users and Expenses.

* **Users** will store the personal data of our user such as their name and email
* **Expenses** will store the information about the type of expenses of each user, a description, the date of purchase/expense and finally the amount spent.

![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/e4dc62f2bb79324f371cc51c153ba9b6/ERD.png)

## CI - Pipeline

Once the bases of our project were defined, we began to code our application. This is when we start to go through our CI pipeline.

The code is created by the developer (VSCode, Python, Flask) and in order to track any changes, we use a VSC. After that, the CI server (Jenkins) handles all the automatic building, testing and deployment of the application. Once finished, a report is generated and if there is any failure, the developer is informed.  Based on a Continuous Deployment approach, there is a final quality test before the application is ready for the Live Environment.

Every time the set of assigned tasks has been completed, we return to the Backlog (Trello) to find out what our next task or set of tasks is.

![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/0294b5d8d1b4d82ee295783fc5fbf41c/CI_Pipeline.png)

## Risk Assessment

The following Risk Assessment identifies hazards and risk factors that have the potential to cause harm to our application deployment. I have listed the prevention measures that I have used to control the risk when the hazard cannot be eliminated.

![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/de248592696ffc12cd6acaa1a1fd1c92/RiskAssesstment.png)

## Test results & Coverage 
Two testing frameworks: Pytest and Unittest have been used in order to achieve the desired coverage level.



![](https://trello-attachments.s3.amazonaws.com/6020264c7ca5b50f2469aef0/6020265bdff1687e04112767/93f4354c6f5d25a782ddb3fa76dbb21c/test.png)

In this case, this application has been 100% tested in its relevant parts.

![](https://trello-attachments.s3.amazonaws.com/6020265bdff1687e04112767/937x423/46c872d33ca17c4068c4033ff94a1ac9/coverage.png)


## External Resources

**Trello Board:** [Trello Board - Expenses Tracker App
](https://trello.com/b/k6vhxiJ9/expensestrackerapp)

**Power Point Presentation:** [Power Point Presentation - Expenses Tracker APP](https://docs.google.com/presentation/d/1X2QrywuLPMiYRns1P_OFashKPquyZcPonaS0C_xDbig/edit#slide=id.p)
## Future Releases 

After the application deployment has been completed, there are some additions and improvements that I would like to accomplish:

- Improve the appearance of the application
- Show expenses by categories and their evolution over time
- Add the functionality to share expenses automatically with another person
- Add the functionality to notify the user when they spend more than planned



	

# Autor 

Andrea Torres-Jaramillo