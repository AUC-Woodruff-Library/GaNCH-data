# Workflow_Manual

This page describes how to walk through the full GaNCH workflow, so that you can replicate the process for your own region.  Links from the GaNCH project are included to provide context, but of course your region may have unique local needs.

## Compile

1. Reach out to [partner organizations](/docs/project_partners.md) and individuals in your region to identify [data sources](/data/data_sources.md)
2. Reformat the data from each source into its own spreadsheet matching a [CSV template](/data/TEMPLATE.csv).

* HTML lists from websites (like the GAMAG dataset) are reformatted into CSV by hand using [VS Code's multi-cursor](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_multi-cursor-selection) capabilities for batch editing.
* Straightforward website tables (like the GPLSV dataset) are harvested using the [HTML Table to CSV/Excel Converter](http://www.convertcsv.com/html-table-to-csv.htm)
* Complex tables (like the GHRAC dataset) are harvested using simple python scripts which dump data into pipe-delimited text files.  These are then imported into Excel, reformatted to match the template, and exported as CSV.

3. At the end of this step, 
* Update (Oct – Dec, 2019). GSA uses web, email, and phone research to confirm that the data is correct and add any updates as necessary.
  * [Phone Script](/docs/phone_script.md)
* Source (Oct – Dec, 2019). Each item is sourced with references to allow for verification of the updates.
  * Web-based references are captured and dated using the Internet Archive Wayback Machine's [Save Page Now](https://web.archive.org/save) tool.
* Reconcile (Jan, 2020). Using OpenRefine, the spreadsheets are reconciled against Wikidata’s schema.
* Upload (Feb, 2020). Updates are uploaded to Wikidata.
* Access (Feb - Apr, 2020). Web Developer creates a website to display results at the City, County, and State level.
* Maintain (Mar – May, 2020). Web Developer creates an automated process to email NCHs annually to request updates. [Partner organizations](/docs/project_partners.md) assist in annual updates.
* Promote (Apr – Jun, 2020). Partner organizations provide outreach to NCHs.
