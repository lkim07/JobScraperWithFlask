# JobScraperWithFlask
Job Scraper with Python(Back-end) and Flask(Front-end)

## Backend:
  ### Python: 
    features:
      1. scrap job postings from these three websites:
            berlinstartupjobs.com
            weworkremotely.com
            web3.career
      2. write csv file 

## Frontend:
  ### Flask and Pico CSS: 
  I chose Flask as it supports the history.back() and history.go() without any trouble. The Pico CSS provides various designs with less effort. 
    features:
      1. search bar
      2. progress bar is shown when the search form is submitted.
      3. Previously searched keywords are shown in the top left corner as dropdown format. By changing the keywords, the searching result are changing but with less time because the previous results are stored in a db dictionary. 
      4. A button to move to home page on top right corner.
      5. can download the searched job's csv file. 

## To run the program:
  1. run the main.py on your VS code 
  2. http://localhost:5000/
     
## 
main home page:
<img width="941" alt="image" src="https://github.com/user-attachments/assets/eddc241c-41a0-4c7a-b35c-e26bf6269775">

progress bar:
<img width="942" alt="image" src="https://github.com/user-attachments/assets/176c6694-da3e-4e16-a51d-b98d25f3b210">

search page
search python
<img width="943" alt="image" src="https://github.com/user-attachments/assets/577f0283-8ff0-4d59-8ece-2cfd06c4c02c">

dropdown bar after search React
<img width="935" alt="image" src="https://github.com/user-attachments/assets/3e2e6f5c-17cf-464c-99d8-56a269e543a3">
dropdown bar after search Java
<img width="193" alt="image" src="https://github.com/user-attachments/assets/fcfa9656-7222-4a28-8264-459fef9529a2">


In search page
<img width="200" alt="image" src="https://github.com/user-attachments/assets/5f89cd24-b346-4711-b333-ba48cd33309e">
store previous searched keyword

right corner: move to the home page.
<img width="209" alt="image" src="https://github.com/user-attachments/assets/ccdc12d4-548b-4be1-8684-4ed2355351fa">

export link: download .csv file
<img width="135" alt="image" src="https://github.com/user-attachments/assets/ac64dac8-611d-4ee6-980d-0e7d12f6c433">

 ## Difficulty while making this project:
  1. showing the same results even I changed the keyword from the dropdown lists. For example, scraping result of 'python' were there first. Then I searched 'react', but the result shown in the '/search' is the combination of the 'python' and 'react' results. It wasn't changed even I clicked another keyword from the dropdown bar.
     This was because I stored the list all_jobs as a global variable in the job_scraper.py. Therefore, I changed the list as a local variable and assigned it as separately to store only one keyword.
     
 ## Features for later development:
   1. use pico css's switch feature to change the displayig style. (ex. from current container to card or Accordion)
   2. remove the link and making the card as a like. 
