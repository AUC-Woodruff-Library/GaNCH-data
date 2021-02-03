# Addressing Challenges

## Hierarchy in queries

The property *located in the administrative territorial entity (P131)* is designed to be hierarchical and transitive (meaning that you should be able to only list the most local territory (such as municipality) and other territories (county, state) should "cascade up".
This creates a challenge when searching with searches timing out, so an alternative is addressed in this conversation. 

* [Property talk:P131/Inheritance/Hierarchy not working during queries?](https://www.wikidata.org/wiki/Property_talk:P131#Inheritance/Hierarchy_not_working_during_queries?)

## Municipalities and Counties

Many municipalities in Georgia exist in more than one county (for example, Atlanta is in both DeKalb and Fulton counties). The below conversations are an attempt to address this wihtin the *located in the administrative territorial entity (P131)*, since there has been no way to ensure that NCHs are showing up in the correct county if only the most local territory is specified.

* [Property talk:P131/Best practice for representing cities/towns in multiple counties?](https://www.wikidata.org/wiki/Property_talk:P131#Best_practice_for_representing_cities/towns_in_multiple_counties?)
* [Wikidata:Property proposal/hierarchy switch](https://www.wikidata.org/wiki/Wikidata:Property_proposal/hierarchy_switch)
* [Wikidata:Project chat/located in the administrative territorial entity (P131) isn't *really* transitive...](https://www.wikidata.org/wiki/Wikidata:Project_chat/Archive/2020/02#located_in_the_administrative_territorial_entity_(P131)_isn't_really_transitive...)
* [Property talk:P131/Possible change of usage](https://www.wikidata.org/wiki/Property_talk:P131#Possible_change_of_usage)

Unfortunately, even after several proposals and over a month of discussion on those four separate Wikidata pages, no consensus was reached.  So for our project we explicitly declare municipality, county, AND state, all in the P131 field, with the hopes that consensus on a solution can be reached in the future.  In the meantime, our queries are functioning well, and we figure it’s better to have too much well-sourced information rather than too little.

## Query construction

We got a lot of help from the Wikidata community in constructing our queries.  In particular, a big shout out to [User:Dipsacus fullonum](https://www.wikidata.org/wiki/User:Dipsacus_fullonum) for all their help!

* [List of public library branches in Georgia](https://www.wikidata.org/wiki/Wikidata:Request_a_query/Archive/2020/05#Public_library_branches_in_Georgia)
* [Line graph of visitors per year for all GPLS library sytems](https://www.wikidata.org/wiki/Wikidata:Request_a_query/Archive/2020/05#Line_graph_of_visitors_per_year_for_all_GPLS_library_sytems)
* [Query timing out with a long VALUES list](https://www.wikidata.org/wiki/Wikidata:Request_a_query/Archive/2020/05#Query_timing_out_with_a_long_VALUES_list)
* [Combining multiple "any subclass of" "instance of"s into a single search?](https://www.wikidata.org/wiki/Wikidata:Request_a_query/Archive/2020/06#Combining_multiple_%22any_subclass_of%22_%22instance_of%22s_into_a_single_search?)

## Sensitive data doesn't fit into Wikidata

During our focus group discussion with heritage emergency response coordinators, the question was raised whether we could record some additional types of data in Wikidata.  These included:
* Personal cell phone numbers for NCH organizations' leadership (preferably four numbers per organization)
* Floor maps of buildings
* Listings of hazardous materials that could be found on site

Each of these types of data could be considered sensitive and therefore inappropriate to include in Wikidata, but appropriate for the state's Emergency Operations Command during a disaster.  Rather than trying to "shoehorn" this data into the project, we strongly encourage NCH organizations in Georgia to reach out to emergency responder leaders in their area to provide this information directly.
