
/* Pull up the 2022.csv under /data/clean/team_vs_team and type verbatum 
the column names followed by (varchar) NOT NULL,
Ive done a few. The stuff underneath is his code from homework 9. It is formatted
how we need to format ours if you want an example. When 
*/

CREATE TABLE team_vs_team (
    Team (varchar) CONSTRAINT Team_key PRIMARY KEY,
    ATL (varchar) NOT NULL,
    BOS (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    CHI (varchar) NOT NULL,
    CHO (varchar) NOT NULL,
    CLE (varchar) NOT NULL,
    DAL (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    BRK (varchar) NOT NULL,
    
);

CREATE TABLE fscskey2014 ()
    stabr varchar(2) NOT NULL,
    fscskey varchar(6) CONSTRAINT fscskey2014_key PRIMARY KEY,
    libid varchar(20) NOT NULL,
    libname varchar(100) NOT NULL,
    obereg varchar(2) NOT NULL,
    rstatus integer NOT NULL,
    statstru varchar(2) NOT NULL,
    statname varchar(2) NOT NULL,
    stataddr varchar(2) NOT NULL,
    longitud numeric(10,7) NOT NULL,
    latitude numeric(10,7) NOT NULL,
    fipsst varchar(2) NOT NULL,
    fipsco varchar(3) NOT NULL,
    address varchar(35) NOT NULL,
    city varchar(20) NOT NULL,
    zip varchar(5) NOT NULL,
    zip4 varchar(4) NOT NULL,
    cnty varchar(20) NOT NULL,
    phone varchar(10) NOT NULL,
    c_relatn varchar(2) NOT NULL,
    c_legbas varchar(2) NOT NULL,
    c_admin varchar(2) NOT NULL,
    geocode varchar(3) NOT NULL,
    lsabound varchar(1) NOT NULL,
    startdat varchar(10),
    enddate varchar(10),
    popu_lsa integer NOT NULL,
    centlib integer NOT NULL,
    branlib integer NOT NULL,
    bkmob integer NOT NULL,
    master numeric(8,2) NOT NULL,
    libraria numeric(8,2) NOT NULL,
    totstaff numeric(8,2) NOT NULL,
    locgvt integer NOT NULL,
    stgvt integer NOT NULL,
    fedgvt integer NOT NULL,
    totincm integer NOT NULL,
    salaries integer,
    benefit integer,
    staffexp integer,
    prmatexp integer NOT NULL,
    elmatexp integer NOT NULL,
    totexpco integer NOT NULL,
    totopexp integer NOT NULL,
    lcap_rev integer NOT NULL,
    scap_rev integer NOT NULL,
    fcap_rev integer NOT NULL,
    cap_rev integer NOT NULL,
    capital integer NOT NULL,
    bkvol integer NOT NULL,
    ebook integer NOT NULL,
    audio_ph integer NOT NULL,
    audio_dl float NOT NULL,
    video_ph integer NOT NULL,
    video_dl float NOT NULL,
    databases integer NOT NULL,
    subscrip integer NOT NULL,
    hrs_open integer NOT NULL,
    visits integer NOT NULL,
    referenc integer NOT NULL,
    regbor integer NOT NULL,
    totcir integer NOT NULL,
    kidcircl integer NOT NULL,
    elmatcir integer NOT NULL,
    loanto integer NOT NULL,
    loanfm integer NOT NULL,
    totpro integer NOT NULL,
    totatten integer NOT NULL,
    gpterms integer NOT NULL,
    pitusr integer NOT NULL,
    wifisess integer NOT NULL,
    yr_sub integer NOT NULL
);
