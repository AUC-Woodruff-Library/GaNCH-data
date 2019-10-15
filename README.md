# GaNCH

Using Linked Open Data for Georgia's Natural, Cultural, and Historic Organizations' Disaster Response.

The [Atlanta University Center Robert W. Woodruff Library](https://www.auctr.edu/) would like to gratefully acknolwedge [LYRASIS](https://www.lyrasis.org/Pages/Main.aspx) for their support of this project via a [2019 LYRASIS Catalyst Fund grant](https://lyrasisnow.org/press-release-lyrasis-announces-the-2019-catalyst-fund-recipients-and-their-projects/)

This one-year project will create a publicly editable directory of Georgia’s Natural, Cultural and Historical Organizations (NCHs), allowing for quick retrieval of location and contact information for disaster response. Directory information will be compiled, updated, and uploaded to Wikidata, the linked open data database from the Wikimedia Foundation. Directory information will then be delivered via a website, allowing emergency responders to quickly search for NCHs in disaster areas.

## Documentation

### Setup

* [Final GaNCH Grant Proposal - Costs Redacted](/docs/AUCRWWL_CF19_Proposal_021919_FINAL_CostRedacts.pdf)
* [Job Description: Graduate Student Assistant](/docs/2019-06-26_GaNCH_Job%20Description_Student%20Assistant.pdf)
* [Press](/docs/press.md) - Annoucements, press releases, blog posts, publications, and presentations related to the project
* [Resources](/docs/resources.md) - Resources and tools used for GaNCH

### Partners

* [Project Partners List](/docs/project_partners.md) - The organizations that we're partnering with in Georgia to supply directory information, including a point of contact at each organization
* [2019-08-29 GaNCH Partners Meeting](https://archive.org/details/2019-08-29_ganch_partners_meeting)

### Workflow

* Compile (Jul – Sep, 2019). Graduate Student Assistant (GSA) will use a curated list of [data sources](/data/data_sources.md) as a starting point. Data from each source will be reformatted into a CSV spreadsheet.
  * HTML lists (like GAMAG) will be reformatted into CSV by hand using [VS Code's multi-cursor](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_multi-cursor-selection) capabilities for batch editing.
  * Straightforward tables (like GPLSV) will be harvested using the [HTML Table to CSV/Excel Converter](http://www.convertcsv.com/html-table-to-csv.htm)
  * Complex tables (like GHRAC) will be harvested using a simple python script which will dump data into a pipe-delimited text file, which can then be reformatted into CSV by hand using VS Code's multi-cursor capabilities for batch editing.
* Update (Oct – Dec, 2019). GSA will use web, email, and phone research to confirm that the data is correct and add any updates as necessary.
  * [Phone Script](/docs/phone_script.md)
* Source (Oct – Dec, 2019). Each item will be sourced with references to allow for verification of the updates.
  * Web-based references will be captured and dated using the Internet Archive Wayback Machine's [Save Page Now](https://web.archive.org/save) tool.
* Reconcile (Jan, 2020). Using OpenRefine, the spreadsheet will be reconciled against Wikidata’s schema.
* Upload (Feb, 2020). Updates will be uploaded to Wikidata.
* Access (Feb - Apr, 2020). Web Developer will create a website to display results at the City, County, and State level.
* Maintain (Mar – May, 2020). Web Developer will create an automated process to email NCHs annually to request updates. Partner organizations (see below) will assist in annual updates.
* Promote (Apr – Jun, 2020). Partner organizations have expressed an interest in providing outreach to NCHs.

## Data

* [Data Dictionary](/data/data_dictionary.md) - Mapping metadata fields to Wikidata's schema
* [Data Sources](/data/data_sources.md) - Where we're getting the directory information
* [Data Actions](/data/data_actions.md) - Step-by-step tracker of what we did
