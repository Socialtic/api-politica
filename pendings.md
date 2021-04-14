---
-   Table:		Area
-   Column:		parent_id
-   Pending:	Change to FK
---
-   Table:		Membership
-   Column:		parent_membership_id
-   Pending:	Change to FK
---
-   Table:		Membership
-   Column:		coalition_id
-   Pending:	Change to FK
---
-   Table:		Party
-   Column:		coalition_id
-   Pending:	Change to FK
---
-   Table:		Contest
-   Column:		membership_id_winner
-   Pending:	Change to FK
---
-   Table:		Role
-   Column:		contest_id
-   Pending:	Change to FK
---
-   Table:		Other_Names
-   Column:		person_id
-   Pending:	Change to FK
---
-   Table:		Person_Professions
-   Column:		person_id
-   Pending:	Change to FK
---
-   Table:		Person
-   Column:		contest_id
-   Pending:	Change to FK
---
-   Table:		Membership
-   Column:		contest_id
-   Pending:	Change to FK
---

export
---
area
chamber
role
person
party
membership
contest
---

-   Table:  membership
-   Column: party_id
-   Pending:    IDs from coalition parties?