# Velb Pay

Um sistema simples de notas financeiras escrito em Python.

## Uso

```bash
# Adicionar uma nota
python -m finance_notes.cli add "Descri\u00e7\u00e3o" 100.0

# Listar notas
python -m finance_notes.cli list

# Remover uma nota pelo ID
python -m finance_notes.cli delete 1
```

As notas s\u00e3o armazenadas no arquivo `notes.json`. Voc\u00ea pode definir o caminho desse arquivo usando a vari\u00e1vel de ambiente `NOTES_PATH`.
