# mx-elections-2021

API to manage information from the candidates for the 2021 mexican elections.

This API is partially based on the [Popolo JSON specification](https://www.popoloproject.com/specs/)

##  Documentation

-   [General structure](general)
-   [Endpoints description](endpoints)
-   [Running app](run)

##  General structure

The API has endpoints with different methods enabled.

**For clients**, the `get` method is available.

**For developers**, the `get` and `post` methods are available on any endpoint.
And for any instance or entity on the endpoints the `get`, `put` and `delete` methods area available.

The available endpoints are:

- `person`: A real person, alive or dead.
- `membership`: A relationship between a person and a role.
- `contest`: A contest represents a single contest or race in an election. a single office may have 
  multiple contests in any given election.
  
- `party`: An organization that coordinates candidates to compete in a country's elections.
- `coalition`: A cooperation by members of different political parties.  
- `chamber`: A deliberative assembly within a legislature which generally meets and votes separately from the
  legislature's other chambers.
- `role`: A role represents a government position that a person can hold. this is often associated with 
  a political area.
- `area`: A geographic area whose geometry may change over time.

- `other-name`: Other possible names for a person.
- `profession`: An occupation founded upon specialized educational training,
- `person-profession`: List of professions associated with a person.
- `url`: List of URLs associated with a person.

- `export`: Gets all the information from the endpoints.
- `export-min`: Gets the minimum necessary information from the endpoints to represent the electoral race in process.

##  Endpoints description

###  ER model

Diagrams can be found in [docs folder](./docs).

- [XML version](./docs/mx-elections-2021-db-er-diagram.xml) from [diagrams.net](diagrams.net)
- [PNG version](./docs/mx-elections-2021-db-er-diagram.png)

![ER model](./docs/mx-elections-2021-db-er-diagram.png)

### Endpoints

####    person

|field_name             |require for input?|type            |description                                     |input value example                         |output value example                                                                                                                                                                                                |notes                                                                                                            |
|-----------------------|------------------|----------------|------------------------------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
|person_id              |no                |int             |Unique identifier                               |1                                           |1                                                                                                                                                                                                                   |On query the name of the field is id                                                                             |
|first_name             |**yes**           |string(50)      |First name of the person                        |Marina del Pilar                            |{<br/>&emsp;"en_US": "Marina del Pilar",<br/>&emsp;"es_MX": "Marina del Pilar"<br/> }                                                                                                                               |The output is on en_US and es_MX locales.                                                                        |
|last_name              |**yes**           |string(50)      |Last name of the person                         |Ávila Olmeda                                |{<br/>&emsp;"en_US": "Ávila Olmeda",<br/>&emsp;"es_MX": "Ávila Olmeda"<br/>}                                                                                                                                        |The output is on en_US and es_MX locales.                                                                        |
|full_name              |**yes**           |string(100)     |Full name of the person                         |Marina del Pilar Ávila Olmeda               |{<br/>&emsp;"en_US": "Marina del Pilar Ávila Olmeda",<br/>&emsp;"es_MX": "Marina del Pilar Ávila Olmeda"<br/>}                                                                                                      |The output is on en_US and es_MX locales.                                                                        |
|date_birth             |no                |date            |Birth date of the person                        |1985-09-19                                  |1985-09-19                                                                                                                                                                                                          |Date format is YYYY-MM-DD                                                                                        |
|gender                 |**yes**           |int             |Gender of the person.                           |2                                           |F                                                                                                                                                                                                                   |1 for male 2 for female                                                                                          |
|dead_or_alive          |**yes**           |boolean         |True if person is alive. Dead if person is dead.|true                                        |true                                                                                                                                                                                                                |-                                                                                                                |
|last_degree_of_studies |no                |int             |id of the last degree of studies.               |6                                           |MASTER DEGREE                                                                                                                                                                                                       |The id should exists as a valid degree of studies in range between [1,7].  Verify the degrees_of_studies catalog.|
|contest_id             |no                |int             |id of the associated contest.                   |301                                         |301                                                                                                                                                                                                                 |The id should exists on contest table.                                                                           |
|other_names            |no                |array of object |Other names for the person.                     |Info available on other-name endpoint       |{<br/>&emsp;"ballot_name": [],<br/>&emsp;"nickname": [<br/>&emsp;&emsp;{<br/>&emsp;&emsp;&emsp;"en_US": "Dr Aguilar"<br/>&emsp;&emsp;},<br/>&emsp;&emsp;{<br/>&emsp;&emsp;&emsp;"es_MX": "Dr Aguilar"<br/>&emsp;&emsp;}<br/>&emsp;],<br/>&emsp;"preferred_name": []<br/>}|Valid keys are ["preferred", "nickname", "ballot_name"]  The output is on en_US and es_MX locales. |
|professions            |no                |array of string |Related professions for the person.             |Info available on person-profession endpoint|[<br/>&emsp;"Law",<br/>&emsp;"Public administration",<br/>&emsp;"Educational planning and evaluation"<br/>]                                                                                                         |-                                                                                                               |
|fb_urls                |no                |array of object |A list of FB urls belong to this person.        |Info available on url endpoint              |[<br/>&emsp;{<br/>&emsp;&emsp;"note": "campaign",<br/>&emsp;&emsp;"url": "https://www.facebook.com/facebook/"<br/>&emsp;} <br/>]                                                                                    |Valid note values are ["campaign", "official", "personal"]  Valid URL format.                                   |
|ig_urls                |no                |array of object |A list of IG urls belong to this person.        |Info available on url endpoint              |[<br/>&emsp;{<br/>&emsp;&emsp;"note": "campaign",<br/>&emsp;&emsp;"url": "https://www.instagram.com/instagram/"<br/>&emsp;} <br/> ]                                                                                 |Valid note values are ["campaign", "official", "personal"]  Valid URL format.                                   |
|social_network_accounts|no                |array of object |Other non-FB social media accounts.             |Info available on url endpoint              |[<br/>&emsp;{<br/>&emsp;&emsp;"type": "Twitter",<br/>&emsp;&emsp;"value": "exampletwitter"<br/>&emsp;},<br/>&emsp;{<br/>&emsp;&emsp;"type": "YouTube",<br/>&emsp;&emsp;"value": "exampleyoutube"<br/>&emsp;&emsp;}<br/>] |Valid type values are ["Twitter", "YouTube", "LinkedIn", "Flickr", "Pinterest", "Tumblr", "RSS"]            |
|websites               |no                |array of object |Official/Campaign websites of the person.       |Info available on url endpoint              |[<br/>&emsp;{<br/>&emsp;&emsp;"note": "official",<br/>&emsp;&emsp;"url": "https://www.official.com"<br/>&emsp;},<br/>&emsp;{<br/>&emsp;&emsp;"note": "campaign",<br/>&emsp;&emsp;"url": "https://www.campaign.com"<br/>&emsp;}<br/>] |Valid note values are ["campaign", "personal", "wikipedia"]  Valid URL format.                  |
|photo_urls             |no                |array of strings|URLs to person photos.                          |Info available on url endpoint              |[<br/>&emsp;"https://www.example.com/pub/photos/p1.jpg",<br/>&emsp;"https://www.example.com/pub/photos/p2.png" ]                                                                                                    |Valid URL format.                                                                                                |

####    membership

---

####    contest

---

####    party

---

####    coalition  

---

####    chamber

---

####    role

---

####    area

---

####    other-name

---

####    profession

---

####    person-profession

---

####    url

##  Running app

### Components

- `python3`
- `pip3`
- `virtualenv`
- `flask`


### Setup environment

This development was made on Debian/Ubuntu GNU/Linux based distro. Please verify any command for your distro before
execute it.

####    Setting up `virtualenv` and `python3`

```bash
# Create a virtual environment.
virtualenv venv -p /usr/bin/python3

# Activate virtual environment
source ./venv/bin/activate

# To deactivate the virtual environment
deactivate
```

####    Installing dependencies

```bash
pip install -r ./requirements.txt
```

####    Running

```bash
# Running app
python ./application.py
```
