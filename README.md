# DRL-MOBTEST

The DRL-MOBTEST is a test tool that aims to generate tests through exploration of the android application .​

*Environment requirements:
  - Ubuntu 18 or later
  - python 3.8.5
  - TensorFlow 2.2.0
  - UI Automator 0.3.6
  - Android SDK
  
*Download the DeepRLGUIMAT.zip https://1drv.ms/f/s!Avu7qFzImegrkYgjs-cSGsAYBDKZOw?e=hVcWux

*The tool DRL-MOBTEST is bundled into executable files to run in Linux. You don't need to install any other python dependency; just downloading all the files will suffice. The application under test may be in the DRL-MOBTEST folder; the tool will install the app, and it can run in a physical phone connected to a computer or in an Android virtual machine

*Extract the zip file in a folder
*The structure of the folder is:

![image](https://user-images.githubusercontent.com/14595529/151639541-72cbd24b-2dd8-48a5-bd39-5570d024c479.png)


*Fill the settings.txt file such as the example below:

![image](https://user-images.githubusercontent.com/14595529/151639636-5bcbb00e-8a1e-4cad-9ede-fc3fb44645ec.png)


*If you have the input entry requirements(REQUIREMENT:yes), fill the file requirements.csv, example bellow:

![image](https://user-images.githubusercontent.com/14595529/151639743-fb80751a-47f1-488a-9a45-02e32125d9f8.png)


*obs: to collect coverage values, use Jacoco coverage tool (https://www.geeksforgeeks.org/how-to-generate-global-coverage-report-in-android-development-using-jacoco-plugin/)


*Execution:
- In the DRL-MOBTEST folder, open the terminal and type ./DeepRLGUIMAT, then Enter, and the tool should execute.

- To run the tool with no input requirements, fill in the settings.txt file on the Requirements:no line. 

** To include the reference: Eliane Collins, Arilo Neto, Auri Vincenzi, and José Maldonado. 2021. Deep Reinforcement Learning based Android Application GUI Testing. Brazilian Symposium on Software Engineering. Association for Computing Machinery, New York, NY, USA, 186–194. DOI:https://doi.org/10.1145/3474624.3474634
