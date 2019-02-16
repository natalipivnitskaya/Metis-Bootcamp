DROP TABLE public.fact;
DROP TABLE public.data;
DROP TABLE public.event_type;
DROP TABLE public.equipment;

CREATE TABLE public.equipment (
    tac varchar PRIMARY KEY,
    vendor varchar NOT NULL,
    platform varchar NOT NULL,
    type varchar NOT NULL
);

COPY public.equipment(tac,vendor,platform,type) 
FROM '/Users/natali/Code/Metis/Metis-Bootcamp/projects/03-mcnulty/Archive/equipment.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE public.event_type (
    id integer PRIMARY KEY,
    lable varchar NOT NULL,
    description text NOT NULL
);

COPY public.event_type(id,lable,description) 
FROM '/Users/natali/Code/Metis/Metis-Bootcamp/projects/03-mcnulty/Archive/event_type.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE public.data (
    id serial PRIMARY KEY,
    lac varchar NOT NULL,
    cid varchar NOT NULL,
    msisdn varchar NOT NULL,
    imei varchar NULL,
    event_type integer NOT NULL references event_type(id),
    tstamp bigint NOT NULL,
    long decimal NOT NULL,
    lat decimal NOT NULL,
    max_dist integer NOT NULL,
    cell_type varchar NOT NULL,
    start_angle decimal NOT NULL,
    end_angle decimal NOT NULL
);

COPY public.data(lac,cid,msisdn,imei,event_type,tstamp,long,lat,max_dist,cell_type,start_angle,end_angle) 
FROM '/Users/natali/Code/Metis/Metis-Bootcamp/projects/03-mcnulty/Archive/data.csv' DELIMITER ';' CSV HEADER;

CREATE TABLE public.fact (
    first varchar NOT NULL,
    second varchar NOT NULL,
    PRIMARY KEY (first, second)
);

COPY public.fact(first,second) 
FROM '/Users/natali/Code/Metis/Metis-Bootcamp/projects/03-mcnulty/Archive/facts.csv' DELIMITER ',' CSV HEADER;
