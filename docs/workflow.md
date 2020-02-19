# Workflow Manual

This page describes how to walk through the full GaNCH workflow, so that you can replicate the process for your own region.  Links from the GaNCH project are included to provide context, but of course your region may have unique local needs.

## Setup

* Download and install free open source software (and one propritary software) to manipulate data and upload it to Wikidata
  * [Git](https://git-scm.com/downloads) - [Version Control](https://www.atlassian.com/git/tutorials/what-is-version-control) software, used to protect your work against accidental deletion.
  * [Visual Studio Code](https://code.visualstudio.com/) - Text and code editor with a built-in terminal. Free and easy to learn interface.
    * [Edit CSV extension](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv) - Edit CSV files in spreadsheet format within VS Code.  We don't use MS Excel since it reformats content (dates, etc.).
    * [markdownlint extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - Helps with formatting markdown files.  We're writing all our documentation in markdown because it provides rich text formatting.
    * [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python for VS Code.
  * [OpenRefine](http://openrefine.org/) - Data wrangling software which is also used to upload to Wikidata.
  * [Microsoft Excel](https://products.office.com/en-us/excel) - You'll use Excel (or [LibreOffice Calc](https://www.libreoffice.org/discover/calc/)) to perform data formatting and cleanup with formulas to prepare CSVs.  Be careful NOT to use Excel for most editing, as it tends to reformat dates, phone numbers, etc.
    * [Excel Fuzzy Lookup Add-In](https://www.microsoft.com/en-us/download/details.aspx?id=15011) for de-duplicating the index.

## Compile

* Reach out to [partner organizations](/docs/project_partners.md) and individuals in your region to identify [data sources](/data/data_sources.md).  
* Data sources can be found on the web, or may be emailed to you directly from a partner organization.  Screen the data for [Personally Identifying Information (PII)](https://en.wikipedia.org/wiki/Personal_data) such as personal email addresses.  If the PII is already available publically on the web (i.e. stan@organization.org published on the organization's website), we include it.  However, if the PII can be replaced with non-peronal information (i.e. info@organization.org), we use the non-personal information.
* Create a [data dictionary](/data/data_dictionary.md) that defines what fields you're going to use, how those field match up to the Wikidata schema, and whether they're going to be required, recommended, or optional.  This will help you format your data correctly for Wikidata, prioritize work, and explain to other folks what you're doing.
* Reformat the data from each source into its own spreadsheet matching a [CSV template](/data/TEMPLATE.csv).
  * HTML lists from websites (like the GAMAG dataset) are reformatted into CSV by hand using [VS Code's multi-cursor](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_multi-cursor-selection) capabilities for batch editing.
  * Straightforward website tables (like the GPLSV dataset) are harvested using the [HTML Table to CSV/Excel Converter](http://www.convertcsv.com/html-table-to-csv.htm)
  * Complex tables (like the GHRAC dataset) are harvested using simple python scripts which dump data into pipe-delimited text files.  These are then imported into Excel, reformatted to match the template, and exported as CSV.
  * Make sure to include fields for the Reference URL (REF URL) and Retrieval Date (RET DAT) for the data, to provide references in Wikidata.
  * If you're working with several datasets and you know that some organizations will be duplicated across datasets, create an [index](/data/index.csv) that will help you de-dupe organizations as you add on new datasets.  This will prevent you from wasting time and energy by performing the Update & Source step multiple times for the same organization.  
    * Generate the new datatset and back it up using Git (see below) so you have a snapshot of the whole dataset.
    * Use the [Excel Fuzzy Lookup Add-In](https://www.microsoft.com/en-us/download/details.aspx?id=15011) to compare your new dataset to the index, idenfitying duplicated records.
    * Delete duplicated record rows in the new dataset -- that way you're only updating and sourcing data for each organization record once.
    * If you accidentally deleted an organization that wasn't duplicate, use Git to view the deleted record and copy-and-paste it back into your dataset to update and source.
* As you work, use [Git](https://www.atlassian.com/git/tutorials/what-is-git) to save your work as you go.  You can get fancy with Git, but for our work we mostly use "[git pull](https://www.atlassian.com/git/tutorials/syncing/git-pull)", "[git add .](https://www.atlassian.com/git/tutorials/saving-changes)", "[git commit -m "what changed"](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)" and "[git push](https://www.atlassian.com/git/tutorials/syncing/git-push)".
* At the end of this step, you will have several datasets formatted to match your CSV template.

## Update & Source

* Starting with web-based research, verify that the data is correct.  
  * Look at each orgnization provided on the partner's list, and try to find that organization on the web.  
  * Make sure that the data that was provided by the partner matches what is on the web, since datasets can become out-of-date relatively quickly.  
  * If you find a more up-to-date fact, update the CSV spreadsheet and record the source of the updated information in the REF URL field, and the date you made the update in the RET DAT field.
  * Whenever possible, use the Internet Archive Wayback Machine's [Save Page Now](https://web.archive.org/save) tool to provide a REF URL that also records the date that the fact was true.
  * If the partner's list is correct, you can cite that list in the REF URL and RET DAT fields.
* If the information you find is ambiguous or confusing, perform email and [phone research](/docs/phone_script.md) to reach out to the organization for clarification.
  * Cite the email or phone conversation in the "Source Notes" field of the CSV spreadsheet.  
  * You can then cite your CSV as the REF URL source (yes it's recursive, but this way you can record that the information was updated via phone call or email like a [MARC 670a Source citation](https://www.loc.gov/marc/authority/ad670.html)).  Once it's uploaded to Wikidata, your CSV can serve as the source/reference for the corrected information.

Below is an example of 1) the phone number field, 2) the phone number REF URL field, and 3) the phone number RET DAT fields. Underlined in red are several corrected phone numbers with their associated REF URLs and RET DATs for the locations and dates of the corrections.
![Example of 1) the Phone field, 2) the Phone REF URL field, and 3) the Phone RET DAT fields. Underlined in red are several corrected phone numbers with their associated REF URLs and RET DATs for the locations and dates of the corrections.](/docs/images/phone_number_REF_URL_and_RET_DAT.png)

* Generate coordinate location & county
  * Using a free online tool like [Geocod.io](https://www.geocod.io/) or [MapLarge's Geocoder](https://geocoder.maplarge.com/Geocoder) (free version limited to batches of 100), generate coordinate location and county for each organization's address.  
  * These tools are not exact, so you'll check to make sure that the mapping is correct during the Quality Control step below.
  * Note that Wikidata requires you to *ingest* coordinate location using decimal format (i.e. "34.435818, -84.702066"), but *displays* coordinate location using DMS format (i.e. "34° 26′ 8.95″ N, 84° 42′ 7.44″ W").

## Reconcile

* Before begnning the reconciling process for your dataset, see if your region is well-described geographically in Wikidata.
  * To save time during reconciliation, make sure that administrative regions (counties, boroughs, parishes, territories, districts, census areas, consolidated city-counties, etc.), [municipalities](https://www.wikidata.org/wiki/Q76514543) (cities and towns with a local government), and [unincorporated communities](https://www.wikidata.org/wiki/Q17343829) (small towns without local governments) are already in Wikidata and have helpful descriptions (so you can tell your region's "Springfield" or "Franklin County" from all the others in the world).
* Using OpenRefine, reconcile your spreadsheet, build your schema, check for issues, and preview the results.
  * On the rows tab, [reconcile](https://github.com/OpenRefine/OpenRefine/wiki/Reconciliation) those fields that can be reconciled against Wikidata (organization label, instance of, city, state, county, country, parent organization, and subsidiaries).  Unique fields (phone number, email address, official website, etc.) don't have to be reconciled.
  * On the [Schema](https://www.wikidata.org/wiki/Wikidata:Tools/OpenRefine/Editing/Schema_alignment) tab, build out the schema to map your fields to the matching properties in Wikidata.  Use your REF URL and RET DAT fields to create field-specific references.
  * On the [Issues](https://www.wikidata.org/wiki/Wikidata:Tools/OpenRefine/Editing/Quality_assurance) tab, check for typos, conflicts, or other problems. Resolve what you can.
  * On the Preview tab, do a final check to make sure that the sample records are displaying the way you want them to.  Go back and fix any problems you notice.
* NOTE: OpenRefine is awesome, but there are some challenges to be aware of:  
  * When reconciling or building the schema, OpenRefine will time out if the Wikidata query service server is running slowly.  If it's lagging too much, do some other kind of work and come back later when the server isn't so busy.
  * OpenRefine doesn't give you a report after uploading to Wikidata, so if records were skipped you won't know unless you specifically look for them.  You can catch these by doing a post-ingest check, or during the Quality Control step.
  * You can't create a new item in OpenRefine and create relationships for that item (e.g. Parent Organization and Subsidiaries) at the same time.  Create the new items first (removing the Parent Org and Subsidiary fields from the schema), then do a seperate upload of the relationship fields after the items already exist.  Since property creation doesn't happen simultaneously, OpenRefine may choke on inverse-dependent relationships. 

## Upload

* Updates are uploaded to Wikidata.

## Quality Control

* A team member who didn't work on the original dataset reviews the records in Wikidata for any errors.
* Each location coordinate should be checked closely, since they are automatically generated and prone to being incorrect.
  * On the organization record in Wikidata, right click on the coordinate location and open in a new tab.
  * This will take you to the coordinate location on the GeoHack website.  Click on Google Maps link at the top of the screen to open the coordinate location in Google Maps.  Zoom in to see if the coordinate location pin is located on top of the correct location.  If the location isn't labeled, you may have to use Street View to confirm that it's the correct location.  If the location is correct, move on to the next record.
  * If the coordinate location is incorrect, search to find the correct location (which may take some sleuthing).  Once you have found the correct location, right click on top of the location and choose "What's here?"  In the pop-up menu at the bottom of the screen, click on the decimal coordinate location.  On the left menu, copy the decimal coordinate location.
  * For the REF URL reference, copy the URL up through the decimal coordinate location (i.e. <https://www.google.com/maps/place/Johnston+Lakes+Library/@30.6835504,-83.2116414,19z/>). NOTE that Wikidata does *not* accept reference URLs formatted with DMS coordinate locations in the URL (i.e. <https://www.google.com/maps/place/30°41'00.8"N+83°12'40.0"W/@30.6835502,-83.2116545,19z/>) since they include non-standard characters.
* As the reviewer checks (and potentially corrects) each record in Wikidata, they mark that they've checked it in the dataset in the QC column by adding the date reviewed and their initials (i.e. 2019-12-03 CL)
* Since quality control is done in Wikidata, your dataset will no longer be the "source of truth" after ingest.  The datasets exist for the purpose of ingesting data and references into Wikidata and performing quality control.  Wikidata then becomes the source of truth, not your datasets.

## Access

* Web Developer creates a website to display results at the City, County, and State level.

## Maintain

* Web Developer creates an automated process to email NCHs annually to request updates. [Partner organizations](/docs/project_partners.md) assist in annual updates.

## Promote

* Partner organizations provide outreach to NCHs.
