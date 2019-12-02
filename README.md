# ZooHackathon2019

![ZooHackathon 2019](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_photos/000/863/216/datas/full_width.png)

Global Problem Statement 7
Organization: TRAFFIC
Problem Statement POC: Willow Outhwaite (Research and Analysis Programme Officer)
willow.outhwaite@traffic.org

Title: It costs how much? Monitoring the changing price of wildlife online

The Problem:
Keeping abreast of the latest trade trends, fluctuations, dynamics and criminal activity is
essential to protecting natural biodiversity. TRAFFIC was established as the "wildlife trade
monitoring network" and wildlife trade monitoring is still at the heart of what we do.
TRAFFIC has a long history of monitoring physical markets to determine which species and
commodities are in trade, the volume and the price. However, increasingly the sale of legal and
illegal wildlife is moving online. The internet provides quick and extensive information to a vast,
ever increasing interconnected audience. Internet markets are flourishing, with eBay one of the
most popular auction websites, visited by users worldwide. In addition to auction websites, chat
rooms on thematic websites also allow traders to advertise, communicate with customers and
make deals for almost any products, including those derived from wild animals and plants.
Recent TRAFFIC studies have found the online trade is truly global. For example, focusing on
ivory alone:
- Websites with a domain .vn (Viet Nam) were found selling a total of 1,066 ivory
products1 - Six online antique marketplaces offered a total of 2,008 ivory items in the United
Kingdom2 1 Indenbaun, R. A. (2018) Viet Nam Online: A rapid assessment of e-commerce wildlife trade in Viet Nam 2017 TRAFFIC International, Cambridge, United Kingdom 2 Lau, W., Crook, V., Musing, L., Guan, J. and Xu, L. (2016) A rapid survey of UK ivory markets. TRAFFIC, Cambridge, UK.
- A total of 2,056 pieces of ivory were documented for sale online in the USA by vendors
based in 47 states, worth an estimated starting price of 3,437,250 .3
It is not only ivory that can be found for sale online, but a wide variety of species including
reptiles, amphibians, mammals, fish, birds, invertebrates and plants. Species assessed as being
threatened on the IUCN Red List can be found for sale. For example, two Critically Endangered
species (Helmeted Hornbill Rhinoplax vigil and Siamese Crocodile Crocodylus siamensis) were
found for sale online in a recent survey in Thailand . The same study found a total of 1,521 live 4
animals from at least 200 species offered for sale: just over half of the species offered for sale are
protected by law in Thailand, and some were listed in the CITES Appendices. Some of the
wildlife for sale is legal, some is illegal, and for a proportion it is difficult to tell as clear
legislation around offers for sale online may not exist.
Trying to monitor the vast internet to determine the volume of wildlife for sale and the price is
incredibly intensive, with surveyors either relying on manual searches of key words or
developing “web-scrapers” to automate the process. If a tool were to be developed which further
automated this work, it would free up conservationists’ time to work on other pressing issues
affecting wildlife. Monitoring using these existing methods is made even more difficult by the
ever-evolving nature of online trade: vendors may switch to advertising on different websites or
platforms, and the key words they use to describe their product may evolve. In addition, some
advertisements are hoaxes or fraudulent sales, and the specimen of wildlife can be offered for
sale in multiple places. Wildlife can be offered for sale in numerous languages, and prices given
in different currencies.

The Challenge:
For conservationists (such as those working for TRAFFIC or within the IUCN Species Survival
Commission) that have limited coding skills, it would be useful to develop an easy to use tool
that allows the user to enter their search criteria (e.g. species name, or commodity type (ivory,
shark fin, wild meat). The tool would then search the internet and provide back a summary of the
data.

Criteria:
Developing a tool that monitors the volume of wildlife offered for sale is likely impossible, but
what would be useful is a tool that can determine the average price given in an advert and the
number of adverts. If the tool can determine the number of specimens offered for sale (e.g. 3
live, 5 bones, 2 skins) that would be even better. The assumption is that obtaining the number of
adverts available and average price per advert would allow the user to make some inferences on
the size of the supply and demand. For example, if the average price per item is increasing this
3 Kramer, R., Sawyer, R., Amato, S. and LaFontaine, P. (2017) The US elephant ivory market: A new baseline. TRAFFIC, Washington, DC. 4 Phassaraudomsak, M. and Krishnasamy, K. (2018). Trading Faces: A rapid assessment on the use of Facebook to trade in wildlife in Thailand. TRAFFIC, Petaling Jaya, Selangor, Malaysia.
could mean that demand is increasing or supply is decreasing. An example of how the results
may look is provided below.
The tool should be easy to use for people with limited technical skills.
The tool should be able to convert the search terms into different languages. It should also be
able to convert prices offered in different currencies into a standard currency (e.g. USD), ideally
taking into account varying conversion rates.
What sets this apart from a typical web-scraper is that it would be able to identify adverts from
any other post that contains the key words (e.g. adverts of iguanas for sale vs. photos people took
on holiday of iguanas, advice for iguana keepers etc.). It could also use machine learning to
search for similar search terms that evolve over time. Finally, it would be helpful if it could
detect the same advert (either by photo or text) that has been posted in multiple places, and
account for the duplication.
Ideally the tool could be used for any species/commodity but a first version could focus on one
species/group for example live reptiles, medicinal products containing pangolin, elephant ivory
carvings.
Ideally the tool would be able to search across platforms that have different layouts, but a first
version could focus on getting it to work on one website (e.g. for reptiles =
http://www.faunaclassifieds.com/ or https://www.terraristik.com).
As noted above, there are issues that make searching for adverts difficult:
- hoaxes or fraudulent sales
- on auction sites (e.g. eBay) a decision has to be made to decide which is the price
(starting bid or final)
- specimen of wildlife can be offered for sale in multiple places
- wildlife can be offered for sale in numerous languages, and prices given in different
currencies
- wildlife can be offered for sale in numerous languages, and prices given in different
currencies
Data Sets and Other Resources:
● The relevant IUCN SSC – Specialist Group should be consulted for advice on
specific-specific trade information.
● TRAFFIC has undertaken a number of web surveys which can be found online and help
typical search methods and websites: https://www.traffic.org/publications/. Other
organizations such as IFAW also conduct online surveys (e.g.
https://www.ifaw.org/news/killing-with-keystrokes-20-ifaws-investigation-into-the-europ
ean-online-ivory-trade).
● Key words (on Facebook) = Buy-Sell Animals, Exotic Animals, Buy-Sell Exotic Pets /
Animals, Buy-Sell Exotic from
https://www.traffic.org/site/assets/files/11073/trading_faces_thailand_2019.pdf
● Key words (English translation of Vietnamese words) = ivory, genuine ivory, sell ivory,
sell-buy ivory, ivory jewellery, ivory carvings, smoking pipe, ivory smoking pipe from
https://www.traffic.org/site/assets/files/11494/traps-tusk-to-trinket.pdf
