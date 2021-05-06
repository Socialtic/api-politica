#	Valores "nulos"

-	int: -1
-	date: '0001-01-01'

#	Tablas

```
Area{
	district_type	integer
	parent_area_id	integer
}

Chamber{
	area_id	integer
}

Role{
	role	integer
	area_id	integer
	chamber_id	integer
	contest_id	integer
}

Party{
	area_id	integer
	coalition_id	integer
}

Person{
	date_birth	date
	gender	integer
	last_degree_of_studies	integer
	contest_id	integer
}

Other-Name{
	other_name_type	integer
	person_id	integer
}

Person-Profession{
	person_id	integer
	profession_id	integer
}

Membership{
	person_id	integer
	role_id	integer
	party_id	integer
	coalition_id	integer
	contest_id	integer
	membership_type	integer
	start_date	date
	end_date	date
	parent_membership_id	integer
	date_changed_from_substitute	date
}

Contest{
	area_id	integer
	membership_id_winner	integer
	start_date	date
	end_date	date
}

URL{
	url_type	integer
	owner_type	integer
	owner_id	integer
}
```