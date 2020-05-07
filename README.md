# GaNCH

GaNCH: Using Linked Open Data for **G**eorgi**a**'s **N**atural, **C**ultural, and **H**istoric Organizations' Disaster Response.

The [Atlanta University Center Robert W. Woodruff Library](https://www.auctr.edu/) would like to gratefully acknolwedge [LYRASIS](https://www.lyrasis.org/Pages/Main.aspx) for their support of this project via a [2019 LYRASIS Catalyst Fund grant](https://lyrasisnow.org/press-release-lyrasis-announces-the-2019-catalyst-fund-recipients-and-their-projects/)

This one-year project will create a publicly editable directory of Georgia’s Natural, Cultural and Historical Organizations (NCHs), allowing for quick retrieval of location and contact information for disaster response. Directory information will be compiled, updated, and uploaded to Wikidata, the linked open data database from the Wikimedia Foundation. Directory information will then be delivered via a website, allowing emergency responders to quickly search for NCHs in disaster areas.

("GaNCH" rhymes with "ranch")

## Data

* [Data Dictionary](/data/data_dictionary.md) - Mapping metadata fields to Wikidata's schema
* [Data Sources](/data/data_sources.md) - Where we're getting the directory information

## Documentation

### Setup

* [Final GaNCH Grant Proposal - Costs Redacted](/docs/AUCRWWL_CF19_Proposal_021919_FINAL_CostRedacts.pdf)
* [Job Description: Graduate Student Assistant](/docs/2019-06-26_GaNCH_Job%20Description_Student%20Assistant.pdf)
* [Press](/docs/press.md) - Annoucements, press releases, blog posts, publications, and presentations related to the project
* [Resources](/docs/resources.md) - Resources and tools used for GaNCH

### Partners

* [Project Partners List](/docs/project_partners.md) - The organizations that we're partnering with in Georgia to supply directory information, including a point of contact at each organization
* [2019-08-29 GaNCH Partners Meeting](https://archive.org/details/2019-08-29_ganch_partners_meeting)
* [2019-10-31 GaNCH Partners Meeting](https://archive.org/details/2019-10-31_GaNCH_Partners_Meeting)
* [2020-01-30 GaNCH Partners Meeting](https://archive.org/details/2020-01-30_GaNCH_Partners_Meeting)
* [2020-03-26 GaNCH Partners Meeting](https://archive.org/details/2020-03-26_GaNCH_Partners_Meeting)

### Workflow
* The [Workflow Manual](/docs/workflow.md) provides a step-by-step process for accomplishing the tasks of the project to help others replicate or adapt our process for their own region.
* [Addressing Challenges](/docs/challenges.md) describes and documents some of the challenges we encountered during the project, and how we are addressing them. 

### Timeline

* Compile (Jul – Sep, 2019). Graduate Student Assistant (GSA) uses a curated list of [data sources](/data/data_sources.md) as a starting point. Data from each source is reformatted into its own spreadsheet matching a [CSV template](/data/TEMPLATE.csv).
* Update (Oct – Dec, 2019). GSA uses web, email, and phone research to confirm that the data is correct and add any updates as necessary.
* Source (Oct – Dec, 2019). Each item is sourced with references to allow for verification of the updates.
* Reconcile (Jan, 2020). Using OpenRefine, the spreadsheets are reconciled against Wikidata’s schema.
* Upload (Feb, 2020). Updates are uploaded to Wikidata.
* Access (Feb - Apr, 2020). Web Developer creates a website to display results at the City, County, and State level.
* Maintain (Mar – May, 2020). Web Developer creates an automated process to email NCHs annually to request updates. [Partner organizations](/docs/project_partners.md) assist in annual updates.
* Promote (Apr – Jun, 2020). Partner organizations provide outreach to NCHs.
