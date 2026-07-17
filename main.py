from app.services.excel_service import ExcelService

excel = ExcelService("data/cancelados.xlsx")

excel.abrir()

print(excel.listar_abas())