# Política de Segurança da Informação e Gestão de Credenciais

Projeto de portfólio em **GRC**: uma Política de Segurança da Informação (PSI) completa para uma clínica **fictícia**, com política de senhas alinhada às boas práticas atuais, aspectos da **LGPD** e **rastreabilidade** com uma matriz de riscos e com a ISO/IEC 27001:2022.

> Documento fictício, criado para fins de estudo. Nenhuma informação refere-se a uma organização real.

## Visão geral

| Item | Descrição |
| :--- | :--- |
| Organização | Clínica Viver Bem (fictícia) |
| Documento | [`PSI_Clinica_Viver_Bem_v1.1.md`](PSI_Clinica_Viver_Bem_v1.1.md) |
| Versão | 1.1 (revisão de 08/10/2026) |
| Foco | Proteção de dados de saúde (LGPD), controle de acesso, senhas e MFA, incidentes e terceiros |

## Conteúdo da política

1. Introdução e objetivo
2. Escopo
3. Papéis e responsabilidades (Direção, TI, GRC, **DPO**, colaboradores)
4. Diretrizes gerais
   - Classificação da informação
   - Controle de acesso e gestão de ativos
   - Uso aceitável
   - Criptografia e proteção de dados
   - Segurança de rede e disponibilidade
   - Backup e continuidade
   - Gestão de vulnerabilidades
   - Desenvolvimento seguro e segredos
   - Descarte seguro
   - Terceiros e fornecedores
   - Gestão de incidentes
5. **Política de senhas e autenticação (MFA)**
6. Exceções
7. Conformidade e sanções
8. Revisão e vigência
9. **Rastreabilidade** (política × riscos × controles ISO 27001)
10. Histórico de revisões

## Decisões de projeto

- **Senhas alinhadas ao NIST SP 800-63B:** comprimento mínimo (12 caracteres, 14 para contas administrativas), verificação contra senhas fracas e vazadas, **sem troca periódica obrigatória** e **sem regras forçadas de composição**. A troca é obrigatória quando há suspeita de comprometimento. Esse modelo substitui o clássico "trocar a cada 90 dias com símbolos e números", que tende a gerar senhas previsíveis.
- **MFA obrigatório** para acesso remoto, prontuário eletrônico, e-mail, sistemas financeiros e todas as contas administrativas.
- **Segregação de funções:** quem implementa o controle (TI) é distinto de quem o audita (GRC).
- **LGPD:** inclui o encarregado (DPO) e a comunicação de incidentes à ANPD quando houver risco relevante aos titulares.
- **Classificação da informação** em quatro níveis, com prontuários e dados de pacientes tratados como **Restritos**.

## Rastreabilidade

A seção 9 da política relaciona cada diretriz aos **10 riscos** da matriz de riscos do projeto e aos controles do **Anexo A da ISO/IEC 27001:2022**. Exemplos:

| Seção da PSI | Risco | Controles Anexo A |
| :--- | :--- | :--- |
| 4.6 Backup e continuidade | R-02 | A.8.13, A.5.30 |
| 4.7 Gestão de vulnerabilidades | R-05 | A.8.8 |
| 5. Senhas e MFA | R-04, R-01 | A.5.17, A.8.5, A.8.2 |

Tabela completa na seção 9 do documento.

## Premissas e limitações

- Prazos e periodicidades (ex.: correção de vulnerabilidades críticas em 7 dias, testes de restauração a cada 6 meses) são **valores fictícios**, definidos para fins de exemplo.
- O prazo de comunicação de incidentes à ANPD (3 dias úteis) deve ser **confirmado na regulamentação vigente** a cada revisão.
- Não substitui uma política elaborada com a participação da área jurídica, do DPO e da direção de uma organização real.
- As referências ao Anexo A seguem a numeração da ISO/IEC 27001:2022.

## Projetos relacionados
- [Matriz de Riscos de Segurança da Informação](https://github.com/thlozz/matriz-riscos-grc): os 10 riscos que esta política trata, com risco inerente, residual e mapa de calor.
- [Analisador de Logs de Segurança](https://github.com/thlozz/log-analyzer-soc): ferramenta de apoio à detecção de ataques de força bruta, relacionada ao bloqueio de conta da seção 5.3.

## Referências
- ISO/IEC 27001:2022, Anexo A
- NIST SP 800-63B (Digital Identity Guidelines)
- Lei Geral de Proteção de Dados (Lei nº 13.709/2018)
