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

##### URL

[https://www.apielectoral.mx/person/< id >](https://www.apielectoral.mx/person)

##### Fields

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

##### Output

[https://www.apielectoral.mx/person/1](https://www.apielectoral.mx/person/1)

```json
{
  "person": {
    "contest_id": 301,
    "date_birth": "1985-09-19",
    "dead_or_alive": true,
    "fb_urls": [
      {
        "note": "campaign",
        "url": "https://www.facebook.com/MarinadelpilarBc"
      }
    ],
    "first_name": {
      "en_US": "Marina del Pilar",
      "es_MX": "Marina del Pilar"
    },
    "full_name": {
      "en_US": "Marina del Pilar Ávila Olmeda",
      "es_MX": "Marina del Pilar Ávila Olmeda"
    },
    "gender": "F",
    "id": 1,
    "ig_urls": [
      {
        "note": "campaign",
        "url": "https://www.instagram.com/marinadelpilar_ao"
      }
    ],
    "last_degree_of_studies": "MASTER DEGREE",
    "last_name": {
      "en_US": "Ávila Olmeda",
      "es_MX": "Ávila Olmeda"
    },
    "other_names": {
      "ballot_name": [],
      "nickname": [],
      "preferred_name": []
    },
    "photo_urls": [],
    "professions": [
      "Law",
      "Public administration",
      "Educational planning and evaluation"
    ],
    "social_network_accounts": [],
    "websites": [
      {
        "note": "official",
        "url": "https://www.marinadelpilar.mx"
      }
    ]
  },
  "success": true
}
```
####    membership

##### URL

[https://www.apielectoral.mx/membership/< id >](https://www.apielectoral.mx/membership)

##### Fields

|field_name                  |require for input?|type            |description                                                                                  |input value example           |output value example                                                            |notes                                                                                                                                                            |
|----------------------------|------------------|----------------|---------------------------------------------------------------------------------------------|------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|membership_id               |no                |int             |Unique identifier                                                                            |1                             |1                                                                               |On query the name of the field is id                                                                                                                             |
|role_id                     |yes               |int             |The id of the role that the member fulfills in the organization                              |1                             |1                                                                               |id should exist on role endpoint.                                                                                                                                |
|person_id                   |yes               |int             |The id of the person that this membership is associated with                                 |1                             |1                                                                               |id should exist on person endpoint.                                                                                                                              |
|party_id                    |yes               |int             |The id of the party that this is associated with                                             |39                            |39                                                                              |id should exist on party endpoint.                                                                                                                               |
|coalition_id                |no                |int             |The id of the coalition that this is associated with                                         |7                             |7                                                                               |id should exist on coalition endpoint.                                                                                                                           |
|contest_id                  |no                |int             |If this membership is for a contest, specify the contest id here.                            |301                           |301                                                                             |id should exists on contest endpoint.                                                                                                                            |
|goes_for_coalition          |yes               |boolean         |True if the membership represents a coalition contest.                                       |true                          |true                                                                       |-                                                                                                                                                                |
|membership_type             |yes               |int             |The type of relationship between the office and the figure.                                  |2                             |campaigning_politician                                                          |On input, the id should exists as a valid type in range between [1,3].<br/>On ouput, the valid values are ['officeholder', 'campaigning_politician', 'party_leader']|
|goes_for_reelection         |yes               |boolean         |True if the memberships goes for a reelection contest.                                       |false                         |false                                                                           |-                                                                                                                                                                |
|start_date                  |no                |date            |Start date of the membership.                                                                |2021-04-04                    |2021-04-04                                                                      |Date format is YYYY-MM-DD                                                                                                                                        |
|end_date                    |no                |date            |End date of the membership.                                                                  |2021-06-02                    |2021-06-02                                                                      |Date format is YYYY-MM-DD                                                                                                                                        |
|is_substitute               |yes               |boolean         |True if membership is for substitute candidate. False if membership is for primary candidate.|false                         |false                                                                           |-                                                                                                                                                                |
|parent_membership_id        |no                |int             |id of the membership associated to the candidate for whom is substitute.                     |                              |                                                                                |id should exist on membership endpoint.                                                                                                                          |
|changed_from_substitute     |no                |boolean         |True if membership changed from substitute to primary.                                       |false                         |false                                                                           |-                                                                                                                                                                |
|date_changed_from_substitute|no                |date            |Date when the substitute changed from substitute to primary.                                 |                              |                                                                                |Date format is YYYY-MM-DD                                                                                                                                        |
|source_urls                 |no                |array of strings|Source of truth.                                                                             |Info available on url endpoint|[<br/>&emsp;"https://www.example.com/pub/1",<br/>&emsp;"https://www.example.com/pub/2" ]|Valid URL format.                                                                                                                                                |


##### Output example

[https://www.apielectoral.mx/membership/1](https://www.apielectoral.mx/membership/1)

```json
{
  "membership": {
    "changed_from_substitute": false,
    "coalition_id": 7,
    "contest_id": 301,
    "date_changed_from_substitute": "",
    "end_date": "2021-06-02",
    "goes_for_coalition": true,
    "goes_for_reelection": false,
    "id": 1,
    "is_substitute": false,
    "membership_type": "campaigning_politician",
    "parent_membership_id": "",
    "party_ids": [
      39
    ],
    "person_id": 1,
    "role_id": 1,
    "source_urls": [],
    "start_date": "2021-04-04"
  },
  "success": true
}

```

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
