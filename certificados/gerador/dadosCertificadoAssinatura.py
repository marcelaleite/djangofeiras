"""
Classe para armazenamento dos Dados das Assinaturas no Certificado

 Esta classe armazena e valida os dados de assinatura que
serão inseridos no certificado.

 Os dados podem ser carregados através do construtor, ou
inseridos/alterados individualmente através das propriedades.

TODO: adicionar comentários/descrições nos métodos e propriedades
"""

class DadosCertificadoAssinatura:
    def __init__(self,
                 nome=None,
                 cargo=None,
                 instituicao=None,
                 imagem_assinatura=None):
        self.nome = nome
        self.cargo = cargo
        self.instituicao = instituicao
        self.imagem_assinatura = imagem_assinatura

    def _getNome(self):
        return self.__nome

    def _setNome(self, nome):
        if (nome is not None):
            self.__nome = nome
        else:
            self.__nome = "\u00abNOME\u00bb"

    nome = property(fget=_getNome, fset=_setNome)

    def _get_cargo(self):
        return self.__cargo

    def _set_cargo(self, cargo):
        if (cargo is not None):
            self.__cargo = cargo
        else:
            self.__cargo = "\u00abCARGO\u00bb"

    cargo = property(fget=_get_cargo, fset=_set_cargo)

    def _get_instituicao(self):
        return self.__instituicao

    def _set_instituicao(self, instituicao):
        if (instituicao is not None):
            self.__instituicao = instituicao
        else:
            self.__instituicao = "\u00abINSTITUIÇÃO\u00bb"

    instituicao = property(fget=_get_instituicao, fset=_set_instituicao)

    def _get_imagem_assinatura(self):
        return self.__imagem_assinatura

    def _set_imagem_assinatura(self, img_ass):
        self.__imagem_assinatura = img_ass

    imagem_assinatura = property(fget=_get_imagem_assinatura, fset=_set_imagem_assinatura)
