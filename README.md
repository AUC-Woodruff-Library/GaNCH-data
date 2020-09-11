# GaNCH

GaNCH: Using Linked Open Data for **G**eorgi**a**'s **N**atural, **C**ultural, and **H**istoric Organizations' Disaster Response.

**https://ganch.auctr.edu**

The [Atlanta University Center Robert W. Woodruff Library](https://www.auctr.edu/) would like to gratefully acknolwedge [LYRASIS](https://www.lyrasis.org/Pages/Main.aspx) for their support of this project via a [2019 LYRASIS Catalyst Fund grant](https://lyrasisnow.org/press-release-lyrasis-announces-the-2019-catalyst-fund-recipients-and-their-projects/)

This one-year project will create a publicly editable directory of Georgia’s Natural, Cultural and Historical Organizations (NCHs), allowing for quick retrieval of location and contact information for disaster response. Directory information will be compiled, updated, and uploaded to Wikidata, the linked open data database from the Wikimedia Foundation. Directory information will then be delivered via a website, allowing emergency responders to quickly search for NCHs in disaster areas.

("GaNCH" rhymes with "ranch")

## Data

* [Data Dictionary](/data/data_dictionary.md) - Mapping metadata fields to Wikidata's schema
* [Data Sources](/data/data_sources.md) - Where we're getting the directory information
* [Index](/data/index.csv) - Index of all the organizations we've created/edited in Wikidata
* ["Instance of" taxonomy](/data/instance_of_taxonomy.csv) - Taxonomy of all the [P31 "Instance of"](https://www.wikidata.org/wiki/Property:P31) organization types that we are including, and their relevant subclasses. This helps us construct the SPARQL queries we use, since we can say "find me all cultural institutions or anything that's a subclass of cultural institution" to save time and energy.
* [Municipalities](/data/municipalities.csv) - A spreadsheet of Georgia's municipalities and all their counties, mapping the problem where about 10% of Georgia's municipalities belong to more that one county (see: [Addressing Challenges](/docs/challenges.md)).
* [Schema](/data/schema.json) - The OpenRefine schema that we use to reconcile against Wikidata's data model before uploading.
* [Template](/data/TEMPLATE.csv) - The CSV template that we make all the source datasets use.
* [SPARQL_GEMA](/data/SPARQL_GEMA.md) - Examples of SPARQL queries for the GEMA Regions, showing how we use VALUES lists to 1) combine multiple counties together to create the regions, and 2) combine multiple "instance of"s together to get our specific results

## Documentation

### Setup

* [Final GaNCH Grant Proposal - Costs Redacted](/docs/AUCRWWL_CF19_Proposal_021919_FINAL_CostRedacts.pdf)
* [Job Description: Graduate Student Assistant](/docs/2019-06-26_GaNCH_Job%20Description_Student%20Assistant.pdf)
* [Press](/docs/press.md) - Annoucements, press releases, blog posts, publications, and presentations related to the project
* [Resources](/docs/resources.md) - Resources and tools used for GaNCH

### Partners

* [Project Partners List](/docs/project_partners.md) - The organizations that we're partnering with in Georgia to supply directory information, including a point of contact at each organization

### Workflow
* The [Workflow Manual](/docs/workflow.md) provides a step-by-step process for accomplishing the tasks of the project to help others replicate or adapt our process for their own region.
* [Addressing Challenges](/docs/challenges.md) describes and documents some of the challenges we encountered during the project, and how we are addressing them. 
