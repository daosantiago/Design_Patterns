# -*- coding: UTF-8 -*-

def imprime(nota_fiscal):
    print 'Nota fiscal %s' % (nota_fiscal.cnpj)

def envia_por_email(nota_fiscal):
     print  'Enviando nota %s por email' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
    print 'Salvando a nota %s no bando de dados' % (nota_fiscal.cnpj)