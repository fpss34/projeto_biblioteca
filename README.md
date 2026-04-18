# projeto_biblioteca

{
  "openapi": "3.1.0",
  "info": {
    "title": "API de Livros",
    "version": "1.0.0",
    "description": "API simples para gerenciamento de livros (CRUD) usando FastAPI"
  },
  "paths": {
    "/db-test": {
      "get": {
        "summary": "Testar conexão com banco",
        "description": "Verifica se a conexão com o banco de dados está funcionando",
        "operationId": "testDb",
        "responses": {
          "200": {
            "description": "Conexão bem-sucedida",
            "content": {
              "application/json": {
                "example": {
                  "status": "ok"
                }
              }
            }
          }
        }
      }
    },
    "/livros/": {
      "get": {
        "summary": "Listar livros",
        "description": "Retorna todos os livros cadastrados",
        "operationId": "listarLivros",
        "responses": {
          "200": {
            "description": "Lista de livros",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Livro"
                  }
                }
              }
            }
          }
        }
      },
      "post": {
        "summary": "Criar livro",
        "description": "Cria um novo livro no sistema",
        "operationId": "criarLivro",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/LivroInput"
              },
              "example": {
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis",
                "ano": 1899
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Livro criado com sucesso",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Livro"
                }
              }
            }
          },
          "422": {
            "description": "Erro de validação",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/livros/{id}": {
      "get": {
        "summary": "Buscar livro",
        "description": "Busca um livro pelo ID",
        "operationId": "buscarLivro",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "ID do livro"
          }
        ],
        "responses": {
          "200": {
            "description": "Livro encontrado",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Livro"
                }
              }
            }
          },
          "404": {
            "description": "Livro não encontrado"
          }
        }
      },
      "delete": {
        "summary": "Deletar livro",
        "description": "Remove um livro pelo ID",
        "operationId": "deletarLivro",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer"
            },
            "description": "ID do livro"
          }
        ],
        "responses": {
          "200": {
            "description": "Livro deletado com sucesso",
            "content": {
              "application/json": {
                "example": {
                  "message": "Livro removido"
                }
              }
            }
          },
          "404": {
            "description": "Livro não encontrado"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Livro": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "example": 1
          },
          "titulo": {
            "type": "string",
            "example": "Dom Casmurro"
          },
          "autor": {
            "type": "string",
            "example": "Machado de Assis"
          },
          "ano": {
            "type": "integer",
            "example": 1899
          }
        }
      },
      "LivroInput": {
        "type": "object",
        "required": ["titulo", "autor"],
        "properties": {
          "titulo": {
            "type": "string"
          },
          "autor": {
            "type": "string"
          },
          "ano": {
            "type": "integer"
          }
        }
      },
      "HTTPValidationError": {
        "type": "object",
        "properties": {
          "detail": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            }
          }
        }
      },
      "ValidationError": {
        "type": "object",
        "required": ["loc", "msg", "type"],
        "properties": {
          "loc": {
            "type": "array",
            "items": {
              "anyOf": [
                { "type": "string" },
                { "type": "integer" }
              ]
            }
          },
          "msg": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        }
      }
    }
  }
}