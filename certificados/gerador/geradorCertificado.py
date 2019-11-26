"""
Classe Geradora de Certificados

 Esta classe é responsável por gerar o certificado,
utilizando as informaçãoes recebidas através da classe de
armazenamento 'dadosCertificado', onde os dados estarão
validados e normatizados.

 Os dados podem ser carregados através do construtor, ou
inseridos/alterados individualmente através da propriedade.

TODO: adicionar comentários/descrições nos métodos e propriedades
"""

import io
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

from .dadosCertificado import DadosCertificado

class GeradorCertificado:
    def __init__(self,
                 dadosCertificado=None):
        self.dadosCertificado = dadosCertificado

    def _getDadosCertificado(self):
        return self.__dadosCertificado

    def _setDadosCertificado(self, dadosCertificado):
        if (dadosCertificado is not None):
            self.__dadosCertificado = dadosCertificado
        else:
            self.__dadosCertificado = DadosCertificado()

    dadosCertificado = property(fget=_getDadosCertificado, fset=_setDadosCertificado)

    #
    # Obtém o certificado em forma de dados
    # ATENÇÃO: Todas as informações devem estar pré-carregadas
    #
    def getCertificado(self, pageSize=landscape(A4)):
        # Obtém o paragrafo de descrição do certificado
        ptext = self.dadosCertificado.get_ptext_com_dados_xml()

        return self._getCertificado(pageSize, ptext)

    #
    # Obtém o certificado em forma de dados
    #
    def _getCertificado(self,
                        pageSize,
                        pText = '<font name="Times-Roman" size=16>\u00abPARAGRAFO DE DESCRIÇÃO\u00ab</font>'):

        if (type(pageSize) is not tuple):
            raise TypeError("O parâmetro 'pageSize' deve ser do tipo 'tuple'.")

        # Definição de estilos para utilização em parágrafos
        styleSheet = getSampleStyleSheet()
        styleSheet.add(ParagraphStyle(name='Left', alignment=TA_LEFT, leading=22))
        styleSheet.add(ParagraphStyle(name='Center', alignment=TA_CENTER, leading=22))
        styleSheet.add(ParagraphStyle(name='Right', alignment=TA_RIGHT, leading=22))
        styleSheet.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, leading=22))
        styleSheet.add(ParagraphStyle(name='Center-Single', alignment=TA_CENTER))
        styleSheet.add(ParagraphStyle(name='Right-Single', alignment=TA_RIGHT))

        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        cnv = canvas.Canvas(buffer, pagesize=pageSize)

        self._makeFrente(cnv, pageSize, styleSheet, pText)
        self._makeVerso(cnv, pageSize, styleSheet)

        return buffer

    #
    # Criação da página para a frente do certificado
    #
    def _makeFrente(self, cnv, pageSize, styleSheet, pText):
        dadosCert = self.dadosCertificado

        width, height = pageSize  #keep for later

        # Inserção da imagem de fundo do certificado
        if (dadosCert.imagem_fundo is not None):
            cnv.drawImage(dadosCert.imagem_fundo, 0, 0, width, height)

        # Inserção da imagem de logo do evento no certificado
        if (dadosCert.imagem_evento is not None):
            #x = (width / 2) - 125 # Centraliza a imagem horizontalmente
            #cnv.drawImage(dadosCert.imagem_evento, x, 390, 270, 100)
            self._insere_imagem_evento(dadosCert.imagem_evento, width, cnv, styleSheet)

        # Define a fonte e escreve o título
        cnv.setFillColor(colors.white)
        cnv.setStrokeColor(colors.white)
        cnv.setFont("Helvetica-Bold", 64)
        cnv.drawString(255, 525, "Certificado")

        # Escreve a descrição no certificado
        self._insere_descricao(pText, width, cnv, styleSheet)

        # Escreve o local e data da emissão do certificado
        if (dadosCert.local_data_emissao is not None):
            self._insere_local_data_emissao(dadosCert.local_data_emissao, width, cnv, styleSheet)

        # Se existir organizadores, insere-os no certificado
        if (len(dadosCert.lista_imgs_organizadores) > 0):
            self._insere_tabela_organizadores(cnv, styleSheet)

        # Se existir assinaturas, insere-as no certificado
        if (len(dadosCert.lista_imgs_organizadores) > 0):
            self._insere_assinaturas(cnv, styleSheet)

        # Insere a autenticidade do certificado
        if (dadosCert.autenticidade is not None):
            self._insere_autenticador(dadosCert.autenticidade, width, cnv, styleSheet)

        # Cria uma nova página
        cnv.showPage()

    #
    # Criação da página para o verso do certificado
    #
    def _makeVerso(self, cnv, pageSize, styleSheet):
        atividades = self.dadosCertificado.lista_atividades

        width, height = pageSize  #keep for later

        # Prepara os dados fixos que serão inseridos na tabela
        p00 = Paragraph('<font name="Times-Roman" size=16><b>ATIVIDADES DESENVOLVIDAS</b></font>', styleSheet["Center"])
        p01 = Paragraph('<font name="Times-Roman" size=16><b>CARGA HORÁRIA</b></font>', styleSheet["Center"])
        p20 = Paragraph('<font name="Times-Roman" size=16><b>CARGA HORÁRIA TOTAL</b></font>', styleSheet["Left"])

        # Adiciona os títulos das colunas na lista da tabela
        data = [[p00, p01]]

        # Adiciona os dados das atividades em uma lista de atividades
        total_horas = 0
        atividade_id = 1
        atividades_lista = []
        for atividade in atividades:
            if (type(atividade) is list):
                if (len(atividade) == 2):
                    p10 = Paragraph('<font name="Times-Roman" size=14>   %s. %s</font>' % (atividade_id, atividade[0]), styleSheet["Left"])
                    p11 = Paragraph('<font name="Times-Roman" size=14>%s h</font>' % (atividade[1]), styleSheet["Center"])
                    atividades_lista.append([p10, p11])
                    atividade_id = atividade_id + 1
                    total_horas = total_horas + atividade[1]

        # Memoriza a quantidade de linhas de dados das atividades que serão inseridas na tabela (minímo 1 linha)
        atividades_lista_linhas = len(atividades_lista)
        if (atividades_lista_linhas == 0):
            p10 = Paragraph('<font name="Times-Roman" size=14>1.</font>', styleSheet["Left"])
            atividades_lista.append([p10, '0 h'])
            atividades_lista_linhas = 1

        # Cria a lista de altura das linhas da tabela
        tabela_alturas_linhas = atividades_lista_linhas*[0.3*inch]   # Altura linhas dos dados de atividades
        tabela_alturas_linhas.insert(0, 0.35*inch)   # Altura linha do cabeçalho da tabela
        tabela_alturas_linhas.append(0.35*inch)   # Altura linha do rodapé da tablela

        # Adiciona as atividades na lista da tabela
        for atividade_lista in atividades_lista:
            data.append(atividade_lista)

        # Adiciona o rodapé da tabela à lista da tabela
        p21 = Paragraph('<font name="Times-Roman" size=16><b>%s h</b></font>' % (total_horas), styleSheet["Center"])
        data.append([p20, p21])

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t = Table(data, [5.5*inch, 2.4*inch], tabela_alturas_linhas)

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                               ('ALIGN',(0,1),(-2,-1),'LEFT'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               ('LINEABOVE',(0,2),(-1,-2),0.25,colors.lightgrey),
                               ('INNERGRID', (0,0), (-1,1), 0.25, colors.black),
                               ('INNERGRID', (0,-2), (-1,-1), 0.25, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Cálcula a posição da tabela de acordo com a quantidade de dados
        x = (width - tW) / 2  # Centralizado horizontalmente
        y = height - tH - 125

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, x, y)

        # Salva o arquivo
        cnv.showPage()
        cnv.save()

    #
    # Insere o local e data de emissão como sendo uma célula de tabela
    #
    def _insere_imagem_evento(self, imagem_evento, width, cnv, styleSheet):
        # Dimensões máximas para a imagem
        hMax = 100
        wMax = 270

        # Carrega a imagem
        i00 = Image(imagem_evento)

        # Testa e redimensiona a imagem conforme necessidade
        if (i00.drawHeight > hMax):
            i00.drawWidth = hMax * (i00.drawWidth/i00.drawHeight)
            i00.drawHeight = hMax

        if (i00.drawWidth > wMax):
            i00.drawHeight = wMax * (i00.drawHeight/i00.drawWidth)
            i00.drawWidth = wMax

        # Adiciona a imagem à lista da tabela
        data = [[i00]]

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t=Table(data, [wMax], [hMax])

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                               ('LEFTPADDING',(0,0),(-1,-1),0),
                               ('RIGHTPADDING',(0,0),(-1,-1),0),
                               ('BOTTOMPADDING',(0,0),(-1,-1),0),
                               ('TOPPADDING',(0,0),(-1,-1),0),
                               #('BOX', (0,0), (-1,-1), 0.25, colors.black), #Descomentar para visualizar caixa
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Centraliza a imagem horizontalmente
        x = (width - tW) / 2

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, x, 390)

    #
    # Insere a descrição como sendo uma célula de tabela
    #
    def _insere_descricao(self, pText, width, cnv, styleSheet):
        # Cria um paragráfo
        p00 = Paragraph(pText, styleSheet["Justify"])

        # Adiciona p parágrafo na lista da tabela
        data = [[p00]]

        # Available width and height
        aW = width - 80
        aH = 140

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t=Table(data, [aW], [aH])

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                               #('BOX', (0,0), (-1,-1), 0.25, colors.black), #Descomentar para visualizar caixa
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Centraliza horizontalmente a tabela
        x = (width - tW) / 2

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, x, 240)

    #
    # Insere o local e data de emissão como sendo uma célula de tabela
    #
    def _insere_local_data_emissao(self, local_data_emissao, width, cnv, styleSheet):
        # Cria um paragráfo
        p00 = Paragraph('<font name="Times-Roman" size=16>%s</font>' % (local_data_emissao), styleSheet["Right-Single"])

        # Adiciona p parágrafo na lista da tabela
        data = [[p00]]

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t=Table(data, [5.5*inch], [0.2*inch])

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                               ('TOPPADDING',(0,0),(-1,-1),-6),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               #('BOX', (0,0), (-1,-1), 0.25, colors.black), #Descomentar para visualizar caixa
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Posição Horizontal da tabela
        x = width - tW - 50

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, x, 215)

    #
    # Insere as tabelas com as assinaturas
    #
    def _insere_assinaturas(self, cnv, styleSheet):
        assinaturas = self.dadosCertificado.lista_assinaturas

        if (len(assinaturas) > 0):
            self._insere_assinatura(assinaturas[0], 85, 140, cnv, styleSheet)

        if (len(assinaturas) > 1):
            self._insere_assinatura(assinaturas[1], 350, 140, cnv, styleSheet)

    #
    # Insere a tabela com a assinatura na posição especificada
    #
    def _insere_assinatura(self, assinatura, x, y, cnv, styleSheet):
        # Dimensões máximas para as assinaturas
        hMax = 1.2*inch
        wMax = 3.1*inch

        # Carrega a imagem
        i00 = Image(assinatura.imagem_assinatura)

        # Testa e redimensiona a imagem conforme necessidade
        if (i00.drawHeight > hMax):
            i00.drawWidth = hMax * (i00.drawWidth/i00.drawHeight)
            i00.drawHeight = hMax

        if (i00.drawWidth > wMax):
            i00.drawHeight = wMax * (i00.drawHeight/i00.drawWidth)
            i00.drawWidth = wMax

        # Prepara o texto para a tabela
        p10 = Paragraph('<font name="Times-Roman" size=12><b>%s</b></font>' % (assinatura.nome), styleSheet["Center-Single"])
        p20 = Paragraph('<font name="Times-Roman" size=12>%s</font>' % (assinatura.cargo), styleSheet["Center-Single"])
        p30 = Paragraph('<font name="Times-Roman" size=12>%s</font>' % (assinatura.instituicao), styleSheet["Center-Single"])

        # Adiciona os dados à lista da tabela
        data= [[i00], [p10], [p20], [p30]]

        # Cria lista da altura das linhas da tabela
        rows_height = 3*[0.18*inch]
        rows_height.insert(0, 1.2*inch) # Altura célula imagem

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t=Table(data, [3.52*inch], rows_height)

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                               ('VALIGN',(0,0),(-1,0),'BOTTOM'),
                               ('VALIGN',(1,0),(-1,-1),'MIDDLE'),
                               ('BOTTOMPADDING',(0,0),(-1,0),-2),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), #Descomentar para visualizar grade
                               #('BOX', (0,0), (-1,-1), 0.25, colors.black),       #
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, x, y) # Localização da tabela

    #
    # Insere a tabela com as imagens dos organizadores
    #
    def _insere_tabela_organizadores(self, cnv, styleSheet):
        imgs_organizadores = self.dadosCertificado.lista_imgs_organizadores

        # Paragrafo para a primeira célula da tabela
        p00 = Paragraph('<font name="Times-Roman" size=16><b>Organização:</b></font>', styleSheet["Left"])

        # Adiciona os títulos das colunas na lista da tabela
        data = [[p00]]

        # Adiciona as imagens dos organizadores em uma lista
        #imgs_lista = []
        tabela_largura_colunas = [1.5*inch]
        for img_organizador in imgs_organizadores:
            # Carrega e redimenciona a imagem
            img = Image(img_organizador)
            if (img.drawHeight < img.drawWidth):
                img.drawHeight = 1.05*inch * (img.drawHeight/img.drawWidth)
                img.drawWidth = 1.05*inch
            else:
                img.drawWidth = 1.05*inch * (img.drawWidth/img.drawHeight)
                img.drawHeight = 1.05*inch

            # Adiciona a imagem a tabela
            #imgs_lista.append(img)
            data[0].append(img)

            # Adiciona à lista de largura das colunas da tabela
            if (len(data[0]) <= 5):
                tabela_largura_colunas.append(1.15*inch)
            else:
                tabela_largura_colunas.append(1.5*inch)

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t = Table(data, tabela_largura_colunas, [1.25*inch])

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                               ('VALIGN',(0,0),(-1,-1),'TOP'),
                               ('ALIGN',(1,0),(-1,-1),'CENTER'),
                               ('VALIGN',(1,0),(-1,-1),'MIDDLE'),
                               ('TOPPADDING',(0,0),(0,-1),10),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), #Descomentar para visualizar grade
                               #('BOX', (0,0), (-1,-1), 0.25, colors.black),
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, 35, 50) # Localização da tabela

    #
    # Insere a autenticidade do certificado como sendo uma célula de tabela
    #
    def _insere_autenticador(self, autenticidade, width, cnv, styleSheet):
        # Cria um paragráfo
        p00 = Paragraph('<font name="Times-Roman" size=10>%s</font>' % (autenticidade), styleSheet["Right-Single"])

        # Adiciona p parágrafo na lista da tabela
        data = [[p00]]

        # Cria a tabela com os dados e parametriza as dimensões da grade
        t=Table(data, [10.5*inch], [0.15*inch])

        # Configura alguns estilos na tabela
        t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'RIGHT'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                               ('BOTTOMPADDING',(0,0),(-1,-1),-6),
                               ('TOPPADDING',(0,0),(-1,-1),-6),
                               ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                               #('BOX', (0,0), (-1,-1), 0.25, colors.black), #Descomentar para visualizar caixa
                               ]))

        # Obtém a altura e largura da tabela
        tH = sum(t._argH)
        tW = sum(t._argW)

        # Posição Horizontal da tabela
        x = width - tW - 38

        # Insere a tabela ao PDF
        t.wrapOn(cnv, tW, tH)
        t.drawOn(cnv, x, 30)
