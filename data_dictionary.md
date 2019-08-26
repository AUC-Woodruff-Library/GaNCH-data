## Data dictionary for the GaNCH project

This data dictionary defines the metadata that will be recorded for organizations.  

Some fields are repeatable, such as "Instance of", where an organization can be both a museum and an archives at the same time.

Some fields are mapped to the same Wikidata property, such as "City", "County", and "State", all of which map to "located in the administrative territorial entity".

* [Label (Organization)](https://www.wikidata.org/wiki/Wikidata:Introduction#How_does_Wikidata_work?) - REQUIRED: the organization's name
* [Instance of](https://www.wikidata.org/wiki/Property:P31) - REQUIRED: that class of which this subject is a particular example and member (subject typically an individual member with a proper name label) (i.e., library, archives, museum, gallery, etc.)
* [Parent organization](https://www.wikidata.org/wiki/Property:P749) - OPTIONAL: parent organization of an organization, opposite of subsidiaries (P355)
* [Address (located at street address)](https://www.wikidata.org/wiki/Property:P6375) - REQUIRED: full street address where subject is located. include building number through to post code. use also P669 if the street is known as a separate element
* [City (located in the administrative territorial entity)](https://www.wikidata.org/wiki/Property:P131) - REQUIRED: the item is located on the territory of the following administrative entity
* [State (located in the administrative territorial entity)](https://www.wikidata.org/wiki/Property:P131) - REQUIRED: the item is located on the territory of the following administrative entity
* [Country](https://www.wikidata.org/wiki/Property:P17) - REQUIRED: Soverign state of the item 
* [PostCode (postal code)](https://www.wikidata.org/wiki/Property:P281) - REQUIRED: identifier assigned by postal authorities for the subject area or building
* [County (located in the administrative territorial entity)](https://www.wikidata.org/wiki/Property:P131) - REQUIRED: the item is located on the territory of the following administrative entity
* [Coordinates (coordinate location)](https://www.wikidata.org/wiki/Property:P625) - REQUIRED: geocoordinates of the subject. For Earth, please note that only WGS84 coordinating system is supported at the moment 
* [Founded (inception)](https://www.wikidata.org/wiki/Property:P571) - RECOMMENDED: date or point in time when the subject came into existence as defined
* [Phone number](https://www.wikidata.org/wiki/Property:P1329) - REQUIRED: telephone number in standard format (RFC3966), without 'tel:' prefix
* [E-mail address](https://www.wikidata.org/wiki/Property:P968) - RECOMMENDED: e-mail address of the organisation. Format: prefixed with mailto:
* [Official website](https://www.wikidata.org/wiki/Property:P856) - RECOMMENDED: URL of the official homepage of an item (current or former) [if the homepage changes, add an additional statement with preferred rank. Do not remove the former URL]

### Examples
* [McCain Library Special Collections](https://www.wikidata.org/wiki/Q56232938)
* [Acworth Society for Historic Preservation](https://www.wikidata.org/wiki/Q56232937)
