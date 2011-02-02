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
* Data are fixed at 2010-12-31 for a few weeks, then they go real-time (with historical view)
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

Location data need to be mapped to constituencies. 
This can be done through     
::

  op_location
  op_constituency_location
  op_constituency
  op_election_type

This map should be cached, and not computed at each request.

Cached data in ``opp_politician_history_cache`` lack some fields: parliamentary group and constituency, but those fields
are present in the ``opp_carica`` table, which has a one-to-one relation to the cached data, through the ``chi_id`` field.
A *view* may be created in mysql, named ``opp_productivity_index_view``, and the connection could query the view, instead of using a more complex join in the query.

:Authors:
    Guglielmo Celata,
    Ettore Di Cesare,
    DEPP Srl
:Version:
    1.0
    