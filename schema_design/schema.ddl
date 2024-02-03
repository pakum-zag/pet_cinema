
CREATE SCHEMA IF NOT EXISTS content;


CREATE TABLE content.film_work (
    id uuid NOT NULL PRIMARY KEY,
    title text NOT NULL,
    description text,
    creation_date date,
    rating double precision,
    type text NOT NULL,
    file_path text NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid NOT NULL PRIMARY KEY,
    name character varying(100) NOT NULL,
    description text,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid NOT NULL PRIMARY KEY,
    genre_id uuid NOT NULL,
    film_work_id uuid NOT NULL,
    created timestamp with time zone,

    FOREIGN KEY (genre_id) REFERENCES content.genre(id),
    FOREIGN KEY (film_work_id) REFERENCES content.film_work(id)
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid NOT NULL PRIMARY KEY,
    full_name character varying(255) NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid NOT NULL PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role character varying(100) NOT NULL,
    created timestamp with time zone,

    FOREIGN KEY (person_id) REFERENCES content.person(id),
    FOREIGN KEY (film_work_id) REFERENCES content.film_work(id)
);


CREATE INDEX IF NOT EXISTS film_work_creation_date_idx ON content.film_work(creation_date);

CREATE UNIQUE INDEX IF NOT EXISTS film_work_person_idx ON content.person_film_work (film_work_id, person_id, role);
CREATE UNIQUE INDEX IF NOT EXISTS genre_film_work_idx ON content.genre_film_work (genre_id, film_work_id);