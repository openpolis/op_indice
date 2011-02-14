from django.db import models
import datetime

# these classes are not managed (syncdb will not try to create the tables)
# the model only serves as container for data extracted via the Manager.raw() method 
# from complex queries (join) in the op_openparlamento table


class OpVConstituenciesForLocation(models.Model):
  raw_sql = u"select l.id, l.name as provincia, e.name as ramo, c.name as collegio  from op_location l, op_constituency_location cl, op_constituency c, op_election_type e where c.id=cl.constituency_id and l.id=cl.location_id and c.election_type_id=e.id and e.name in ('camera', 'senato') and l.provincial_id=(select provincial_id from op_location  where name=%s and location_type_id=6) order by l.name, e.name;"
  provincia = models.CharField(max_length=50)
  collegio = models.CharField(max_length=50)
  ramo = models.CharField(max_length=16)
  class Meta:
    managed=False
    db_table = u'op_v_constituency_for_location'

class OppVLastDate(models.Model):
  raw_sql = u"select id, max(data) as last_date from opp_politician_history_cache where chi_tipo='P'"
  last_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
  class Meta:
    managed=False
    db_table = u'opp_v_last_date'


class OppVIndicePolitico(models.Model):
  raw_sqls = {
    'list': u"select pc.id, p.id as politico_id, p.nome, p.cognome, g.acronimo, c.circoscrizione, pc.assenze/(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, pc.assenze as assenze, (pc.presenze+pc.missioni+pc.assenze) as votazioni, pc.indice, pc.indice_pos from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s",
    'group': u"select pc.id, g.acronimo, count(*) as n, sum(pc.assenze)/sum(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, sum(pc.indice) as indice_totale, sum(pc.indice)/count(*) as indice_medio from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s group by g.acronimo",
    'constituency': u"select pc.id, c.circoscrizione, count(*) as n, sum(pc.assenze)/sum(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, sum(pc.indice) as indice_totale, sum(pc.indice)/count(*) as indice_medio from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s group by c.circoscrizione",
    'sex': u"select pc.id, p.sesso, count(*) as n, sum(pc.assenze)/sum(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, sum(pc.indice) as indice_totale, sum(pc.indice)/count(*) as indice_medio from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s group by p.sesso",
    'top': u"select pc.id, p.id as politico_id, p.nome, p.cognome, g.acronimo, c.circoscrizione, pc.assenze/(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, pc.assenze as assenze, (pc.presenze+pc.missioni+pc.assenze) as votazioni, pc.indice from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s order by pc.indice desc limit %s",
    'mps_in_location': u"select pc.id, p.id as politico_id, p.nome, p.cognome, g.acronimo, c.circoscrizione, pc.assenze/(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, pc.assenze as assenze, (pc.presenze+pc.missioni+pc.assenze) as votazioni, pc.indice from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s and c.circoscrizione=%s order by pc.indice desc",
    
  }
  politico_id = models.IntegerField()
  nome = models.CharField(max_length=30, blank=True)
  cognome = models.CharField(max_length=30, blank=True)
  acronimo = models.CharField(max_length=80, blank=True)
  ramo = models.CharField(max_length=1, blank=True)
  circoscrizione = models.CharField(max_length=180, blank=True)
  perc_assenze = models.FloatField(null=True, blank=True)
  indice = models.FloatField(null=True, blank=True)
  indice_pos = models.IntegerField(null=True, blank=True)
  assenze = models.IntegerField(null=True, blank=True)
  votazoni = models.IntegerField(null=True, blank=True)
  class Meta:
    managed=False
    db_table = u'opp_v_indice_politico'
