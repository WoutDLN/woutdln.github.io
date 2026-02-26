---
layout: page
description: Conference Paper
author: Wout Dillen
title: Clean versus Functional Code in Scholarly Digital Editing
subtitle: The Case of the Beckett Digital Manuscript Project
year: 2014
eventtitle: ESTS 2014
eventtitleaddon: Textual Trails. Transmissions of Oral and Written Texts
venue: The Finnish Literature Society
location: Helsinki, Finland
eventdate: 2014-10-30/2014-11-01
img: /assets/img/cities/helsinki.jpg
date: 2014-10-31
eventurl: "https://web.archive.org/web/20151002220926/https://www.finlit.fi/fi/tutkimus/kriittiset-editiot-edith/textual-trails-transmissions-oral-and-written-texts#.Vg8Amy_P3wP"
programmeurl: "https://web.archive.org/web/20171012193335/http://www.finlit.fi/sites/default/files/mediafiles/tutkimus/programme_ests2014.pdf"
pdf: /assets/pdf/slides/2014-10-31_clean-vs-functional-code.pdf
category: conference-paper
---
{% include talk_intro.liquid %}

### Abstract

The introduction of descriptive markup into the field of Textual Criticism represents one of the greatest technological advances the Digital Turn has brought to the field. Not only does this type of markup allow us to separate a source text's transcription from its presentation (thereby allowing that transcription to be presented in a variety of ways, potentially based on a variety of editorial principles); it also forces the editor of the scholarly digital edition to make her interpretation of that source text more explicit by adding a new layer of textual signs to the text. 

On the one hand, the more information is included into the source text's transcription the better, because the textual trail of descriptive markup the editor of a scholarly digital edition leaves behind effectively increases her accountability for the editorial decisions she makes. In addition, if the transcription's portability is ensured (e.g. by encoding it in TEI-conformant XML), third parties can use the added information for their own purposes, such as computer-aided text analysis. On the other hand, however, extensive tagging may cause the transcription to reach a point where it becomes too difficult to see the wood for the trees. The more information an encoded document contains, the more pre-processing that document may require: for specific tasks, most of the information in the encoded document will often be redundant, and may therefore hinder or at least slow down the process of (human or computer-aided) text analysis. Furthermore, while all the signs in an XML document are (as a rule) human readable, that does not mean that all of the code in TEI-conformant XML documents is designed to be read by human eyes. If a transcription is part of a scholarly digital edition with its own tools and functionalities, it will often need additional code to make those tools work – such as a series of coordinates that facilitate image/text-linking for example. Such 'functional' code is often only marginally related to the transcribed text itself, and incomprehensible for the human reader who is interested in that text. 

In this paper, I will demonstrate how the editor of Scholarly Digital Editions leaves a textual trail behind in the texts she transcribes and investigate the tension this trail creates between 'clean' and 'functional' markup, using the Beckett Digital Manuscript Project ([www.beckettarchive.org](http://www.beckettarchive.org/)) as a case study.