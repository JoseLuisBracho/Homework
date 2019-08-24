drop table movies;
create table movies (
"ID" int primary key,
"Film" text,
"Year" int,
"Director" text,
"Gross" text,
"Budget" text,
"IMDb_score" text
);

drop table oscars;
create table oscars (
"ID" int primary key,
"Film" text,
"Year" int,
"Award" text,
"Name" text
);

select * from movies
order by "Year";

select * from oscars;

SELECT mv."Year", mv."Film", mv."Director", mv."Gross", mv."Budget", mv."IMDb_score", os."Award", os."Name"
FROM movies mv
INNER JOIN oscars os
ON trim(mv."Film", ' ') = trim(os."Film")
order by mv."Year";
