from django.db import models

# this class is not managed (syncdb will not try to create the opp_v_indice_politico table)
# the model only serves as container for data extracted via the Manager.raw() method 
# from complex queries (join) in the op_openparlamento table
class OppVIndicePolitico(models.Model):
  raw_sqls = {
    'list': u"select pc.id, pc.chi_id, p.nome, p.cognome, g.acronimo, c.circoscrizione, pc.assenze/(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, pc.indice from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s",
    'group': u"select pc.id, g.acronimo, count(*) as n, sum(pc.assenze)/sum(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, sum(pc.indice) as indice_totale, sum(pc.indice)/count(*) as indice_medio from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s group by g.acronimo",
    'constituency': u"select pc.id, c.circoscrizione, count(*) as n, sum(pc.assenze)/sum(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, sum(pc.indice) as indice_totale, sum(pc.indice)/count(*) as indice_medio from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s group by c.circoscrizione",
    'sex': u"select pc.id, p.sesso, count(*) as n, sum(pc.assenze)/sum(pc.presenze+pc.missioni+pc.assenze)*100.0 as perc_assenze, sum(pc.indice) as indice_totale, sum(pc.indice)/count(*) as indice_medio from opp_politician_history_cache pc, opp_carica c, opp_politico p, opp_carica_has_gruppo cg, opp_gruppo g where p.id=c.politico_id and c.id=pc.chi_id and cg.carica_id=c.id and cg.gruppo_id=g.id and cg.data_fine is null and c.data_fine is null and pc.chi_tipo='P' and pc.data=%s and pc.ramo=%s group by p.sesso"
  }
  chi_id = models.IntegerField()
  nome = models.CharField(max_length=30, blank=True)
  cognome = models.CharField(max_length=30, blank=True)
  acronimo = models.CharField(max_length=80, blank=True)
  ramo = models.CharField(max_length=1, blank=True)
  circoscrizione = models.CharField(max_length=180, blank=True)
  perc_assenze = models.FloatField(null=True, blank=True)
  indice = models.FloatField(null=True, blank=True)
  class Meta:
    managed=False
    db_table = u'opp_v_indice_politico'
