# Política de Segurança da Informação (PSI) e Gestão de Credenciais

**Empresa:** Clínica Viver Bem (fictícia)  
**Versão:** 1.1  
**Data da última revisão:** 08/10/2026  
**Próxima revisão prevista:** Outubro de 2027 (revisão anual)  
**Classificação:** Uso Interno  
**Aprovação:** Direção / Comitê de Segurança e Privacidade

> Documento fictício, criado para fins de estudo e portfólio. Nenhuma informação refere-se a uma organização real.

---

## 1. Introdução e Objetivo

A **Clínica Viver Bem** reconhece a informação, em especial os dados pessoais e os prontuários dos pacientes, como um de seus ativos mais valiosos.

O objetivo desta Política de Segurança da Informação (PSI) é estabelecer as diretrizes operacionais e administrativas para assegurar:

* **Confidencialidade:** o acesso à informação é restrito a pessoas autorizadas.
* **Integridade:** a informação e os métodos de processamento são exatos e protegidos contra alteração indevida.
* **Disponibilidade:** usuários autorizados têm acesso à informação e aos ativos quando necessário.

Esta política também apoia o cumprimento da Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018), em especial no tratamento de dados pessoais sensíveis de saúde.

---

## 2. Escopo

Esta política aplica-se a:

* Todos os colaboradores, médicos prestadores de serviço, estagiários, terceiros e fornecedores da Clínica Viver Bem.
* Todos os ativos de informação, sistemas corporativos, redes, prontuários eletrônicos (PEP), dispositivos móveis e a infraestrutura física e lógica da instituição.

---

## 3. Papéis e Responsabilidades

### 3.1. Direção / Comitê de Segurança e Privacidade
* Aprovar e revisar esta política, no mínimo uma vez por ano.
* Garantir os recursos necessários para a implementação dos controles.
* Decidir sobre exceções e sobre a aceitação formal de riscos (ver seção 6).

### 3.2. Responsável por TI (Administração de Sistemas)
* Implementar e manter os controles técnicos de segurança.
* Executar backups, aplicação de correções (patches) e gestão de acessos.

### 3.3. Responsável por GRC / Segurança da Informação
* Monitorar o cumprimento desta política e conduzir auditorias periódicas de acesso e de conformidade.
* Manter a matriz de riscos atualizada e promover campanhas de conscientização.
* **Segregação de funções:** quem implementa o controle (TI) não deve ser a mesma pessoa que o audita (GRC). Em estruturas pequenas em que isso não for possível, a limitação deve ser registrada como risco e a Direção deve fazer a revisão independente.

### 3.4. Encarregado pelo Tratamento de Dados Pessoais (DPO)
* Atuar como canal de comunicação entre a clínica, os titulares dos dados e a Autoridade Nacional de Proteção de Dados (ANPD), conforme a LGPD.
* Orientar colaboradores sobre boas práticas de proteção de dados e apoiar a resposta a incidentes que envolvam dados pessoais.

### 3.5. Colaboradores e Usuários das Redes e Sistemas
* Ler, compreender e cumprir esta PSI.
* Reportar imediatamente qualquer incidente ou suspeita de vulnerabilidade (ver 4.11).
* Proteger suas credenciais e as informações sob sua responsabilidade.

---

## 4. Diretrizes Gerais de Segurança da Informação

### 4.1. Classificação da Informação
Toda informação deve ser classificada pelo seu responsável em um dos níveis abaixo:

| Nível | Descrição | Exemplos |
| :--- | :--- | :--- |
| **Pública** | Pode ser divulgada sem prejuízo. | Site institucional, horários de atendimento. |
| **Uso Interno** | Destinada ao público interno; divulgação externa não autorizada causa dano limitado. | Procedimentos internos, escalas, esta PSI. |
| **Confidencial** | Dados cuja divulgação indevida causa dano relevante. | Contratos, informações financeiras, dados de colaboradores. |
| **Restrita** | Dados pessoais sensíveis e de saúde; exigem os controles mais fortes. | Prontuários, exames, laudos, dados de pacientes. |

Informações **Restritas** só podem ser armazenadas e transmitidas em sistemas homologados pela TI e com criptografia.

### 4.2. Controle de Acesso e Gestão de Ativos
* **Menor privilégio:** o acesso aos sistemas (ex.: PEP) é concedido estritamente conforme a necessidade da função (*need-to-know*).
* **Concessão e revogação:** o acesso deve ser solicitado e aprovado formalmente. Em caso de desligamento ou mudança de função, deve ser revogado ou ajustado imediatamente.
* **Revisão de acessos:** o Responsável por GRC revisa os acessos ao PEP e a sistemas críticos, no mínimo, a cada 6 meses.
* **Registro de acessos (logs):** acessos ao PEP devem ser registrados e passíveis de auditoria.
* **Contas administrativas:** devem ser nominais e separadas da conta de uso diário, com MFA obrigatório. O uso de contas administrativas genéricas ou compartilhadas é proibido.
* **Estações de trabalho:** o bloqueio automático de tela deve ser configurado por política para 5 minutos de inatividade. O usuário deve também bloquear manualmente a tela ao se ausentar (Win + L).
* **Inventário:** todo ativo corporativo (computadores, notebooks, celulares) deve constar em inventário com responsável definido.

### 4.3. Uso Aceitável dos Recursos Tecnológicos
* Os recursos de TI (computadores, e-mail corporativo, internet) destinam-se ao uso profissional.
* É proibido baixar, instalar ou usar software não homologado pela TI (*Shadow IT*).
* É vedado o envio de dados sensíveis de pacientes (prontuários, exames) por e-mail pessoal ou por aplicativos de mensagem não corporativos.

### 4.4. Criptografia e Proteção de Dados
* Todos os dispositivos móveis corporativos (notebooks, tablets, celulares) devem usar criptografia de disco total (ex.: BitLocker, FileVault) e permitir bloqueio e apagamento remoto (MDM).
* Dados em trânsito contendo informações de pacientes devem usar conexões criptografadas (HTTPS, TLS 1.2 ou superior).

### 4.5. Segurança de Rede e Disponibilidade
* A rede deve ser protegida por firewall, com segmentação entre a rede administrativa, a rede assistencial (PEP) e a rede de visitantes.
* Serviços expostos à internet devem contar com proteção contra negação de serviço (DDoS) e limitação de requisições (*rate limiting*), preferencialmente por serviço gerenciado.

### 4.6. Backup e Continuidade
* Dados críticos (incluindo o banco do PEP) devem seguir a regra **3-2-1**: 3 cópias, em 2 tipos de mídia, com 1 cópia fora do local.
* Os backups devem ser automáticos e monitorados.
* **Testes de restauração** devem ser realizados, no mínimo, a cada 6 meses e registrados.

### 4.7. Gestão de Vulnerabilidades e Atualizações
* Varreduras de vulnerabilidades devem ser executadas **quinzenalmente** nos servidores e serviços expostos.
* Prazos máximos para correção: vulnerabilidades **críticas em até 7 dias**; **altas em até 30 dias**. Prazos não cumpridos exigem justificativa e plano de mitigação.

### 4.8. Desenvolvimento Seguro e Gestão de Segredos
* É proibido armazenar senhas, chaves de API ou outros segredos no código-fonte ou em repositórios.
* Segredos devem ficar em cofre apropriado (*secret manager*), e os repositórios devem ter varredura automática de segredos (*secret scanning*).
* Sistemas desenvolvidos ou customizados devem seguir práticas de codificação segura (ex.: OWASP Top 10).

### 4.9. Descarte Seguro de Equipamentos e Mídias
* Equipamentos e mídias que armazenaram dados da clínica só podem ser descartados, doados ou reutilizados após sanitização ou destruição segura (referência: NIST SP 800-88).
* Cada descarte deve gerar registro ou laudo de sanitização.

### 4.10. Terceiros e Fornecedores
* Fornecedores com acesso a dados ou sistemas da clínica passam por avaliação de segurança e privacidade (*due diligence*) antes da contratação.
* Os contratos devem conter cláusulas de confidencialidade, proteção de dados (LGPD), notificação de incidentes e níveis de serviço (SLA).
* O desempenho e a conformidade do fornecedor devem ser revisados periodicamente.

### 4.11. Gestão de Incidentes de Segurança
* Qualquer anomalia, tentativa de acesso não autorizado, e-mail suspeito (*phishing*) ou perda de dispositivo deve ser reportado em até **2 horas** à equipe de TI/GRC.
* Todo incidente deve ser registrado, analisado e tratado, com lições aprendidas documentadas.
* Quando o incidente puder acarretar risco ou dano relevante aos titulares de dados pessoais, o **DPO** deve conduzir a comunicação à ANPD e aos titulares, conforme a LGPD (art. 48) e a regulamentação da ANPD em vigor. O prazo atualmente previsto é de **3 dias úteis**, e deve ser confirmado na regulamentação vigente a cada revisão desta política.

---

## 5. Política de Senhas e Autenticação

As credenciais de acesso são a primeira linha de defesa dos sistemas da clínica. As regras a seguir aplicam-se a todas as contas corporativas e administrativas e seguem as boas práticas atuais (referência: NIST SP 800-63B).

### 5.1. Criação de Senhas
* **Comprimento mínimo:** 12 caracteres para contas comuns e **14 caracteres para contas administrativas**. Recomenda-se o uso de *passphrases* (frases secretas longas e fáceis de lembrar).
* **Sem regras forçadas de composição:** não se exige mistura obrigatória de maiúsculas, números e símbolos, pois isso leva a senhas previsíveis. O tamanho e a imprevisibilidade são mais importantes.
* **Verificação de senhas fracas:** o sistema deve recusar senhas comuns, sequências (`123456`), palavras do dicionário, datas de nascimento, nomes da clínica ou do usuário e senhas já vazadas em incidentes públicos.
* **Unicidade:** a senha corporativa não pode ser reutilizada em serviços pessoais ou externos.

### 5.2. Autenticação Multifator (MFA)
O **MFA é obrigatório** para:
1. Acesso remoto (VPN ou portais web).
2. Acesso ao Prontuário Eletrônico do Paciente (PEP).
3. Contas de e-mail corporativo e sistemas financeiros.
4. **Todas as contas administrativas.**

### 5.3. Troca, Bloqueio e Comprometimento
* **Sem troca periódica obrigatória:** as senhas não expiram em intervalos fixos. A troca é obrigatória **imediatamente** quando houver suspeita ou confirmação de comprometimento, em caso de aparição em lista de vazamento ou após desligamento de quem conhecia a senha (ex.: contas compartilhadas de sistema).
* **Bloqueio de conta:** a conta será bloqueada temporariamente por 15 minutos após **5 tentativas incorretas** consecutivas.
* **Contas de serviço:** devem ter senhas longas e únicas, armazenadas em cofre e com responsável nominal.

### 5.4. Proteção e Armazenamento de Credenciais
* **Sigilo:** as senhas são pessoais e intransferíveis. É proibido compartilhá-las com colegas, superiores ou com o suporte técnico.
* **Sem anotações inseguras:** é proibido anotar senhas em papel, post-its, cadernos ou arquivos de texto sem criptografia.
* **Gerenciador de senhas:** o armazenamento de credenciais corporativas **deve** ser feito apenas em gerenciador de senhas homologado pela TI.

---

## 6. Exceções

* Qualquer exceção a esta política deve ser solicitada por escrito, com justificativa, risco associado, medidas compensatórias e prazo de validade.
* A exceção só é válida após aprovação da Direção e registro pelo Responsável por GRC, que deve revisá-la ao final do prazo.

---

## 7. Conformidade e Sanções Disciplinares

O descumprimento desta política constitui infração às diretrizes internas da **Clínica Viver Bem**. As violações estão sujeitas a medidas disciplinares, que variam de advertência por escrito à rescisão do contrato, sem prejuízo das responsabilidades civis e criminais cabíveis, incluindo as previstas na LGPD.

---

## 8. Revisão e Vigência

Esta política entra em vigor na data de sua aprovação e deve ser revisada **anualmente** ou sempre que ocorrerem mudanças relevantes (incidente significativo, mudança de sistemas, alteração legal ou regulatória).

---

## 9. Rastreabilidade: Política, Riscos e Controles

A tabela relaciona cada seção desta política aos riscos da **Matriz de Riscos** do projeto (arquivo `matriz_riscos_grc.xlsx`) e aos controles do Anexo A da ISO/IEC 27001:2022.

| Seção da PSI | Risco(s) relacionado(s) | Controles ISO/IEC 27001:2022 (Anexo A) |
| :--- | :--- | :--- |
| 4.1 Classificação da informação | R-01 | A.5.12, A.5.13 |
| 4.2 Controle de acesso e ativos | R-01, R-04 | A.5.15, A.5.18, A.8.2, A.8.15 |
| 4.3 Uso aceitável | R-03 | A.5.10, A.6.3 |
| 4.4 Criptografia e proteção de dados | R-10 | A.8.1, A.8.24, A.7.9 |
| 4.5 Segurança de rede e disponibilidade | R-07 | A.8.20, A.8.14 |
| 4.6 Backup e continuidade | R-02 | A.8.13, A.5.30 |
| 4.7 Gestão de vulnerabilidades | R-05 | A.8.8 |
| 4.8 Desenvolvimento seguro e segredos | R-06 | A.8.4, A.8.28 |
| 4.9 Descarte seguro | R-08 | A.7.14, A.7.10, A.8.10 |
| 4.10 Terceiros e fornecedores | R-09 | A.5.19, A.5.20, A.5.22 |
| 4.11 Gestão de incidentes | R-03 | A.5.24, A.5.26, A.6.8 |
| 5. Senhas e autenticação (MFA) | R-04, R-01 | A.5.17, A.8.5, A.8.2 |
| 3.4 / 4.11 Privacidade e DPO | R-01, R-09 | A.5.34 |

---

## 10. Histórico de Revisões

| Data | Versão | Descrição da Alteração | Autor | Aprovação |
| :--- | :---: | :--- | :--- | :--- |
| 08/10/2026 | 1.0 | Criação e publicação inicial do documento. | Equipe de GRC / TI | Direção |
| 08/10/2026 | 1.1 | Política de senhas alinhada ao NIST SP 800-63B (sem rotação forçada, sem regras de composição, MFA para contas administrativas); inclusão do DPO e da comunicação de incidentes à ANPD; segregação de funções entre TI e GRC; novas seções (classificação, rede, backup, vulnerabilidades, desenvolvimento seguro, descarte, terceiros, exceções, revisão); tabela de rastreabilidade com a matriz de riscos; correções de redação. | Equipe de GRC / TI | Direção |
