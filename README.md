
#  Habitus

**Habitus** é um aplicativo de gerenciamento de hábitos desenvolvido como Projeto Livre da disciplina de **Orientação a Objetos (UnB FGA)**. Ele permite que usuários registrem seus hábitos diários, semanais ou mensais, acompanhem seu progresso e mantenham o foco nas metas pessoais com uma interface simples e intuitiva.

---

##  Funcionalidades

-  Cadastrar novos hábitos com:
  - Nome
  - Descrição
  - Categoria
  - Periodicidade (diário, semanal ou mensal)
-  Marcar hábito como concluído no dia atual
-  Visualizar lista de hábitos ativos com progresso e última conclusão
-  Editar e excluir hábitos existentes
-  Persistência dos dados (os hábitos são salvos automaticamente)
-  Interface gráfica com botões intuitivos e lista dinâmica

---

##  Interface Gráfica

Interface construída com **Tkinter**, apresentando:

- Botão  para novo hábito
- Lista com progresso de cada hábito
- Botões  para edição e 🗑 para exclusão
- Registro instantâneo com  “Marcar como feito”




##  Estrutura do Projeto

```
habitus/
├── interface_v3_sem_grafico.py
├── main.py
├── README.md
├── Habitus.code-workspace
├── dados.pkl
├── package/
│   ├── __init__.py
│   ├── habit.py
│   ├── user.py
│   ├── categoria.py
│   ├── registro.py
│   └── storage.py
└── diagrama_classes_habitus.png
```

---

##  Conceitos de POO aplicados

-  **Encapsulamento**
-  **Herança** (`HabitoDiario`, `HabitoSemanal`, `HabitoMensal`)
-  **Polimorfismo** (`progresso()` implementado por tipo de hábito)
-  **Mixin** (`ExportavelMixin` para exportação em JSON)
-  **Composição** (`Habito` contém `Registro`)
-  **Associação fraca** (`Usuario` possui múltiplos `Habitos`)

---

##  Serialização

Todos os dados são salvos automaticamente usando o módulo `pickle`.  
O arquivo `dados.pkl` garante que os hábitos persistam entre sessões.

---

##  Diagrama de Classes UML

Arquivo incluído: `diagrama_classes_habitus.png`  
Exibe as classes principais, atributos, métodos e relacionamentos.

---
##  Projeto Acadêmico

- **Disciplina:** Orientação a Objetos
- **Curso:** Engenharia de Software – FGA/UnB
- **Semestre:** 01/2025
- **Professor:** Henrique Moura
- **Aluno:** Bruno Augusto

---

##  Licença

Uso acadêmico exclusivo.  
Projeto desenvolvido para fins de avaliação e aprendizado.
