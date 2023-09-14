# Documentação de Upgrades
Esse documento tem como objetivo centralizar os problemas encontrados.
# Problemas e soluções
 
1. Problema de dependência circular entre os modelos Ambiente (networkapi/ambiente/models.py) e DatacenterRooms (networkapi/rack/models.py).
   - Status: Resolvido 
   - Alinhado com a Globo: Sim
   - Possível solução: a solução é modelar o atributo dcroom em Ambiente com o tipo inteiro, sem FK para DatacenterRooms.



2. Problema de dependência circular entre os modelos EquipamentoAcesso (networkapi/equipamento/models.py), Vrf (networkapi/api_vrf/models.py) e Equipamento (networkapi/equipamento/models.py).
   - Status: Resolvido
   - Alinhado com a Globo: Sim
   - Descrição: O campo default_vrf não existe no banco de dados. Foi retirado da model Ambiente. O erro de dependência foi sanado.


3. Problema  de dependência circular entre os modelos Ambiente e Vlan
   - Status: Pendente resposta para prosseguimento do trabalho.
   - Alinhado com a Globo: Sim
   - Descrição: django.db.migrations.exceptions.CircularDependencyError: ambiente.0001_initial, vlan.0001_initial


4. Problema de dependência circular entre os modelos equipamento e api_vrf
   - Status: Confirmado e resolvido
   - Alinhado com a Globo: Sim.
   - Erro do Django: django.db.migrations.exceptions.CircularDependencyError: equipamento.0001_initial, api_vrf.0001_initial
   - Descrição: Essa dependência foi comentada em reunião nessa semana. Importante confirmação dessa ação.
   - Resolução: Exclusão do campo na model antiga: equipamento.vrf, que deveria ter sido feito na criação da App nova: api_vrf, que já contém VrfVlanEquipment.equipment (FK de equipamento). Assim a dependência cíclica foi resolvida.
   - Solicitado, em 11/09/2023, para converter o campo que causa dependência cíclica para o tipo String.


5. Problema de dependência circular entre os modelos requisicaovips e blockrules
   - Status: Pendente posicionamento da Globo
   - Erro do Django: django.db.migrations.exceptions.CircularDependencyError: requisicaovips.0001_initial, blockrules.0001_initial
   - Descrição: Dependência encontrada.  Conferidos os campos em conflito. Campos requisicaovips.RequisicaoVips.rule, requisicaovips.RequisicaoVips.rule_applied e requisicaovips.RequisicaoVips.rule_rollback comparando com blockrules.Rule.vip.
   - Resolução: Indicado pela globo em 11/09/2023, para alterar o campo blockrules.Rule.vip (id_vip no banco de dados) de ForeignKey para Integer.


