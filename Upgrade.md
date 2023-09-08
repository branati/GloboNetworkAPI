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
   - Status: Pendente
   - Alinhado com a Globo: Não
   - Descrição: django.db.migrations.exceptions.CircularDependencyError: ambiente.0001_initial, vlan.0001_initial





