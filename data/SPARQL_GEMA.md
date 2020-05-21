#SPARQL Queries for GEMA Regions

##GEMA Region 1

    #GEMA Region 1
    SELECT DISTINCT ?library ?libraryLabel ?located_at_street_address ?coordinate_location ?phone_number ?e_mail_address ?countyLabel
    WHERE {
    VALUES (?located_in_the_administrative_territorial_entity ?countyLabel)
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
    FILTER NOT EXISTS { ?library wdt:P576 [] }
    ?library (wdt:P31/(wdt:P279*)) wd:Q5193377.
    ?library wdt:P131 ?located_in_the_administrative_territorial_entity. hint:Prior hint:runFirst true.
    OPTIONAL { ?library wdt:P6375 ?located_at_street_address. }
    OPTIONAL { ?library wdt:P625 ?coordinate_location. }
    OPTIONAL { ?library wdt:P1329 ?phone_number. }
    OPTIONAL { ?library wdt:P968 ?e_mail_address. }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY ?library
    LIMIT 10000