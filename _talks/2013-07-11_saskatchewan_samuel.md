---
layout: page
description: Conference Paper
author: Wout Dillen
title: The Samuel Beckett Digital Manuscript Project as a Collaborative Genetic Edition
year: 2013
eventtitle: Social, Digital, Scholarly Editing
location: Saskatchewan, Canada
venue: University of Saskatchewan
eventdate: 2013-07-11/2013-07-13
eventurl: "https://web.archive.org/web/20140301035751/https://ocs.usask.ca/conf/index.php/sdse/sdse13"
category: conference-papers
---
{% include talk_intro.liquid %}

### Abstract
The *Samuel Beckett Digital Manuscript Project* (BDMP) aims to reunite and make publically accessible all manuscripts of Samuel Beckett’s works, the physical documents of which are located in different holding libraries around the world. The digital aspect of this substantial genetic edition (www.beckettarchive.org) consists of 26 modules, one published each year, each of which comprises digital facsimiles and transcriptions of all extant manuscripts pertaining to an individual text – or to a collection of shorter texts. Each of the modules will have a different single editor or editorial team. This paper offers a detailed description of the project (a new module of which is scheduled to appear around the time of the conference), focussing on its social aspect. 

The BDMP’s social aspect is twofold. Its first part is internal: during the production process, the preparation of these modules takes a considerable collaborative effort. In collaboration with the Project’s founders Mark Nixon (University of Reading) and Dirk Van Hulle (University of Antwerp), and with the technical support of Vincent Neyt (University of Antwerp), the editors are responsible for the transcription of their module’s manuscripts into XML. Often, the editors are also assisted by undergraduates and international PhD students, working as interns at the University of Antwerp’s Centre for Manuscript Genetics. To facilitate the teamwork of this variable assembly, the BDMP is an interested party concerning open source technologies that allow for collaborative editing of genetic materials in TEI-compliant XML. 

The digital publication architecture of the BDMP uses Apache Cocoon, an XML publishing framework. At the moment, all members of the editorial team have installed this architecture in a local server on their computers. Currently, the transcriptions in XML are mailed back and forth between the editors, with each document’s ‘Master File’ only belonging to one editor at one time. This system, though it has proved to work these past years, still holds dangers because multiple instances of the file exist. To bypass these problems and optimize the project’s productivity, it would be ideal if a ‘Collaborative Editing System’ could be plugged into the Apache Cocoon architecture, allowing the editorial team to create and modify the transcriptions simultaneously in an online environment. To this end, we would like to present the BDMP to the conference’s community of experts as a possible test case for the developers of such systems. 

The project’s second social aspect is external: to keep the modules updated, to allow for new interpretations of ‘unclear’ readings in the manuscripts, and to fix bugs and correct errors, the BDMP provides its readers the opportunity to comment on different aspects of the edition. These comments are reviewed by the module’s editors before they are implemented, in order to guarantee the quality of the work. Updates to the edition are recorded in a changelog in the header of to the relevant .xml-file. The BDMP also welcomes ideas that would increase the reader’s participation in the edition.