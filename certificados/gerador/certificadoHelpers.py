from datetime import date, datetime
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import User

from .dadosCertificado import DadosCertificado
from .dadosCertificadoAssinatura import DadosCertificadoAssinatura
from .geradorCertificado import GeradorCertificado

from certificados.models import Certificado
from gestao_feira.models import Feira, Patrocinadores
from gestao_presenca.models import Atividade, Inscricao, Pessoa

# Lista dos meses em extenso
__mes_ext = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}

#
# Formatação de datas por extenso compreentidas em um periodo
#
def _dataExtensoPeriodo(data_inicio, data_fim):
    if (data_inicio == data_fim):
        return _dataExtenso(data_fim)
    elif (data_fim.year > data_inicio.year):
        return '{0} a {1}'.format(_dataExtenso(data_inicio), _dataExtenso(data_fim))
    elif (data_fim.month > data_inicio.month):
        return '{0} de {1} a {2}'.format(data_inicio.day, __mes_ext[data_inicio.month], _dataExtenso(data_fim))
    else:
        return '{0} a {1}'.format(data_inicio.day, _dataExtenso(data_fim))

#
# Formatação de data por extenso
#
def _dataExtenso(data):
    return '{0} de {1} de {2}'.format(data.day, __mes_ext[data.month], data.year)

#def makeDadosCertificado(listModelCertificado=None):

#
# Cria objeto com os dados Dados do Certificado a partir das informações de entrada
#
def makeDadosCertificado(objModelUser=None,
                         objModelPessoa=None,
                         objModelCertificado=None,
                         objModelFeira=None,
                         lstModelAtividades=None,
                         lstModelPatrocinadores=None):
    dadosCert = DadosCertificado()

    if (objModelUser is not None):
        if (type(objModelUser) is not SimpleLazyObject):
            raise TypeError("O parâmetro 'objModelUser' deve obrigatóriamente ser um objeto do tipo 'SimpleLazyObject'!")
        else:
            dadosCert.nome = objModelUser.get_full_name()

    if (objModelPessoa is not None):
        if (type(objModelPessoa) is not Pessoa):
            raise TypeError("O parâmetro 'objModelPessoa' deve obrigatóriamente ser um objeto do tipo modelo de 'Pessoa'!")
        else:
            dadosCert.dataNascimento = _dataExtenso(objModelPessoa.data_nascimento)
            dadosCert.naturalidadeUF = objModelPessoa.nacionalidade
            dadosCert.rg = objModelPessoa.rg

    if (objModelCertificado is not None):
        if (type(objModelCertificado) is not Certificado):
            raise TypeError("O parâmetro 'objModelCertificado' deve obrigatóriamente ser um objeto do tipo modelo de 'Certificado'!")
        else:
            dadosCert.ptext = objModelCertificado.ptext
            dadosCert.imagem_fundo = objModelCertificado.imagem_fundo.path
            dadosCert.imagem_evento = objModelCertificado.imagem_evento.path

    if (objModelFeira is not None):
        if (type(objModelFeira) is not Feira):
            raise TypeError("O parâmetro 'objModelFeira' deve obrigatóriamente ser um objeto do tipo modelo de 'Feira'!")
        else:
            dadosCert.nome_evento = objModelFeira.nome_feira
            dadosCert.uf_evento = '{0}/{1}'.format(objModelFeira.cidade, objModelFeira.uf)
            dadosCert.local_data_emissao = '{0}, {1}.'.format(objModelFeira.cidade, _dataExtenso(objModelFeira.data_fim))
            dadosCert.data_evento = _dataExtensoPeriodo(objModelFeira.data_inicio, objModelFeira.data_fim)

    if (lstModelAtividades is not None):
        if (type(lstModelAtividades) is not list):
            raise TypeError("O parâmetro 'lstModelAtividades' deve obrigatóriamente ser uma lista!")
        else:
            for atividade in lstModelAtividades:
                if (type(atividade) is not Atividade):
                    raise TypeError("O parâmetro 'lstModelAtividades' deve obrigatóriamente ser composto por objetos do tipo modelo de 'Atividade'!")
                else:
                    dadosCert.lista_atividades.append([atividade.titulo, atividade.carga_horaria])

    if (lstModelPatrocinadores is not None):
        if (type(lstModelPatrocinadores) is not list):
            raise TypeError("O parâmetro 'lstModelPatrocinadores' deve obrigatóriamente ser uma lista!")
        else:
            for patrocinador in lstModelPatrocinadores:
                if (type(patrocinador) is not Patrocinadores):
                    raise TypeError("O parâmetro 'lstModelPatrocinadores' deve obrigatóriamente ser composto por objetos do tipo modelo de 'Patrocinadores'!")
                else:
                    dadosCert.lista_imgs_organizadores.append(patrocinador.imagem_fundo.path)

    return dadosCert

#
# Cria um objeto do tipo certificado a partir das informações de entrada
#
def makeCertificado(objModelUser=None,
                    objModelPessoa=None,
                    objModelCertificado=None,
                    objModelFeira=None,
                    lstModelAtividades=None,
                    lstModelPatrocinadores=None):
    dadosCert = makeDadosCertificado(objModelUser, objModelPessoa, objModelCertificado, objModelFeira, lstModelAtividades, lstModelPatrocinadores)
    return GeradorCertificado(dadosCert)

#
# Cria um buffer tipo arquivo com os dados do PDF do certificado.
#
def makeCertificadoBytesIO(objModelUser=None,
                           objModelPessoa=None,
                           objModelCertificado=None,
                           objModelFeira=None,
                           lstModelAtividades=None,
                           lstModelPatrocinadores=None):
    certificado = makeCertificado(objModelUser, objModelPessoa, objModelCertificado, objModelFeira, lstModelAtividades, lstModelPatrocinadores)
    return certificado.getCertificado()
