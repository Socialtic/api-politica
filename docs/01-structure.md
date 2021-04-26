#  General structure

The API has endpoints with different methods enabled.

**For clients**, the `get` method is available.

**For developers**, the `get` and `post` methods are available on any endpoint.
And for any instance or entity on the endpoints the `get`, `put` and `delete` methods are available.

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