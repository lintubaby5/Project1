<h1>HOW SAFE IS TORONTO?</h1>
This project aimed to investigate the Toronto crime rates. The Toronto Police Department has an open data file available in this URL: 
https://data.torontopolice.on.ca/pages/open-data
<p>
<h2>Project Description:</h2>
This application is written in Python. The user needs to install or run locally in a machine the CSV files.

With this project we will identify the types of crime that happened in Toronto. The data retrieved in the CSV files are from 2014 to 2022. Data analysis included the top 3 crimes based on the premises type (outside, houses, apartment, commercial, etc) they happened, the occurance, the neighbourhoods affected. Lastly, we also predict the total number of crimes that will happen in 2023.
<p>
<h2>How to use:</h2>
No authentication like passwords or usernames is required. Feel free to give us a thumbs up if you like it.  

<p>
<h2>Content:</h2>

<h2>1-  What are the top 3 crimes committed in Toronto? </h2>

At first, we read all the crimes from the API and plot them in a piechart to identify the top 3 crimes.
The Top 3 Crimes are Assault, Theft from Motor Vehicle and Break and Enter. 

Assaut - 161833

Theft from Motor Vehicle - 76914

Break and Enter - 56466

These crimes are then analysed one by one to reach at a conclusion on which is the safest place, what is the safest time to be in Toronto and to predict the next year's total crimes

![CrimeAnalysis](https://user-images.githubusercontent.com/119901094/218620020-7eb475b5-fc9b-4ac3-889b-887089e96144.png)

---------------------------------------------------------------------------------------------

<h2>2-  What kind of premises are the most prone to crimes? </h2>

The data analysis showed that the top 3 crimes occurred mainly in the outdoors. Assaults are predominantly in apartments more than the double of houses. Thefts from motor vehicles happened outside followed by houses. Breaks and enters happened in commercial properties and houses.


<h2> Top 3 Crimes </h2>

![premises_all_480](https://user-images.githubusercontent.com/119235680/218617872-2ab7d26f-d583-45bc-ae69-b2632f6b4a87.png)


<h2> Assault  Crimes </h2>

![premises_assault_480](https://user-images.githubusercontent.com/119235680/218617864-7bee84d1-5bdf-48c7-b4b6-083c39bde28f.png)


<h2> Motor Vehicle Theft  Crimes </h2>

![premises_theft_480](https://user-images.githubusercontent.com/119235680/218617853-1afcd941-645b-4b65-9403-d7ae4d669a66.png)


<h2> Break and Enter Crimes </h2>

![premises_bne_480](https://user-images.githubusercontent.com/119235680/218617846-a41fd403-be4c-408b-beca-001f09130ef3.png)


---------------------------------------------------------------------------------------------

<h2>3-  What is the relationship between time and crime rates? </h2>

I have analysed the occurance hour of the top 3 crimes: Assault, Motor Vehicle Theft, and Break & Enter

Firstly, the common factor exisitng in all three, is the fact that the highest number of crimes are happen at 12am. After that, as each hour passes, the rate starts to drop. This could be due to lesser people being awake and outdoors. This provides an avenue for those committing the crime to have a lesser chance of getting noticed and caught. What's also interesting to see is that at 12pm, we see a peak of the number of crimes committed across all three.

<h2> Assault Crimes </h2>

![Assault Crimes by the Hour](
<img width="402" alt="ASSAULT LINE" src="https://user-images.githubusercontent.com/117491346/218629426-6cd0207c-f9cf-4b5f-9ae4-06c273d17132.png">)


<h2> Motor Vehicle Theft Crimes </h2>

![Motor Vehicle Theft Crimes by the Hour](<img width="400" alt="TMV LINE" src="https://user-images.githubusercontent.com/117491346/218629635-be2a1348-d83c-45b9-b29c-437abab780ed.png">
)


<h2> Break and Enter Crimes </h2>

![Break and Enter Crimes by the Hour](<img width="496" alt="BNE LINE" src="https://user-images.githubusercontent.com/117491346/218629595-e54a22b1-9ca5-40bb-a000-c038da7a0215.png">
)


---------------------------------------------------------------------------------------------

<h1>4-  What is the relationship between crimes and different areas in Toronto? </h2>

---------------------------------------------------------------------------------------------


Second step was to figure out the crime rates in Toronto neighbourhoods for each type.

1- Assault:

Waterfront Communities-The Island: 7,204 entries.

Church-Yonge Corridor: 6,300 entries.

Bay Street Corridor: 5,620 entries.

<img width="762" alt="ASSAULT" src="https://user-images.githubusercontent.com/117491346/218614603-8168662a-dca3-489f-9382-523a8ea16add.png">



2- Theft from motor vehicle:

Kensington-Chinatown: 2,980 entries.

West Humber-Clairville: 2,820 entries.

Waterfront Communities-The Island: 2,354 entries.


<img width="766" alt="TMV" src="https://user-images.githubusercontent.com/117491346/218614721-bf4cbd49-938a-45d3-97c6-27d1be8abf34.png">



3- Breaking and entering:

Waterfront Communities-The Island: 2,196 entries.

Church-Yonge Corridor: 1,656 entries.

Bay Street Corridor: 1,305 entries.


<img width="761" alt="BNE" src="https://user-images.githubusercontent.com/117491346/218614757-fb5df26f-8d8f-4eb8-b90b-aa8f132b9a15.png">

---------------------------------------------------------------------------------------------


<h2>5-  How did the crime rates change over the years? </h2>

The trend shows that crimes were increasing till 2020 and there is a significant low number of crimes in 2021 which we say after the Covid-19 outbreak when people are more stay at home


![YearlyAnalysisTop3crimes](<img width="497" alt="YEARLY TFMV " src="https://user-images.githubusercontent.com/117491346/218630002-80d60c22-4500-4e93-9167-9801b05dc15e.png">
<img width="502" alt="YEARLY BNE" src="https://user-images.githubusercontent.com/117491346/218630004-e909f1b2-1a6f-42b3-8166-51117eda9383.png">
<img width="499" alt="YEARLY ASSAULT" src="https://user-images.githubusercontent.com/117491346/218630005-2a9d8f7d-b409-492a-9fc2-072132bab0c2.png">
)

Once the total crime is plotted, a regression line is plotted to predict the next year's (2023) total crimes using Regression Analysis.


![YearlyTrendRegression](https://user-images.githubusercontent.com/119901094/218620228-064fd717-1128-4685-8361-7b1b7df82769.png)

The number of crimes in 2023 forecasted as per this info will be 36251.


<h2>Credits:</h2>
This project was made by the jointed efforts of a team of collaborators listed below:
<ol>Lintu Baby - https://linkedin.com/in/lintu-baby-80906870
<ol>Zaid Al Dulaimi - https://linkedin.com/in/zaid-dulaimi
<ol>Anumta Khan - https://linkedin.com/in/anumta-khan
<ol>Anabel Scaranelo - https://linkedin.com/in/anabel-scaranelo-md-phd-fsbi-6b3598144
