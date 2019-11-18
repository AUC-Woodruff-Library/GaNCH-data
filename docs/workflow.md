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

## Compile

* Reach out to [partner organizations](/docs/project_partners.md) and individuals in your region to identify [data sources](/data/data_sources.md).  
* Data sources can be found on the web, or may be emailed to you directly from a partner organization.  Screen the data for [Personally Identifying Information (PII)](https://en.wikipedia.org/wiki/Personal_data) such as personal email addresses.  If the PII is already available publically on the web (i.e. stan@organization.org published on the organization's website), we include it.  However, if the PII can be replaced with non-peronal information (i.e. info@organizationl.org), we use the non-peronal information.
* Create a [data dictionary](/data/data_dictionary.md) that defines what fields you're going to use, how those field match up to the Wikidata schema, and whether they're going to be required, recommended, or optional.  This will help you format your data correctly for Wikidata, prioritize work, and explain to other folks what you're doing.
* Reformat the data from each source into its own spreadsheet matching a [CSV template](/data/TEMPLATE.csv).
  * HTML lists from websites (like the GAMAG dataset) are reformatted into CSV by hand using [VS Code's multi-cursor](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_multi-cursor-selection) capabilities for batch editing.
  * Straightforward website tables (like the GPLSV dataset) are harvested using the [HTML Table to CSV/Excel Converter](http://www.convertcsv.com/html-table-to-csv.htm)
  * Complex tables (like the GHRAC dataset) are harvested using simple python scripts which dump data into pipe-delimited text files.  These are then imported into Excel, reformatted to match the template, and exported as CSV.
  * Make sure to include fields for the Source (REF URL) and Retrieval Date (RET DAT) for the data, to provide references in Wikidata.
  * If you're working with several datasets and you know that some organizations will be duplicated across datasets, create an [index](/data/index.csv) that will help you de-dupe organizations as you add on new datasets.  This will prevent you from performing the Update & Source step multiple times for the same organization.
* As you work, use [Git](https://www.atlassian.com/git/tutorials/what-is-git) to save your work as you go.  You can get fancy with Git, but for our work we mostly use "[git pull](https://www.atlassian.com/git/tutorials/syncing/git-pull)", "[git add](https://www.atlassian.com/git/tutorials/saving-changes)", "[git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)" and "[git push](https://www.atlassian.com/git/tutorials/syncing/git-push)".
* At the end of this step, you will have several datasets formatted to match your CSV template.

## Update & Source

* Starting with web-based research, verify that the data is correct.  
  * Look at each orgnization provided on the partner's list, and try to find that organization on the web.  
  * Make sure that the data that was provided by the partner matches what is on the web, since data sets can become out-of-date relatively quickly.  
  * If you find a more up-to-date fact, update the CSV spreadsheet and record the source of the updated information in the REF URL field, and the date you made the update in the RET DAT field.
  * Whenever possible, use the Internet Archive Wayback Machine's [Save Page Now](https://web.archive.org/save) tool to provide a REF URL that also records the date that the fact was true.
  * If the partner's list is correct, you can cite that list in the REF URL and RET DAT fields.
* If the information you find is ambiguous or confusing, perform email and [phone research](/docs/phone_script.md) to reach out to the organization for clarification.
  * Cite the email or phone conversation in the "Source Notes" field of the CSV spreadsheet.  
  * You can then cite your CSV as the REF URL source (yes it's recursive, but this way you can record that the information was updated via phone call or email like a [MARC 670a Source citation](https://www.loc.gov/marc/authority/ad670.html)).  Once it's uploaded to Wikidata, your CSV can serve as the source/reference for the corrected information.

Below is an example of 1) the phone number field, 2) the phone number REF URL field, and 3) the phone number RET DAT fields. Underlined in red are several corrected phone numbers with their associated REF URLs and RET DATs for the locations and dates of the corrections.
![Example of 1) the Phone field, 2) the Phone REF URL field, and 3) the Phone RET DAT fields. Underlined in red are several corrected phone numbers with their associated REF URLs and RET DATs for the locations and dates of the corrections.](/docs/images/phone_number_REF_URL_and_RET_DAT.png)

## Reconcile

* Using OpenRefine, the spreadsheets are reconciled against Wikidata’s schema.

## Upload

* Updates are uploaded to Wikidata.

## Access

* Web Developer creates a website to display results at the City, County, and State level.

## Maintain

* Web Developer creates an automated process to email NCHs annually to request updates. [Partner organizations](/docs/project_partners.md) assist in annual updates.

## Promote

* Partner organizations provide outreach to NCHs.
