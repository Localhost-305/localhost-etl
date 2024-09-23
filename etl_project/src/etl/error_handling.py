def map_error_message(error_message):
    if "Duplicate entry" in error_message:
        return "Valor já existente no banco de dados"
    elif "FOREIGN KEY" in error_message:
        return "Chave estrangeira ausente no banco de dados"
    elif "Object of type Timestamp is not JSON serializable" in error_message:
        return "Erro de formatação de data - Tipo Timestamp não serializável"
    elif "DataError" in error_message:
        return "Tamanho do valor excede o limite permitido"
    elif "NOT NULL" in error_message:
        return "Tentativa de inserir um valor nulo em um campo obrigatório"
    elif "TypeError" in error_message:
        return "Tipo de dado incorreto"
    elif "Too many connections" in error_message:
        return "Excesso de conexões simultâneas ao banco de dados"
    elif "TimeoutError" in error_message:
        return "Tempo limite da operação excedido"
    elif "MemoryError" in error_message:
        return "Memória insuficiente para processar os dados"
    elif "OperationalError" in error_message:
        return "Erro de conexão ou operação no banco de dados"
    elif "Primary key violation" in error_message:
        return "Violação de chave primária. Registro já existe."
    elif "Unique constraint failed" in error_message:
        return "Violação de restrição de unicidade. Registro duplicado."
    elif "TransactionError" in error_message:
        return "Erro ao gerenciar a transação. A operação foi revertida."
    else:
        return f"Erro desconhecido: {error_message}"
