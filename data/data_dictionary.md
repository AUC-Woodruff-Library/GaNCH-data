## Data dictionary for the GaNCH project

This data dictionary defines the metadata that will be recorded for organizations.  

Some fields are repeatable, such as "Instance of", where an organization can be both a museum and an archives at the same time.

Some fields are mapped to the same Wikidata property, such as "City", "County", and "State", all of which map to "located in the administrative territorial entity".

| Metadata Field | Description and Constraints | Requirement |
| --- | --- | --- |
| Code | Internal 4 digit index code for organizations (to help de-dupe across data sources) | N/A | REQUIRED |
| [organization_label (en)](https://www.wikidata.org/wiki/Wikidata:Introduction#How_does_Wikidata_work?)	| The organization's name, language must be defined | REQUIRED |
|description (en)	| brief description of the organization to help disambiguate, language must be defined | REQUIRED |
|alias (en)	| other names/spellings of the organization, language must be defined | optional |
|[instance of (P31)](https://www.wikidata.org/wiki/Property:P31)| that class of which this subject is a particular example and member (subject typically an individual member with a proper name label) (i.e., library, archives, museum, gallery, etc.) | REQUIRED |
|[located at street address (P6375)](https://www.wikidata.org/wiki/Property:P6375)| full street address where subject is located. include building number through to post code. use also P669 if the street is known as a separate element | REQUIRED |
|[city (P131)](https://www.wikidata.org/wiki/Property:P131)	| the item is located on the territory of the following administrative entity | REQUIRED |
|[county (P131)](https://www.wikidata.org/wiki/Property:P131)	|the item is located on the territory of the following administrative entity | REQUIRED |
|[state (P131)](https://www.wikidata.org/wiki/Property:P131)	| the item is located on the territory of the following administrative entity | REQUIRED |
|[country (P17)](https://www.wikidata.org/wiki/Property:P17)	| soverign state of the item | REQUIRED |
|[coordinate location (P625)](https://www.wikidata.org/wiki/Property:P625) | geocoordinates of the subject. For Earth, please note that only WGS84 coordinating system is supported at the moment | REQUIRED |
|[phone number (P1329)](https://www.wikidata.org/wiki/Property:P1329)	| telephone number in standard format (RFC3966), without 'tel:' prefix | Recommended |
|[email address (P968)](https://www.wikidata.org/wiki/Property:P968)	| e-mail address of the organisation. Format: prefixed with mailto: | Recommended|
|[official website (P856)](https://www.wikidata.org/wiki/Property:P856)	| URL of the official homepage of an item (current or former) [if the homepage changes, add an additional statement with preferred rank. Do not remove the former URL] | Recommneded |
|[inception (P571)](https://www.wikidata.org/wiki/Property:P571)	| date or point in time when the subject came into existence as defined | optional |
|[dissolved, abolished or demolished (P576)](https://www.wikidata.org/wiki/Property:P576)| date or point in time at which the subject ceased to exist as defined (use P730 for a building, see also discontinued date (P2669))| optional |
|[parent organization (P749)](https://www.wikidata.org/wiki/Property:P749) | parent organization of an organization, opposite of subsidiaries (P355) | optional |
|[subsidiaries (P355)](https://www.wikidata.org/wiki/Property:P355) | subsidiary of a company or organization, opposite of parent organization (P749) | optional |

### Examples
* [McCain Library Special Collections](https://www.wikidata.org/wiki/Q56232938)
* [Acworth Society for Historic Preservation](https://www.wikidata.org/wiki/Q56232937)
