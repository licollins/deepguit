# deepguit
The DeepGUIT is a test tool that aims to generate tests through exploration of the android application .​

*Environment requirements:
  - Ubuntu 18 or later
  - python 3.8.5
  - TensorFlow 2.2.0
  - UI Automator 0.3.6
  - Android SDK
*Download the DeepRLGUIMAT.zip available in https://1drv.ms/u/s!Avu7qFzImegrh7FyBW7g0U4lddA9Qw?e=bOunEj
*Extract the zip file in a folder
*The structure of the folder is:

![image](https://user-images.githubusercontent.com/14595529/151639541-72cbd24b-2dd8-48a5-bd39-5570d024c479.png)


*Fill the settings.txt file such as the example below:

APK NAME:app.apk (or path until apk)
PACKAGE:app.package.com
RESOLUTION:1520x720
COVERAGE:yes
REQUIREMENT:yes
TIME:7200

*If you have the input entry requirements(REQUIREMENT:yes), fill the file requirements.csv, example bellow:

activity	    field	         id	       action	 type	  size_start	size_end	value
app activity	button	    id/menu	      click	  none				
app activity	edittext	id/NameEdit	    type	  text	    1	          30	   test
app activity	edittext	id/valueEdit	  type	  number	  1	           9	    150
app activity	button	  id/action_save  click	  none			

*obs: to collect coverage values, use Jacoco coverage tool (https://www.geeksforgeeks.org/how-to-generate-global-coverage-report-in-android-development-using-jacoco-plugin/)

*Execution:
- In the DeepRLGUIMAT folder, open the terminal and type ./DeepRLGUIMAT, then Enter, and the tool should execute.

