# -*- coding: utf-8 -*-
from __future__ import unicode_literals

localeID = 'pt_BR'

dateSep = ['/']
usesMeridian = False
uses24 = True

Weekdays = [
    'segunda|segunda-feira', 'terça|terca|terça-feira|terca-feira', 'quarta|quarta-feira',
    'quinta|quinta-feira', 'sexta|sexta-feira', 'sábado|sabado', 'domingo',
]

shortWeekdays = [
    'seg', 'ter', 'qua', 'qui', 'sex', 'sáb|sab', 'dom',
]

Months = [
    'janeiro', 'fevereiro', 'março|marco', 'abril', 'maio', 'junho', 'julho',
    'agosto', 'setembro', 'outobro', 'novembro', 'dezembro',
]

shortMonths = [
    'jan', 'fev', 'mar', 'abr', 'mai', 'jun',
    'jul', 'ago', 'set', 'out', 'nov', 'dez',
]

dateFormats = {
    'full': "EEEE, d' de 'MMMM' de 'yyyy",
    'long': "d' de 'MMMM' de 'yyyy",
    'medium': 'dd-MM-yy',
    'short': 'dd/MM/yyyy'
}

timeFormats = {
    'full': "HH'H'mm' 'ss z",
    'long': 'HH:mm:ss z',
    'medium': 'HH:mm:ss',
    'short': 'HH:mm',
}

dp_order = ['d', 'm', 'y']

numbers = {
    'zero': 0,
    'um': 1,
    'uma': 1,
    'dois': 2,
    'três': 3,
    'tres': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'treze': 13,
    'catorze': 14,
    'quatorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
}

decimal_mark = ','


units = {
    'seconds': ['segundo', 'segundos', 'seg', 'segs', 's'],
    'minutes': ['minuto', 'minutos', 'min', 'mins', 'm'],
    'hours': ['hora', 'horas', 'hr', 'hrs', 'h'],
    'days': ['dia', 'dias', 'd'],
    'weeks': ['semana', 'semanas', 'sem'],
    'months': ['mês', 'mes', 'meses'],
    'years': ['ano', 'anos'],
}


re_values = {
    'specials': 'em|às|as|na',
    'timeseparator': ':',
    'rangeseparator': '-',
    'daysuffix': 'º',
    'qunits': 'h|m|s|d|sem|ano',
    'now': ['agora', 'agora mesmo'],
}

Modifiers = {
    'from': 1,
    'antes': -1,
    'depois': 1,
    'atrás': -1,
    'atras': -1,
    'prévio': -1,
    'previo': -1
    'anterior': -1,
    'última': -1,
    'ultima': -1
    'próxima': 1,
    'proxima': 1
    'previous': -1,
    'fim da': 0,
    'fim de': 0,
    'fim do': 0
    'essa': 0,
    'esse': 0,
    'fdd': 1,
    'fdm': 1,
    'fda': 1,
}

dayOffsets = {
    'amanhã': 1,
    'amanha': 1
    'hoje': 0,
    'ontem': -1,
}

re_sources = {
    'meio-dia': {'hr': 12, 'mn': 0, 'sec': 0},
    'meio dia': {'hr': 12, 'mn': 0, 'sec': 0},
    'tarde': {'hr': 13, 'mn': 0, 'sec': 0},
    'almoço': {'hr': 12, 'mn': 0, 'sec': 0},
    'almoco': {'hr': 12, 'mn': 0, 'sec': 0},
    'manhã': {'hr': 6, 'mn': 0, 'sec': 0},
    'manha': {'hr': 6, 'mn': 0, 'sec': 0},
    'café da manhã': {'hr': 8, 'mn': 0, 'sec': 0},
    'cafe da manha': {'hr': 8, 'mn': 0, 'sec': 0},
    'jantar': {'hr': 19, 'mn': 0, 'sec': 0},
    'tarde': {'hr': 18, 'mn': 0, 'sec': 0},
    'meia-noite': {'hr': 0, 'mn': 0, 'sec': 0},
    'meia noite': {'hr': 0, 'mn': 0, 'sec': 0},
    'noite': {'hr': 21, 'mn': 0, 'sec': 0},
    'hoje a noite': {'hr': 21, 'mn': 0, 'sec': 0},
    'fdd': {'hr': 17, 'mn': 0, 'sec': 0},
    'fim do dia': {'hr': 17, 'mn': 0, 'sec': 0},
}

small = {
    'zero': 0,
    'um': 1,
    'uma': 1,
    'dois': 2,
    'três': 3,
    'tres': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'catorze': 14,
    'quatorze': 14
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezointo': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90
}

magnitude = {
    'mil': 1000,
    'milhão': 1000000,
    'milhao': 1000000,
    'bilhão': 1000000000,
    'bilhao': 1000000000,
    'trilhão': 1000000000000,
    'trilhao': 1000000000000,
    'quadrilhão': 1000000000000000,
    'quadrilhao': 1000000000000000,
    'quintilhão': 1000000000000000000,
    'quintilhao': 1000000000000000000,
    'sextilhão': 1000000000000000000000,
    'sextilhao': 1000000000000000000000,
    'septilhão': 1000000000000000000000000,
    'septilhao': 1000000000000000000000000,
    'octilhão': 1000000000000000000000000000,
    'octilhao': 1000000000000000000000000000,
    'nonilhão': 1000000000000000000000000000000,
    'nonilhao': 1000000000000000000000000000000,
    'decilhão': 1000000000000000000000000000000000,
    'decilhao': 1000000000000000000000000000000000,
}

ignore = ('e', ',', 'a partir de agora')
