Dit is een Odoo 14 module wat een MIS Rapport template bevat, wat
gebruikt kan worden om de BTW grootboeken van Odoo aan het eind van het
jaar zodanig af te sluiten, dat:

* Alle rekeningen met verschillende BTW categoriën weer op nul gezet
  worden.
* De grootboekrekening 155000 bevat op 1 januari van het volgende jaar
  alleen het bedrag wat in de loop van januari nog over het afgesloten
  boekjaar moet worden afdragen.

Het bestand btw-boeking-template.ods wordt niet gebruikt door het Odoo module.
Download het naar uw PC en gebruik Excel of libreOffice om een handmatige
boeking te doen:

Gebruik dit spreadsheet om de BTW boeking die je hebt gemaakt in Odoo met Rapportages→MIS Rapporten→BTW boeking om te zetten in een memoriaalboeking (Journal Entry).

* Maak met een MIS Rapport (Rapportages→MIS Rapporten) een nieuw rapport voor het jaar wat je wilt sluiten voor de BTW (01-01 t/m 31-12, of je fiscale jaar als dat niet gelijk is aan het kalenderjaar)
* Bekijk dit rapport, controleer of dit er goed uit ziet.
* Exporteer het rapport naar Excel of ODS formaat.
* Open dit geëxporteerde bestand, en kopiëer het enige tabblad over het tabblad “MIS report export” van dit template
* Selecteer het tabblad “boeking”. Verwijder alle regels na regel 5 waarvan Journal Items/Credit of Journal Items/Debit de waarde nul hebben.
* Sla het bestand op onder een andere naam, bijvoorbeeld btw-boeking-2022.ods
* Importeer de journaalboeking onder Boekhouding→Boekingen. De “Importeer records” knop is verstopt onder het “Favorieten” icoon. Druk nog niet op “Bevestigen”.
* Draai een Trial Balance uit (Vink “Alle boekingen” aan) . Controleer dat het 155000 grootboek een saldo heeft van hooguit een paar Euro (de afronding in uw voordeel die u op de BTW aangifte mag maken), plus het BTW bedrag wat u in januari van het volgende boekjaar moet betalen. Alle grootboekrekeningen Af te dragen BTW en Voorbelasting horen op nul te staan.
