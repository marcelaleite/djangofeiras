"""
Classe para armazenamento dos Dados de Certificado

 Esta classe armazena e valida os dados que serão inseridos
no certificado.

 Os dados podem ser carregados através do construtor, ou
inseridos/alterados individualmente através das propriedades.

TODO: adicionar comentários/descrições nos métodos e propriedades
"""

from .dadosCertificadoAssinatura import DadosCertificadoAssinatura

class DadosCertificado:
    def __init__(self,
                 nome=None,
                 data_nasc=None,
                 natur_uf=None,
                 rg=None,
                 nome_trabalho=None,
                 premiacao=None,
                 nome_evento=None,
                 uf_evento=None,
                 data_evento=None,
                 local_data_emissao=None,
                 lista_assinaturas=None,
                 lista_atividades=None,
                 imagem_fundo=None,
                 imagem_evento=None,
                 lista_imgs_organizadores=None,
                 autenticidade=None,
                 ptext=None):
        self.nome = nome
        self.dataNascimento = data_nasc
        self.naturalidadeUF = natur_uf
        self.rg = rg
        self.nome_trabalho = nome_trabalho
        self.premiacao = premiacao
        self.nome_evento = nome_evento
        self.uf_evento = uf_evento
        self.data_evento = data_evento
        self.local_data_emissao = local_data_emissao
        self.lista_assinaturas = lista_assinaturas
        self.lista_atividades = lista_atividades
        self.imagem_fundo = imagem_fundo
        self.imagem_evento = imagem_evento
        self.lista_imgs_organizadores = lista_imgs_organizadores
        self.autenticidade = autenticidade
        self.ptext = ptext

    def _getNome(self):
        return self.__nome

    def _setNome(self, nome):
        if (nome is not None):
            self.__nome = nome
        else:
            self.__nome = "\u00abNOME\u00bb"

    nome = property(fget=_getNome, fset=_setNome)

    def _getDataNascimento(self):
        return self.__dataNascimento

    def _setDataNascimento(self, dataNascimento):
        if (dataNascimento is not None):
            self.__dataNascimento = dataNascimento
        else:
            self.__dataNascimento = "\u00abDATA_NASC\u00bb"

    dataNascimento = property(fget=_getDataNascimento, fset=_setDataNascimento)

    def _getNaturalidadeUF(self):
        return self.__naturalidadeUF

    def _setNaturalidadeUF(self, uf):
        if (uf is not None):
            self.__naturalidadeUF = uf
        else:
            self.__naturalidadeUF = "\u00abNATURALIDADE UF\u00bb"

    naturalidadeUF = property(fget=_getNaturalidadeUF, fset=_setNaturalidadeUF)

    def _getRG(self):
        return self.__rg

    def _setRG(self, rg):
        if (rg is not None):
            self.__rg = rg
        else:
            self.__rg = "\u00abRG\u00bb"

    rg = property(fget=_getRG, fset=_setRG)

    def _getNomeTrabalho(self):
        return self.__nome_trabalho

    def _setNomeTrabalho(self, nome_trabalho):
        if (nome_trabalho is not None):
            self.__nome_trabalho = nome_trabalho
        else:
            self.__nome_trabalho = "\u00abNOME DO TRABALHO\u00bb"

    nome_trabalho = property(fget=_getNomeTrabalho, fset=_setNomeTrabalho)

    def _getPremiacao(self):
        return self.__premiacao

    def _setPremiacao(self, premiacao):
        if (premiacao is not None):
            self.__premiacao = premiacao
        else:
            self.__premiacao = "\u00abPREMIAÇÃO\u00bb"

    premiacao = property(fget=_getPremiacao, fset=_setPremiacao)

    def _getNomeEvento(self):
        return self.__nome_evento

    def _setNomeEvento(self, nome_evento):
        if (nome_evento is not None):
            self.__nome_evento = nome_evento
        else:
            self.__nome_evento = "\u00abNOME EVENTO\u00bb"

    nome_evento = property(fget=_getNomeEvento, fset=_setNomeEvento)

    def _get_uf_evento(self):
        return self.__uf_evento

    def _set_uf_evento(self, uf_evento):
        if (uf_evento is not None):
            self.__uf_evento = uf_evento
        else:
            self.__uf_evento = "\u00abUF EVENTO\u00bb"

    uf_evento = property(fget=_get_uf_evento, fset=_set_uf_evento)

    def _getDataEvento(self):
        return self.__data_evento

    def _setDataEvento(self, data_evento):
        if (data_evento is not None):
            self.__data_evento = data_evento
        else:
            self.__data_evento = "\u00abDATA/PERIODO EVENTO\u00bb"

    data_evento = property(fget=_getDataEvento, fset=_setDataEvento)

    def _getLocalDataEmissao(self):
        return self.__local_data_emissao

    def _setLocalDataEmissao(self, local_data_emissao):
        if (local_data_emissao is not None):
            self.__local_data_emissao = local_data_emissao
        else:
            self.__local_data_emissao = "\u00abLOCAL E DATA EVENTO\u00bb"

    local_data_emissao = property(fget=_getLocalDataEmissao, fset=_setLocalDataEmissao)

    def _get_lista_assinaturas(self):
        return self.__lista_assinaturas

    def _set_lista_assinaturas(self, lst_ass):
        if (lst_ass is not None):
            if (type(lst_ass) is list):
                for assinatura in lst_ass:
                    if (type(assinatura) is not DadosCertificadoAssinatura):
                        raise TypeError("A lista de assinaturas contém objetos inválidos")

                self.__lista_assinaturas = lst_ass
            else:
                raise TypeError("A lista de assinaturas deve ser do tipo 'list'")
        else:
            self.__lista_assinaturas = []

    lista_assinaturas = property(fget=_get_lista_assinaturas, fset=_set_lista_assinaturas)

    def _getListaAtividades(self):
        return self.__lista_atividades

    def _setListaAtividades(self, lista_atividades):
        if (lista_atividades is not None):
            if (type(lista_atividades) is list):
                self.__lista_atividades = lista_atividades
            else:
                raise TypeError("A lista de atividades deve ser do tipo 'list'")
        else:
            self.__lista_atividades = []

    lista_atividades = property(fget=_getListaAtividades, fset=_setListaAtividades)

    def _getImagemFundo(self):
        return self.__imagem_fundo

    def _setImagemFundo(self, imagem_fundo):
        self.__imagem_fundo = imagem_fundo

    imagem_fundo = property(fget=_getImagemFundo, fset=_setImagemFundo)

    def _getImagemEvento(self):
        return self.__imagem_evento

    def _setImagemEvento(self, imagem_evento):
        self.__imagem_evento = imagem_evento

    imagem_evento = property(fget=_getImagemEvento, fset=_setImagemEvento)

    def _get_lista_imgs_organizadores(self):
        return self.__lista_imgs_organizadores

    def _set_lista_imgs_organizadores(self, lst_imgs_org):
        if (lst_imgs_org is not None):
            if (type(lst_imgs_org) is list):
                self.__lista_imgs_organizadores = lst_imgs_org
            else:
                raise TypeError("A lista de imagens dos organizadores deve ser do tipo 'list'")
        else:
            self.__lista_imgs_organizadores = []

    lista_imgs_organizadores = property(fget=_get_lista_imgs_organizadores, fset=_set_lista_imgs_organizadores)

    def _getAutenticidade(self):
        return self.__autenticidade

    def _setAutenticidade(self, autenticidade):
        if (autenticidade is not None):
            self.__autenticidade = autenticidade
        else:
            self.__autenticidade = "\u00abAUTENTICIDADE\u00bb"

    autenticidade = property(fget=_getAutenticidade, fset=_setAutenticidade)

    def _getPText(self):
        return self.__ptext

    def _setPText(self, ptext):
        if (ptext is not None):
            self.__ptext = ptext
        else:
            self.__ptext = "\u00abPARAGRAFO DE DESCRIÇÃO\u00bb"

    ptext = property(fget=_getPText, fset=_setPText)

    #
    # Obtém o paragrafo de descrição do certificado com os dados inseridos.
    #
    def get_ptext_com_dados(self):
        tokens = ["<NOME>", "<DATA_NASC>", "<NATURALIDADE_UF>", "<RG>", "<NOME_TRABALHO>", "<PREMIACAO>", "<NOME_EVENTO>", "<UF_EVENTO>", "<DATA_PERIODO_EVENTO>", "<CARGA_HORARIA>", "<>"]
        ptext = self.ptext

        for token in tokens:
            if (ptext.find(token) >= 0):
                if (token == "<NOME>"):
                    ptext = ptext.replace("<NOME>", self.nome)
                elif (token == "<DATA_NASC>"):
                    ptext = ptext.replace("<DATA_NASC>", self.dataNascimento)
                elif (token == "<NATURALIDADE_UF>"):
                    ptext = ptext.replace("<NATURALIDADE_UF>", self.naturalidadeUF)
                elif (token == "<RG>"):
                    ptext = ptext.replace("<RG>", self.rg)
                elif (token == "<NOME_TRABALHO>"):
                    ptext = ptext.replace("<NOME_TRABALHO>", self.nome_trabalho)
                elif (token == "<PREMIACAO>"):
                    ptext = ptext.replace("<PREMIACAO>", self.premiacao)
                elif (token == "<NOME_EVENTO>"):
                    ptext = ptext.replace("<NOME_EVENTO>", self.nome_evento)
                elif (token == "<UF_EVENTO>"):
                    ptext = ptext.replace("<UF_EVENTO>", self.uf_evento)
                elif (token == "<DATA_PERIODO_EVENTO>"):
                    ptext = ptext.replace("<DATA_PERIODO_EVENTO>", self.data_evento)
                elif (token == "<CARGA_HORARIA>"):
                    ptext = ptext.replace("<CARGA_HORARIA>", str(self.getCargaHorariaTotal()))

        return ptext

    #
    # Obtém o paragrafo de descrição do certificado com os dados inseridos e com os tags de marcação XML para paragrafo.
    #
    def get_ptext_com_dados_xml(self):
        return '<font name="Times-Roman" size=16>%s</font>' % (self.get_ptext_com_dados())

    #
    # Obtém a soma das cargas horárias das atividades exercidas
    #
    def getCargaHorariaTotal(self):
        if (self.lista_atividades is None):
            return 0

        total_horas = 0
        for atividade in self.lista_atividades:
            if (type(atividade) is list):
                if (len(atividade) == 2):
                    total_horas = total_horas + atividade[1]

        return total_horas
