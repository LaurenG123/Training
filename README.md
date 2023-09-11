
```json

 DISCLAIMER: certain files may contain property originating from SpartaGlobal

```







# My 8-Week Training Repository



![Readme Quotes](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=dracula&quote=Sparta%20Global%20is%20on%20a%20mission%20to%20help%20organisations%20invest%20in%20diverse%20emerging%20talent%2C%20closing%20the%20digital%20skills%20gap%20and%20adding%20significant%20social%20value%20through%20its%20quality%2C%20flexible%2C%20and%20sustainable%20technology%20HTD%20model.&author=SpartaGlobal
)


#### *The purpose of this repository is to display projects completed and started during the duration of the Spartaglobal training period spanning 8 weeks. Each file has been grouped and ordered with the following schema :*




***
>In Training Repository Contents
<table border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<thead>
		<tr>
			<th scope="col" style="width:43px">&nbsp;</th>
			<th scope="col" style="width:443px">Files</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th scope="row" style="width:43px">1</th>
			<td style="width:443px"><a href= "https://github.com/LaurenG123/Training/blob/main/1%3A%20Python%20Scrabble.py">Python Scrabble</a>
</td>
		</tr>
		<tr>
			<th scope="row" style="width:43px">2</th>
			<td style="width:443px"><a href="https://github.com/LaurenG123/Training/blob/main/2%3A%20Python%20Calculator.py">Python calculator (for basic functions)</a></td>
		</tr>
		<tr>
			<th scope="row" style="width:43px">3</th>
			<td style="width:443px"><a href="https://github.com/LaurenG123/Training/blob/main/3%3A%20Control%20Flow%20Exercises.py">Python control flow examples</td>
		</tr>
		<tr>
			<th scope="row" style="width:43px">4</th>
			<td style="width:443px"><a href="https://github.com/LaurenG123/Training/blob/main/4%3A%20Python%20Functions.py">Python functions further examples</td>
		</tr>
		<tr>
			<th scope="row" style="width:43px">5</th>
			<td style="width:443px"><a href="https://github.com/LaurenG123/Training/blob/main/5%3A%20Python%20OOP.py">Python Introduction to OOP</td>
		</tr>
		<tr>
			<th scope="row" style="width:43px">6</th>
			<td style="width:443px"><a href="https://github.com/LaurenG123/Training/blob/main/6%3A%20Python%20classes.py">Python classes</td>
		</tr>
		<tr>
			<th scope="row" style="width:43px">7</th>
			<td style="width:443px"><a href="https://github.com/LaurenG123/Training/blob/main/running_pokecode.py">API and csv files</td>
		</tr>
	</tbody>
</table>

***

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=LaurenG123&theme=dracula)](https://github.com/LaurenG123/Training-stats)

***
## Apps with python (KIVY)

The follwowing screenshots are from a window opening in my terminal when the python code is run. As can be noted the program itself runs like an app simulating a battle between two pokemon input by the user. Each pokemon corresponds to an api end point from: https://pokeapi.co. Each input must correspond to a pokemon listed consequently outputing the kind of attacks used by that pokemon in the api database and detracting from its health (also listed on the database) with each subsequent attack. A popup with open to show the winner of the round, and ascrollable battle log is also available. With linux this could be developed very easily into a downloadable form of app however ability to do this using mac is limited to the size of available storage that could be attributed to running a partition. <a href= "https://github.com/LaurenG123/Training/blob/main/running_pokecode.py">Try the pokemon game code.

The only requirement for running the code is to have kivy installed. You can do this through the Pycharm terminal:



		pip install kivy




<img width="300" alt="Screenshot 2023-09-05 at 18 13 39" src="https://github.com/LaurenG123/Training/assets/72687468/9fb1243f-167a-4429-bd8f-ba6052d48fdd">


<img width="300" alt="Screenshot 2023-09-05 at 18 14 01" src="https://github.com/LaurenG123/Training/assets/72687468/2ed31409-baff-412d-98f1-d416ce7cf747">

<img width="300" alt="Screenshot 2023-09-05 at 18 14 27" src="https://github.com/LaurenG123/Training/assets/72687468/6773bf90-ab0c-4280-93fb-3742876ef8eb">


The program also implements a try and except clause to mitigate any problems that may arise if a pokemon that does not correspond to one existing in the database is input by the user. Also note that the program admits inputs in either lower or uppercase... or a mixture of both!!

<img width="300" alt="Screenshot 2023-09-05 at 18 25 43" src="https://github.com/LaurenG123/Training/assets/72687468/17177125-f4ea-4a99-ab47-203089f7e4c4">

In addition to game play, the code creates a csv file containing a readable battle log that is updated with each consequent game. When no file exists, it is created. 

<img width="300" alt="Screenshot 2023-09-11 at 16 24 36" src="https://github.com/LaurenG123/Training/assets/72687468/4f1c1542-d48e-4e33-aba6-68a2fdeb8ae4">


*Could be improved: the build could be contained in a .kv file instead of as a function in main*


***

## Restaurant Project

The restaurant project is a task set by sparta global where a main file and .py file are given containing test conditions and a means to test a code written into the restraunt.py file. The guidlines set for the task were as follows: 

<img width="794" alt="Screenshot 2023-09-11 at 15 54 02" src="https://github.com/LaurenG123/Training/assets/72687468/1ace8e05-fc46-4183-bc89-896d45217858">

Based on these guidlines it was necessary to use trello (inspired by Kanban an AGILE methodology) to approach the task outlineing user stories and acceptance criteria (Gherkin method) to proceed with the tasks requirements. 

<img width="1419" alt="Screenshot 2023-09-11 at 16 03 18" src="https://github.com/LaurenG123/Training/assets/72687468/dde44cd6-d554-4079-abf2-66f40608eab7">

Access to the expanded Trello post-its can be found <a href= "https://trello.com/b/Q6KRUxO0/restraunt-project">on my Trello board.

Note that the gherkin style acceptance criteria are written into the comment section of the post-it for space purposes.
The final code written to satisfiy the test criteria is saved as <a href = "https://github.com/LaurenG123/Training/blob/main/restaurant.py">"restaurant.py". 


The test criteria "test_module.py" was provided by SpartaGlobal. To check the code runs satisfactorily, in regards to the unit test criteria, it is necessary to import the "restaurant_main.py" file into main, then run. 

<a href = "https://github.com/LaurenG123/Training/blob/main/Restaurant_main.py">"restaurant_main.py"


<a href = "https://github.com/LaurenG123/Training/blob/main/test_module.py">"test_module.py"


The output should then be: 

<img width="833" alt="Screenshot 2023-09-11 at 16 07 53" src="https://github.com/LaurenG123/Training/assets/72687468/59e32a27-91a7-40fa-b652-1ef1dd57a96f">

***
## Jupyter Notebook

The following Jupyter Notebook project details data cleaning and visualisation. It examines data extracted from two open source csv files that can be found on kaggle. The methodology and tools used during the project are detailed in the report: 
<img width="1095" alt="Screenshot 2023-09-11 at 16 39 21" src="https://github.com/LaurenG123/Training/assets/72687468/e0453d84-e8e7-4e4f-b2c0-3d9e75038fc0">

The use of data visualisation tools and libraries such a Pandas, NumPy and Matplotlib are of great importance to the project and should be installed. Example graph requireing additional imports for interactability. <a href= "https://github.com/LaurenG123/Training/blob/main/project.ipynb">See Project



<img width="300" alt="Screenshot 2023-09-11 at 16 39 47" src="https://github.com/LaurenG123/Training/assets/72687468/b9310111-d733-4b39-88c3-feae51c49ad7">
<img height="290" alt="Screenshot 2023-09-11 at 16 44 36" src="https://github.com/LaurenG123/Training/assets/72687468/50152eea-2956-42d8-bbf5-04d70ab88172">

Other visualisatins not included in this readme file include interactive functions that can be used further in the creation of dashboards. Certain elements such as these may not be viewable through github but can be viewed directly in jupyter notebook. For this, make sure to install the necessary imports: 


			import pandas as pd
			import matplotlib.pyplot as plt
			import matplotlib.cm as cm
			import numpy as np
			import seaborn as sns

			# Necessary visual imports
			import ipywidgets as widgets
			from IPython.display import display
			import panel as pn
			from bokeh.plotting import figure, show, output_notebook
			from bokeh.models import HoverTool, ColumnDataSource, Slope
