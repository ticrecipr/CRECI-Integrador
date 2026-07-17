from app.services.excel_service import ExcelService

excel = ExcelService("SUA_PLANILHA.xlsx")

excel.abrir()

print(excel.listar_abas())