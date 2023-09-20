# -*- coding: utf-8 -*-
import logging

from django.db import models

from networkapi.models.BaseModel import BaseModel
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Rule(BaseModel):

    id = models.AutoField(
        primary_key=True,
        db_column='id_rule'
    )
    environment = models.ForeignKey(
        'ambiente.Ambiente',
        db_column='id_ambiente',
        null=False,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(
        max_length=80,
        blank=False,
        null=False,
        db_column='name'
    )

    # TODO
    # Caso 5
    # Erro de dependência circular
    # django.db.migrations.exceptions.CircularDependencyError: requisicaovips.0001_initial, blockrules.0001_initial
    # Alinhar com o time Globo
    # https://django.readthedocs.io/en/stable/topics/migrations.html

    # vip = models.ForeignKey(
    #     'requisicaovips.RequisicaoVips',
    #     db_column='id_vip',
    #     null=True,
    #     related_name='vip',
    #     on_delete=models.DO_NOTHING
    # )

    vip = models.IntegerField(
        db_column='id_vip',
        null=True,
        blank=True
    )

    log = logging.getLogger('Rule')

    class Meta (BaseModel.Meta):
        managed = True
        db_table = u'rule'


class BlockRules(BaseModel):

    id = models.AutoField(primary_key=True,
                          db_column='id_block_rules'
                          )
    content = models.TextField(blank=False,
                               null=False,
                               db_column='content'
                               )
    environment = models.ForeignKey(
        'ambiente.Ambiente',
        db_column='id_ambiente',
        null=False,
        on_delete=models.DO_NOTHING
    )
    order = models.IntegerField(
        null=False,
        blank=False
    )

    log = logging.getLogger('BlockRules')

    class Meta (BaseModel.Meta):
        db_table = u'block_rules'
        managed = True


class RuleContent(BaseModel):

    id = models.AutoField(
        primary_key=True,
        db_column='id_rule_content'
    )
    content = models.TextField(
        blank=False,
        null=False,
        db_column='content'
    )
    order = models.IntegerField(
        null=False,
        blank=False,
        db_column='order'
    )
    rule = models.ForeignKey(
        Rule,
        null=False,
        db_column='id_rule',
        on_delete=models.CASCADE
    )

    log = logging.getLogger('RuleContent')

    class Meta (BaseModel.Meta):
        managed = True
        db_table = u'rule_content'
