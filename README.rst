Introduction
============
This web application shows the computed *Index of Productivity* for representatives in the italian Parliament.
It is intended to be used to launch the Openpolis Membership campaign

Requisites
----------
* A home page with:
   * dynamic introductory text,
   * top ten charts for **Senato** and **Camera**,
   * big banners to launch membership, pdf report download, link to openparlamento
   * location-chooser autocomplete field
* Complete charts for **Senato** and **Camera**, 
   * showing name, parliamentary group, constituency, index and non-attendance %,
   * groupable by constituency, parliamentary group and sex,
   * sortable by name, constituency, index and non-attendance %
   * [later] historic links (last month, six months ago, last year, ...)
* Location page, with complete charts filtered by constituency related to location
* Dynamic page describing the methodology
* Data are real-time (last date available)
* Location are chosen through autocompleter (possibly client-side)
* Sorting should be client-side (javascript)
* Complete charts are scrolled through ajax requests (javascript)
* Application should be optimized for high-volume traffic (memcache)
* The content must be in italian and in english (multi-lingual)

Architecture
------------
*Productivity Index* data are stored in the mysql ``op_openparlamento.opp_politician_history_cache`` table.
Location is stored in the ``op_openpolis.op_location`` table.
The application is developed in **Django**, and will have three database connections:
* default: sqlite database containing session, authentication, flatpages, ...
* op: read-only access to mysql ``op_openpolis`` database (to get op_location data)
* opp: read-only access to mysql ``op_openparlamento`` database (to get ``opp_politician_history_cache`` data)


Notes
-----
Location data need to be mapped to constituencies. A user enters her city, and chart data are filtered by the corresponding constituency. This mapping can be done through  the following tables in ``op_openpolis``::

  op_location
  op_constituency_location
  op_constituency
  op_election_type

This map should be *cached*, in order not to perform a query at each request.


Cached data in ``opp_politician_history_cache`` lack some fields: parliamentary group and constituency, but those fields
are present in other tables, so a join is required.
Data can be extracted directly from the DB, using multiple database connections and the Manager.raw method.

The settings.DATABASES parameter contains an ``opp`` connection, with read only access to the ``op_openparlamento`` database.

See charts/models.py and charts.views.py for details on how records are extracted from there, using this complex query::

  select pc.id, pc.chi_id, p.nome, p.cognome, g.acronimo, c.circoscrizione, 
         pc.assenze/(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, pc.indice 
  from opp_politician_history_cache pc, opp_carica c, opp_politico p, 
       opp_carica_has_gruppo cg, opp_gruppo g 
  where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and 
        cg.data_fine is null and c.data_fine is null and 
        pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s


:Authors:
    Guglielmo Celata,
    Ettore Di Cesare,
    DEPP Srl
:Version:
    1.0

