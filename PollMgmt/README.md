***POLL MGMT***


We want to create a small poll management.
To do this, implement the following classes:


**User**: each characterized by:
+ id (automatic alphanumeric);
+ name (alphabetic with spaces);


**Question**: characterized by:
+ id (number);
+ question (alphanumeric);
+ Type answer: open(alphanumeric) or close;


**Poll**:
+ List of questions ;
+ List Users;
+ One instance of Results;
With methods for:
+ constructor which reads list of text files;
+ writing on file;
+ results acquisition;


**Results**: having:
+ table *_tab_* (user x questions) of answers based on each id
And methods for results analysis(for single questions):
+ compute media (only for numeric answer)
+ compute moda (most quoted answer)
+ print histogram


**Test**: Simulation of a Poll with Questions to closed multiple
choice obtained from file (of text):
+ acquisition of new survey from file with random creation
of a list of at least 20 users
+ Simulation of the random acquisition of answers from users;
+ For each survey question:
  + demonstration of the use (print) of at least
  one of the methods of analysis
+ Serialization of completed survey