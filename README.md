# 🚚 Flash Delivery

Sistema de gestão de entregas em Python para a startup **Flash Delivery**, que conecta entregadores a clientes locais.

## 🎯 Sobre o Projeto

Projeto desenvolvido como parte do **Fast Hackathon** do curso de Análise e Desenvolvimento de Sistemas (ADS). O sistema substitui planilhas de Excel no gerenciamento central de entregas, proporcionando maior eficiência e controle.

## ✨ Funcionalidades

### 📦 1. Cadastrar Nova Entrega
- Registro completo de pedidos com ID único
- Captura de dados: cliente, distância, peso do pacote
- Status automático: "Pendente"
- Cálculo automático do valor do frete

### 🧮 2. Calcular Valor do Frete
- Teste independente do cálculo de frete
- Aplica regras específicas da empresa
- Mostra detalhamento do cálculo

### 📋 3. Listar Todas as Entregas
- Relatório completo de entregas cadastradas
- Visualização organizada com todos os campos
- Informações: ID, cliente, distância, peso, frete e status

### ✅ 4. Alterar Status (Entrega Realizada)
- Busca de entregas por ID
- Alteração de status: "Pendente" → "Entregue"
- Confirmação antes da alteração

### 🚪 5. Sair do Sistema
- Encerramento seguro do programa

## 💰 Regras de Cálculo do Frete

1. **Taxa Base:** R$ 10,00 (fixa para qualquer entrega)
2. **Adicional por Km:** R$ 1,50 por Km rodado
3. **Taxa de Peso:** 
   - Pacotes até 5 Kg: sem taxa adicional
   - Pacotes acima de 5 Kg: + R$ 15,00

### Fórmula do Cálculo
Frete = R$ 10,00 + (Distância × R$ 1,50) + Taxa de Peso
### Exemplo Prático
Entrega: 10 Km, 7 Kg
Cálculo: R$ 10,00 + (10 × R$ 1,50) + R$ 15,00 = R$ 40,00

---

## 🏗️ Estrutura Técnica

### Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Persistência:** Lista de dicionários em memória
- **Interface:** Terminal/Console
- **Sistema Operacional:** Compatível com Windows/Linux/Mac

### Arquitetura de Dados
`python
entregas = [
    {
        'id': 1001,
        'cliente': 'Maria Silva',
        'distancia': 15.5,
        'peso': 8.2,
        'frete': 48.25,
        'status': 'Pendente'
    }
]`

---

## 🧠 Aprendizados
- Implementação de fórmulas matemáticas em código
- Estruturação de dados com dicionários aninhados
- Validação básica de entrada do usuário
- Controle de fluxo com loops e condições
- Organização de sistemas modulares

---

## 👩‍💻 Desenvolvido por
Arielle Beatriz Domingos da Silva
