Presentation

What this notebook does
This notebook demonstrates a reproducible data-processing pipeline for a study on time-of-day (ToD) effects in working memory (WM). It ingests multi-source data, performs cleaning and harmonization, and outputs analysis-ready tables for downstream statistical modeling.

Study aim
We assessed whether functional components of WM exhibit independent variations in performance across the day. Specifically, we examined accuracy and reaction time (RT) across classes of WM tasks with distinct functional demands.

Design & tasks
Participants completed four sessions in a within-subject, repeated-measures design at 09:00, 13:00, 17:00, and 21:00.
Tasks included:
•	Complex spans (Reading, Operation, Symmetry) indexing concurrent storage + processing in verbal, numeric, and visuospatial domains.
•	The working memory updating task measuring the ability to update mental representations.
•	The binding and maintenance task assessing the capacity to bind elements into coherent structures.
Participants & screening
Eligible participants were Portuguese adults (18–35) with ≥ high-school education and moderate chronotype (indifferent, moderately morning, or moderately evening). Exclusions covered psychiatric, sleep, neurological conditions, and clinically significant symptoms. To ensure that the participants met the inclusion/exclusion criteria, participants completed a sociodemographic questionnaire, along with the Portuguese versions of the Brief Symptom Inventory and the Morningness-Eveningness Questionnaire on an online platform (Psytoolkit).
Protocol controls
From the moment they were accepted into the study until the completion of the experimental procedures, participants maintained a regular sleep schedule (23:00–01:00 sleep onset; 07:00–09:00 wake), limited caffeine (≤3/day) and alcohol (≤2/day) intake, and avoided sleep aids. Compliance was monitored via sleep and activity diaries (completed in Psytoolkit) and actigraphy (worn on the wrist of the non-dominant hand). 
After five days in this regime, participants completed a practice session to minimize potential learning effects. 
The day after the practice session, participants completed the five WM tasks in four sessions held at different ToD: morning (09:00 h), midday (13:00 h), afternoon (17:00 h), and evening (21:00 h). 

Data sources
•	Online questionnaires (Psytoolkit).
•	Sleep and daily logs (Psytoolkit).
•	Actigraphy (actigraph worn on non-dominant wrist).
•	WM tasks (programmed in Python and run on local platform).
What you’ll find here
For demonstration, we include an anonymized subset (n = 4). The pipeline:
•	Merges heterogeneous sources, 
•	Aligns timestamps, standardizes variable names, computes trial- and aggregate-level metrics,
•	Exports tidy, analysis-ready datasets
How to run
•	Click the Binder badge at the bottom of this section. 
•	Once Binder is launched, execute cells with Ctrl/Cmd + Enter.
•	Locally: download the .py script “Data_Cleaning_Chrono.py” and run with a local Python 3 environment. 
Notes
•	All data are de-identified.
•	This notebook focuses on processing and reproducibility; inferential results are out of scope for this portfolio demo.

[![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FabioATMonteiro92/DataCleaning-Processing/HEAD?labpath=notebook%2F01_data_processing_script.ipynb)


