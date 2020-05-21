# SPARQL Queries for GEMA Regions

These are SPARQL queries run on https://query.wikidata.org/ to show all cultural heritage organizations within [GEMA/HS Field and Homeland Security Regions](https://gema.georgia.gov/locations/regional-field-offices)

## GEMA Region 1

    #GEMA Region 1
    SELECT DISTINCT ?organization ?organizationLabel ?street_address ?coordinate_location ?phone_number ?e_mail_address ?county
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?county)
    {
        (wd:Q491547 "Union County") (wd:Q503538 "Towns County") (wd:Q503546 "Rabun County")
        (wd:Q492040 "Lumpkin County") (wd:Q389365 "White County") (wd:Q501096 "Habersham County")
        (wd:Q498362 "Stephens County") (wd:Q492012 "Hall County") (wd:Q488201 "Banks County")
        (wd:Q385931 "Franklin County") (wd:Q491301 "Hart County") (wd:Q486838 "Barrow County")
        (wd:Q486137 "Jackson County") (wd:Q156387 "Madison County") (wd:Q492016 "Elbert County")
        (wd:Q498312 "Walton County") (wd:Q492026 "Oconee County") (wd:Q112061 "Clarke County")
        (wd:Q491525 "Oglethorpe County") (wd:Q491759 "Wilkes County") (wd:Q491519 "Lincoln County")
        (wd:Q501101 "Newton County") (wd:Q493083 "Morgan County") (wd:Q486765 "Greene County")
    }
    FILTER NOT EXISTS { ?organization wdt:P576 [] }
    ?organization (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?organization wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?organization wdt:P6375 ?street_address. }
    OPTIONAL { ?organization wdt:P625 ?coordinate_location. }
    OPTIONAL { ?organization wdt:P1329 ?phone_number. }
    OPTIONAL { ?organization wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?organization
    LIMIT 10000

## GEMA Region 2

    #GEMA Region 2
    SELECT DISTINCT ?organization ?organizationLabel ?street_address ?coordinate_location ?phone_number ?e_mail_address ?county
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?county)
    {
        (wd:Q498684 "Quitman County") (wd:Q498307 "Randolph County") (wd:Q503492 "Terrell County")
        (wd:Q491508 "Lee County") (wd:Q156486 "Crisp County") (wd:Q156580 "Clay County")
        (wd:Q156632 "Calhoun County") (wd:Q176480 "Dougherty County") (wd:Q486154 "Worth County")
        (wd:Q498336 "Turner County") (wd:Q498346 "Tift County") (wd:Q486757 "Early County")
        (wd:Q493107 "Miller County") (wd:Q376990 "Baker County") (wd:Q493102 "Mitchell County")
        (wd:Q113005 "Colquitt County") (wd:Q156431 "Cook County") (wd:Q498372 "Seminole County")
        (wd:Q493037 "Decatur County") (wd:Q492061 "Grady County") (wd:Q498327 "Thomas County")
        (wd:Q488175 "Brooks County") (wd:Q493134 "Lowndes County")
    }
    FILTER NOT EXISTS { ?organization wdt:P576 [] }
    ?organization (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?organization wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?organization wdt:P6375 ?street_address. }
    OPTIONAL { ?organization wdt:P625 ?coordinate_location. }
    OPTIONAL { ?organization wdt:P1329 ?phone_number. }
    OPTIONAL { ?organization wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?organization
    LIMIT 10000

## GEMA Region 3

    #GEMA Region 3
    SELECT DISTINCT ?organization ?organizationLabel ?street_address ?coordinate_location ?phone_number ?e_mail_address ?county
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?county)
    {
        (wd:Q134080 "Taliaferro County") (wd:Q224910 "Jasper County") (wd:Q498341 "Putnam County")
        (wd:Q493112 "Hancock County") (wd:Q491529 "Warren County") (wd:Q492066 "McDuffie County")
        (wd:Q115307 "Columbia County") (wd:Q488206 "Baldwin County") (wd:Q477951 "Glascock County")
        (wd:Q498319 "Richmond County") (wd:Q503551 "Twiggs County") (wd:Q486317 "Wilkinson County")
        (wd:Q498286 "Washington County") (wd:Q486386 "Jefferson County") (wd:Q211360 "Burke County")
        (wd:Q491556 "Laurens County") (wd:Q163529 "Johnson County") (wd:Q503071 "Treutlen County")
        (wd:Q111894 "Emanuel County") (wd:Q389551 "Jenkins County") (wd:Q503511 "Screven County")
        (wd:Q488224 "Candler County") (wd:Q488166 "Bulloch County") (wd:Q493044 "Evans County")
    }
    FILTER NOT EXISTS { ?organization wdt:P576 [] }
    ?organization (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?organization wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?organization wdt:P6375 ?street_address. }
    OPTIONAL { ?organization wdt:P625 ?coordinate_location. }
    OPTIONAL { ?organization wdt:P1329 ?phone_number. }
    OPTIONAL { ?organization wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?organization
    LIMIT 10000

## GEMA Region 4

    #GEMA Region 4
    SELECT DISTINCT ?organization ?organizationLabel ?street_address ?coordinate_location ?phone_number ?e_mail_address ?county
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?county)
    {
        (wd:Q503486 "Spalding County") (wd:Q488210 "Butts County") (wd:Q498295 "Troup County")
        (wd:Q501151 "Meriwether County") (wd:Q491533 "Pike County") (wd:Q493049 "Lamar County")
        (wd:Q493024 "Monroe County") (wd:Q493040 "Jones County") (wd:Q486133 "Harris County")
        (wd:Q498356 "Talbot County") (wd:Q498377 "Upson County") (wd:Q486401 "Crawford County")
        (wd:Q488171 "Bibb County") (wd:Q492048 "Muscogee County") (wd:Q486394 "Chattahoochee County")
        (wd:Q486344 "Marion County") (wd:Q505299 "Taylor County") (wd:Q387216 "Schley County")
        (wd:Q492021 "Macon County") (wd:Q491553 "Peach County") (wd:Q486362 "Houston County")
        (wd:Q491543 "Stewart County") (wd:Q491514 "Webster County") (wd:Q503076 "Sumter County")
        (wd:Q492036 "Dooly County")
    }
    FILTER NOT EXISTS { ?organization wdt:P576 [] }
    ?organization (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?organization wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?organization wdt:P6375 ?street_address. }
    OPTIONAL { ?organization wdt:P625 ?coordinate_location. }
    OPTIONAL { ?organization wdt:P1329 ?phone_number. }
    OPTIONAL { ?organization wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?organization
    LIMIT 10000

## GEMA Region 5

    #GEMA Region 5
    SELECT DISTINCT ?organization ?organizationLabel ?street_address ?coordinate_location ?phone_number ?e_mail_address ?county
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?county)
    {
        (wd:Q156637 "Effingham County") (wd:Q384890 "Chatham County") (wd:Q486848 "Bryan County")
        (wd:Q487692 "Liberty County") (wd:Q493033 "Long County") (wd:Q492652 "McIntosh County")
        (wd:Q491762 "Wayne County") (wd:Q487016 "Glynn County") (wd:Q486800 "Pierce County") 
        (wd:Q156650 "Brantley County") (wd:Q486659 "Charlton County") (wd:Q110504 "Camden County")
    }
    FILTER NOT EXISTS { ?organization wdt:P576 [] }
    ?organization (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?organization wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?organization wdt:P6375 ?street_address. }
    OPTIONAL { ?organization wdt:P625 ?coordinate_location. }
    OPTIONAL { ?organization wdt:P1329 ?phone_number. }
    OPTIONAL { ?organization wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?organization
    LIMIT 10000

## GEMA Region 6

    #GEMA Region 5
    SELECT DISTINCT ?organization ?organizationLabel ?street_address ?coordinate_location ?phone_number ?e_mail_address ?county
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?county)
    {
        (wd:Q486654 "Dade County") (wd:Q498321 "Walker County") (wd:Q260871 "Catoosa County")
        (wd:Q491537 "Whitfield County") (wd:Q493074 "Murray County") (wd:Q493054 "Gilmer County")
        (wd:Q493079 "Fannin County") (wd:Q486179 "Chattooga County") (wd:Q200696 "Gordon County") 
        (wd:Q498675 "Pickens County") (wd:Q492032 "Dawson County") (wd:Q486389 "Floyd County")
        (wd:Q488181 "Bartow County") (wd:Q486664 "Cherokee County") (wd:Q493092 "Forsyth County")
        (wd:Q498395 "Polk County") (wd:Q501140 "Paulding County") (wd:Q544539 "Haralson County")
        (wd:Q493088 "Carroll County") (wd:Q486348 "Heard County") (wd:Q111928 "Coweta County") 
    }
    FILTER NOT EXISTS { ?organization wdt:P576 [] }
    ?organization (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?organization wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?organization wdt:P6375 ?street_address. }
    OPTIONAL { ?organization wdt:P625 ?coordinate_location. }
    OPTIONAL { ?organization wdt:P1329 ?phone_number. }
    OPTIONAL { ?organization wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?organization
    LIMIT 10000